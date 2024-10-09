namespace Weather.Models
{
    public record DailyForecast
    {
        public float? High { get; set; }
        public float? Low { get; set; }
        public string? Icon { get; set; }
        public List<ForecastItem>? Details { get; set; }
    }
}