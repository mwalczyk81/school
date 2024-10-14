using Microsoft.AspNetCore.WebUtilities;
using System.Text.Json;
using Weather.Models.Location;

namespace Weather.Services
{
    public interface ICitySuggestionService
    {
        Task<IEnumerable<CitySuggestion>> GetCitySuggestionsAsync(string input, CancellationToken cancellationToken);
    }

    public class CitySuggestionService(IHttpClientFactory httpClientFactory, ILogger<CitySuggestionService> logger, JsonSerializerOptions jsonSerializerOptions) : ICitySuggestionService
    {
        private readonly IHttpClientFactory _httpClientFactory = httpClientFactory;
        private readonly ILogger<CitySuggestionService> _logger = logger;
        private readonly JsonSerializerOptions _jsonSerializerOptions = jsonSerializerOptions;

        public async Task<IEnumerable<CitySuggestion>> GetCitySuggestionsAsync(string input, CancellationToken cancellationToken)
        {
            if (string.IsNullOrWhiteSpace(input) || input.Length < 2)
            {
                _logger.LogWarning("No input to search for.");
                return [];
            }

            var username = "mwalczyk";
            var query = new Dictionary<string, string?>
            {
                { "q", input },
                { "maxRows", "5" },
                { "username", username },
                { "featureClass", "P" },
                { "style", "full" }
            };

            var url = QueryHelpers.AddQueryString("searchJSON", query);

            using var client = _httpClientFactory.CreateClient("Cities");
            var response = await client.GetAsync(url, cancellationToken);

            response.EnsureSuccessStatusCode();

            var result = await JsonSerializer.DeserializeAsync<GeoNamesResult>(await response.Content.ReadAsStreamAsync(cancellationToken), _jsonSerializerOptions, cancellationToken: cancellationToken);

            if (result?.Geonames == null || result.Geonames.Count == 0)
            {
                _logger.LogError("No city names returned.");
                return [];
            }

            return result.Geonames.Select(geoname => new CitySuggestion
            {
                DisplayName = $"{geoname.Name}, {geoname.AdminName1}, {geoname.CountryName}", // City, State, Country
                Lat = geoname.Lat,
                Lng = geoname.Lng
            });
        }
    }
}