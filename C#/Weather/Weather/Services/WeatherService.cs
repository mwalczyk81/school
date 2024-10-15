namespace Weather.Services
{
    using Microsoft.AspNetCore.WebUtilities;
    using System.Globalization;
    using System.Text.Json;
    using Weather.Models.Weather;

    public interface IWeatherService
    {
        Task<WeatherResponse?> GetWeatherAsync(double? lat, double? lon);
    }

    public class WeatherService(IHttpClientFactory httpClientFactory, JsonSerializerOptions jsonSerializerOptions) : IWeatherService
    {
        private readonly IHttpClientFactory _httpClientFactory = httpClientFactory;
        private readonly JsonSerializerOptions _jsonSerializerOptions = jsonSerializerOptions;
        private const string ApiKey = "906b6939735602a519447e37a839d229";

        public async Task<WeatherResponse?> GetWeatherAsync(double? lat, double? lon)
        {
            if (lat is null)
            {
                throw new ArgumentNullException(nameof(lat));
            }

            if (lon is null)
            {
                throw new ArgumentNullException(nameof(lon));
            }

            string currentUrl, forecastUrl;
            var queryParams = new Dictionary<string, string?>
            {
                { "appid", ApiKey },
                { "units", "imperial" },
                { "lat", lat.Value.ToString() },
                { "lon", lon.Value.ToString() }
            };

            currentUrl = QueryHelpers.AddQueryString("weather", queryParams);
            forecastUrl = QueryHelpers.AddQueryString("forecast", queryParams);

            var currentWeather = await FetchDataAsync<WeatherData>(currentUrl);
            var forecastWeather = await FetchDataAsync<ForecastData>(forecastUrl);

            if (currentWeather != null && forecastWeather != null)
            {
                var dailySummary = ProcessForecastData(forecastWeather);
                return new WeatherResponse { WeatherData = currentWeather, DailyForecasts = dailySummary };
            }

            return null;
        }

        private async Task<T?> FetchDataAsync<T>(string url)
        {
            using var client = _httpClientFactory.CreateClient("Weather");
            var response = await client.GetAsync(url);

            response.EnsureSuccessStatusCode();

            var result = await JsonSerializer.DeserializeAsync<T>(await response.Content.ReadAsStreamAsync(), _jsonSerializerOptions);

            return result is null ? default : result;
        }

        private static Dictionary<string, DailyForecast> ProcessForecastData(ForecastData? forecastWeather)
        {
            var dailySummary = new Dictionary<string, DailyForecast>();

            if (forecastWeather?.List == null)
                return dailySummary;

            var forecastGrouped = forecastWeather.List
                .GroupBy(entry =>
                {
                    // Adjust the time using the timezone offset
                    var utcTime = DateTime.ParseExact(entry.Dt_Txt ?? "", "yyyy-MM-dd HH:mm:ss", CultureInfo.InvariantCulture);
                    var localTime = utcTime.AddSeconds(forecastWeather.City?.Timezone ?? 0);

                    entry.Dt_Txt = localTime.ToString("yyyy-MM-dd HH:mm:ss");

                    return localTime.ToString("yyyy-MM-dd");
                });

            // Calculate high/low temperatures for each day and build the daily summary
            foreach (var group in forecastGrouped)
            {
                dailySummary[group.Key] = new DailyForecast
                {
                    High = group.Select(entry => entry.Main?.Temp_Max).ToList().Max(),
                    Low = group.Select(entry => entry.Main?.Temp_Min).ToList().Min(),
                    Icon = group.First().Weather?[0].Icon ?? "",
                    Details = [.. group]
                };
            }

            return dailySummary;
        }
    }
}