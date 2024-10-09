namespace Weather.Models
{
    public record WeatherResponse
    {
        public WeatherData? WeatherData { get; set; }
        public Dictionary<string, DailyForecast>? DailyForecasts { get; set; }
    }
}