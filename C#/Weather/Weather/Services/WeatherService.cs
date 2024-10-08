namespace Weather.Services
{
    using System.Globalization;
    using System.Text.Json;
    using Weather.Models;

    public class WeatherService(HttpClient httpClient)
    {
        private readonly HttpClient _httpClient = httpClient;
        private const string ApiKey = "906b6939735602a519447e37a839d229";

        public JsonSerializerOptions GetOptions()
        {
            return new JsonSerializerOptions() { PropertyNameCaseInsensitive = true };
        }

        public async Task<IEnumerable<CitySuggestion>> GetCitySuggestionsAsync(string input, JsonSerializerOptions options, CancellationToken cancellationToken)
        {
            if (string.IsNullOrWhiteSpace(input) || input.Length < 2)
            {
                return [];
            }

            var username = "mwalczyk";  // Use your GeoNames username
            var url = $"http://api.geonames.org/searchJSON?q={input}&maxRows=5&username={username}&featureClass=P&style=full";

            using var client = new HttpClient();
            var response = await client.GetAsync(url, cancellationToken);
            var result = await JsonSerializer.DeserializeAsync<GeoNamesResult>(await response.Content.ReadAsStreamAsync(cancellationToken), options, cancellationToken);

            if (result?.Geonames == null || !result.Geonames.Any())
                return [];

            return result.Geonames.Select(g => new CitySuggestion
            {
                DisplayName = $"{g.Name}, {g.AdminName1}, {g.CountryName}", // City, State, Country
                Lat = g.Lat,
                Lng = g.Lng
            });
        }

        public async Task<(WeatherData?, Dictionary<string, DailyForecast>?, string?)> GetWeatherAsync(string? city = null, double? lat = null, double? lon = null)
        {
            string currentUrl;
            string forecastUrl;

            if (city != null)
            {
                currentUrl = $"weather?q={city}&appid={ApiKey}&units=imperial";
                forecastUrl = $"forecast?q={city}&appid={ApiKey}&units=imperial";
            }
            else if (lat.HasValue && lon.HasValue)
            {
                currentUrl = $"weather?lat={lat}&lon={lon}&appid={ApiKey}&units=imperial";
                forecastUrl = $"forecast?lat={lat}&lon={lon}&appid={ApiKey}&units=imperial";
            }
            else
            {
                return (null, null, "City or location not provided.");
            }

            var currentResponse = await _httpClient.GetAsync(currentUrl);
            var forecastResponse = await _httpClient.GetAsync(forecastUrl);

            if (currentResponse.IsSuccessStatusCode && forecastResponse.IsSuccessStatusCode)
            {
                var options = new JsonSerializerOptions() { PropertyNameCaseInsensitive = true };
                var currentWeather = await JsonSerializer.DeserializeAsync<WeatherData>(await currentResponse.Content.ReadAsStreamAsync(), options);
                var forecastWeather = await JsonSerializer.DeserializeAsync<ForecastData>(await forecastResponse.Content.ReadAsStreamAsync(), options);
                var timezoneOffset = forecastWeather?.City?.Timezone ?? 0;
                var forecastGrouped = new Dictionary<string, List<ForecastItem>>();
                var dailySummary = new Dictionary<string, DailyForecast>();

                if (forecastWeather?.List != null)
                {
                    foreach (var entry in forecastWeather.List)
                    {
                        DateTime utcTime = DateTime.ParseExact(entry.Dt_Txt ?? "", "yyyy-MM-dd HH:mm:ss", CultureInfo.InvariantCulture);

                        // Adjust the time using the timezone offset (in seconds)
                        DateTime localTime = utcTime.AddSeconds(timezoneOffset);

                        // Update `dt_txt` to reflect the adjusted local time
                        entry.Dt_Txt = localTime.ToString("yyyy-MM-dd HH:mm:ss");

                        // Extract the local date part
                        string localDateStr = localTime.ToString("yyyy-MM-dd");

                        // Group by the local date
                        if (!forecastGrouped.TryGetValue(localDateStr, out List<ForecastItem>? value))
                        {
                            value = ([]);
                            forecastGrouped[localDateStr] = value;
                        }

                        value.Add(entry);
                    }

                    // Calculate high/low temperatures for each day and build the daily summary
                    foreach (var group in forecastGrouped)
                    {
                        var highs = group.Value.Select(entry => entry.Main?.Temp_Max).ToList();
                        var lows = group.Value.Select(entry => entry.Main?.Temp_Min).ToList();
                        var highTemp = highs.Max();
                        var lowTemp = lows.Min();
                        var weatherIcon = group.Value.First().Weather?[0].Icon;

                        dailySummary[group.Key] = new DailyForecast
                        {
                            High = highTemp,
                            Low = lowTemp,
                            Icon = weatherIcon ?? "",
                            Details = group.Value
                        };
                    }
                }

                return (currentWeather, dailySummary, null);
            }
            else
            {
                return (null, null, "Failed to retrieve weather data.");
            }
        }
    }
}