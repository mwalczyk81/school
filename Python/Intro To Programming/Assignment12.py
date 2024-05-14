# Assignment 12
# Written by Matthew Walczyk 
# 2/26/2024
import json, re, requests
from types import SimpleNamespace

base_url = "https://api.openweathermap.org/data/2.5/weather"
appid = "906b6939735602a519447e37a839d229"
# Main function
def main():

    continue_lookup = "1"

    while(continue_lookup == "1"):
        zip_code = input("Enter the zip code for the weather to look up: ")

        # Make sure the input is numeric and 5 digits
        x = re.match("\d{5}$", zip_code)

        # Start loop over if the user entered an invalid zip
        if( x == None):
            print(f"Invalid zip code: {zip_code}")
            continue_lookup = input("Press 1 to continue or 2 to end: ")
            continue

        url = f"{base_url}?q={zip_code}&units=imperial&APPID={appid}"

        response = requests.get(url)

        weather = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))

        # Print weather data in a formatted style
        print(f"The tempature in {weather.name} is {weather.main.temp} and the humidity is {weather.main.humidity} with a windspeed of {weather.wind.speed}")

        continue_lookup = input("Press 1 to continue or 2 to end: ")

# Call main function
main()