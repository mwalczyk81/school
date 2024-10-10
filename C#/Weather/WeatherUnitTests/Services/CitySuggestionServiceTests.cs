using Microsoft.Extensions.Logging;
using NSubstitute;
using System.Net;
using System.Text.Json;
using Weather.Services;

namespace WeatherUnitTests.Services
{
    using System;
    using System.Linq;
    using System.Net.Http;
    using System.Threading;
    using System.Threading.Tasks;
    using Xunit;
    using static WeatherUnitTests.Helpers;

    public class CitySuggestionServiceTests
    {
        private readonly IHttpClientFactory _httpClientFactory;
        private readonly ILogger<CitySuggestionService> _logger;
        private readonly JsonSerializerOptions _jsonSerializerOptions;
        private readonly CitySuggestionService _citySuggestionService;

        public CitySuggestionServiceTests()
        {
            _httpClientFactory = Substitute.For<IHttpClientFactory>();
            _logger = Substitute.For<ILogger<CitySuggestionService>>();
            _jsonSerializerOptions = new JsonSerializerOptions { PropertyNameCaseInsensitive = true };
            _citySuggestionService = new CitySuggestionService(_httpClientFactory, _logger, _jsonSerializerOptions);
        }

        [Fact]
        public async Task GetCitySuggestionsAsync_WithValidInput_ReturnsCitySuggestions()
        {
            // Arrange
            var input = "Lon";
            var geoNamesJson = "{\"geonames\": [{\"name\": \"London\", \"adminName1\": \"England\", \"countryName\": \"United Kingdom\", \"lat\": \"51.5074\", \"lng\": \"-0.1278\"}]}";

            var responses = new Dictionary<string, HttpResponseMessage>
            {
                { "searchJSON", new HttpResponseMessage(HttpStatusCode.OK) { Content = new StringContent(geoNamesJson) } }
            };

            var httpClient = Substitute.For<HttpClient>(new HttpMessageHandlerStub(responses));
            httpClient.BaseAddress = new Uri("https://api.geonames.org/");

            _httpClientFactory.CreateClient(Arg.Any<string>()).Returns(httpClient);

            // Act
            var result = await _citySuggestionService.GetCitySuggestionsAsync(input, CancellationToken.None);

            // Assert
            Assert.NotNull(result);
            Assert.Single(result);
            Assert.Equal("London, England, United Kingdom", result.First().DisplayName);
        }

        [Fact]
        public async Task GetCitySuggestionsAsync_WithShortInput_ReturnsEmpty()
        {
            // Arrange
            var input = "L";

            // Act
            var result = await _citySuggestionService.GetCitySuggestionsAsync(input, CancellationToken.None);

            // Assert
            Assert.Empty(result);
            _logger.Received().LogWarning("No input to search for.");
        }

        [Fact]
        public async Task GetCitySuggestionsAsync_WithEmptyInput_ReturnsEmpty()
        {
            // Arrange
            var input = "";

            // Act
            var result = await _citySuggestionService.GetCitySuggestionsAsync(input, CancellationToken.None);

            // Assert
            Assert.Empty(result);
            _logger.Received().LogWarning("No input to search for.");
        }

        [Fact]
        public async Task GetCitySuggestionsAsync_WithApiError_ThrowsHttpRequestException()
        {
            // Arrange
            var input = "Lon";

            var responses = new Dictionary<string, HttpResponseMessage>
            {
                { "searchJSON", new HttpResponseMessage(HttpStatusCode.InternalServerError) }
            };

            var httpClient = Substitute.For<HttpClient>(new HttpMessageHandlerStub(responses));
            httpClient.BaseAddress = new Uri("https://api.geonames.org/");

            _httpClientFactory.CreateClient(Arg.Any<string>()).Returns(httpClient);

            // Act & Assert
            await Assert.ThrowsAsync<HttpRequestException>(() => _citySuggestionService.GetCitySuggestionsAsync(input, CancellationToken.None));
        }

        [Fact]
        public async Task GetCitySuggestionsAsync_WithNoResults_ReturnsEmpty()
        {
            // Arrange
            var input = "Lon";
            var geoNamesJson = "{\"geonames\": []}";

            var responses = new Dictionary<string, HttpResponseMessage>
            {
                { "searchJSON", new HttpResponseMessage(HttpStatusCode.OK) { Content = new StringContent(geoNamesJson) } }
            };

            var httpClient = Substitute.For<HttpClient>(new HttpMessageHandlerStub(responses));
            httpClient.BaseAddress = new Uri("https://api.geonames.org/");

            _httpClientFactory.CreateClient(Arg.Any<string>()).Returns(httpClient);

            // Act
            var result = await _citySuggestionService.GetCitySuggestionsAsync(input, CancellationToken.None);

            // Assert
            Assert.Empty(result);
            _logger.Received().LogError("No city names returned.");
        }
    }
}