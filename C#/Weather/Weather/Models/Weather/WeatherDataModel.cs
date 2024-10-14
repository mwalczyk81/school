namespace Weather.Models.Weather
{
    public class WeatherDataModel
    {
        public WeatherResponse? WeatherResponse { get; set; }
        public string? ErrorMessage { get; set; }
        public string? ExpandedDay { get; set; } = "";
        public bool IsLoading { get; set; } = false;
    }
}