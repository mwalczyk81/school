namespace Weather.Models
{
    public record ForecastData
    {
        public City? City { get; set; }
        public List<ForecastItem>? List { get; set; }
    }
}