namespace Weather.Models
{
    public record DailyForecast
    {
        public double? High { get; set; }
        public double? Low { get; set; }
        public string? Icon { get; set; }
        public List<ForecastItem>? Details { get; set; }
    }
}