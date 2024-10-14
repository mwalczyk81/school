using Weather.Models.Location;

namespace Weather.Models.Weather
{
    public record ForecastData
    {
        public City? City { get; set; }
        public List<ForecastItem>? List { get; set; }
    }
}