namespace Weather.Models
{
    public record Weather
    {
        public string? Description { get; set; }
        public string? Icon { get; set; }
    }
}