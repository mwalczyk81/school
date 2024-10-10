namespace Weather.Models
{
    public record ForecastItem
    {
        public string? Dt_Txt { get; set; } // Forecast timestamp
        public Main? Main { get; set; }
        public List<Weather>? Weather { get; set; }
        public Wind? Wind { get; set; }
        public Rain? Rain { get; set; }
    }
}