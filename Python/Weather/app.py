from flask import Flask, render_template, request
import requests
from collections import defaultdict
from datetime import datetime
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

app = Flask(__name__)

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Custom filter to format the date in a friendly way
@app.template_filter('datetimeformat')
def datetimeformat(value):
    date_obj = datetime.strptime(value, '%Y-%m-%d')
    return date_obj.strftime('%A, %B %d')

def get_weather(city=None, lat=None, lon=None):
    if city:
        current_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
        forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=imperial"
    elif lat and lon:
        current_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial"
        forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial"

    current_response = requests.get(current_url)
    forecast_response = requests.get(forecast_url)

    if current_response.status_code == 200 and forecast_response.status_code == 200:
        current_weather = current_response.json()
        forecast_weather = forecast_response.json()

        timezone_offset = forecast_weather['city']['timezone']  # Get timezone offset in seconds
        forecast_grouped = defaultdict(list)

        for entry in forecast_weather['list']:
            utc_time = datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S')
            local_time = utc_time + timedelta(seconds=timezone_offset)  # Adjust time to local

            entry['dt_txt'] = local_time.strftime('%Y-%m-%d %H:%M:%S')
            date_str = entry['dt_txt'].split(" ")[0]
            forecast_grouped[date_str].append(entry)

        # Calculate high/low temperatures for each day
        daily_summary = {}
        for date, entries in forecast_grouped.items():
            temps = [entry['main']['temp'] for entry in entries]
            high_temp = max(temps)
            low_temp = min(temps)
            weather_icon = entries[0]['weather'][0]['icon']  # Use the first entry's icon for the day
            daily_summary[date] = {
                'high': high_temp,
                'low': low_temp,
                'icon': weather_icon,
                'details': entries  # Keep detailed forecast for later
            }

        return current_weather, daily_summary, None  # Return daily summary instead of grouped entries
    else:
        return None, None, "City or location not found"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    forecast_data = None
    error = None
    if request.method == "POST":
        city = request.form.get("city")
        lat = request.form.get("lat")
        lon = request.form.get("lon")

        if city:
            weather_data, forecast_data, error = get_weather(city=city)
        elif lat and lon:
            weather_data, forecast_data, error = get_weather(lat=lat, lon=lon)
        else:
            error = "Please enter a city or use geolocation."

        # Ensure forecast data exists and has at least 1 date entry
        if not forecast_data or len(forecast_data) == 0:
            forecast_data = None
            error = error or "Unable to retrieve forecast data."

    return render_template("index.html", weather=weather_data, forecast=forecast_data, error=error)


if __name__ == "__main__":
    app.run(debug=True)
