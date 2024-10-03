namespace Weather.Models
{
    public class ForecastData
    {
        public City? City { get; set; }
        public List<ForecastItem>? List { get; set; }
    }
}