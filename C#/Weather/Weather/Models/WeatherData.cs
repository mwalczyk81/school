namespace Weather.Models
{
    public record WeatherData
    {
        public Main? Main { get; set; }
        public Weather[]? Weather { get; set; }
        public string? Name { get; set; }
    }
}