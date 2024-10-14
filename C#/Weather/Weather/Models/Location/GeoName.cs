namespace Weather.Models.Location
{
    public class GeoName
    {
        public string? Name { get; set; }
        public string? CountryName { get; set; }
        public string? AdminName1 { get; set; }  // State or province
        public string? Lat { get; set; }
        public string? Lng { get; set; }
    }
}