namespace Weather.Models.Weather
{
    public record WeatherData
    {
        public Main? Main { get; set; }
        public WeatherItem[]? Weather { get; set; }
        public string? Name { get; set; }
    }
}