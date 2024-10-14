namespace Weather.Models.Weather
{
    public record Main
    {
        public float? Temp { get; set; }
        public float? Temp_Min { get; set; }
        public float? Temp_Max { get; set; }
        public int? Humidity { get; set; }
    }
}