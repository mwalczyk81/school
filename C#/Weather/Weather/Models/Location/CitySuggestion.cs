namespace Weather.Models.Location
{
    public class CitySuggestion
    {
        public string? DisplayName { get; set; } // For displaying in autocomplete
        public string? Lat { get; set; }
        public string? Lng { get; set; }
    }
}