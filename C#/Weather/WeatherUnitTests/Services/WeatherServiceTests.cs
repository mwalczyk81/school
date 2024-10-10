namespace WeatherUnitTests.Services
{
    using NSubstitute;
    using System;
    using System.Net;
    using System.Net.Http;
    using System.Text.Json;
    using System.Threading.Tasks;
    using Weather.Services;
    using Xunit;
    using static WeatherUnitTests.Helpers;

    public class WeatherServiceTests
    {
        private readonly IHttpClientFactory _httpClientFactory;
        private readonly JsonSerializerOptions _jsonSerializerOptions;
        private readonly WeatherService _weatherService;

        public WeatherServiceTests()
        {
            _httpClientFactory = Substitute.For<IHttpClientFactory>();
            _jsonSerializerOptions = new JsonSerializerOptions { PropertyNameCaseInsensitive = true };
            _weatherService = new WeatherService(_httpClientFactory, _jsonSerializerOptions);
        }

        [Fact]
        public async Task GetWeatherAsync_WithCity_ReturnsWeatherResponse()
        {
            // Arrange
            var city = "London";
            var currentWeatherJson = "{\"main\": {\"temp\": 280.32}, \"weather\": [{\"icon\": \"10d\"}], \"name\": \"London\"}";
            var forecastWeatherJson = "{\"city\": {\"timezone\": 0}, \"list\": [{\"dt_txt\": \"2023-10-01 12:00:00\", \"main\": {\"temp_max\": 285.32, \"temp_min\": 275.32}, \"weather\": [{\"icon\": \"10d\"}]}]}";

            var currentWeatherResponse = new HttpResponseMessage(HttpStatusCode.OK)
            {
                Content = new StringContent(currentWeatherJson)
            };

            var forecastWeatherResponse = new HttpResponseMessage(HttpStatusCode.OK)
            {
                Content = new StringContent(forecastWeatherJson)
            };

            var responses = new Dictionary<string, HttpResponseMessage>
            {
                { "weather?", currentWeatherResponse},
                { "forecast?", forecastWeatherResponse}
            };

            var httpClient = Substitute.For<HttpClient>(new HttpMessageHandlerStub(responses));
            httpClient.BaseAddress = new Uri("https://api.openweathermap.org/data/2.5/");

            _httpClientFactory.CreateClient(Arg.Any<string>()).Returns(httpClient);

            // Act
            var result = await _weatherService.GetWeatherAsync(city);

            // Assert
            Assert.NotNull(result);
            Assert.Equal("London", result.WeatherData?.Name);
            Assert.NotNull(result.DailyForecasts);
            Assert.Single(result.DailyForecasts);
        }

        [Fact]
        public async Task GetWeatherAsync_WithLatLon_ReturnsWeatherResponse()
        {
            // Arrange
            var lat = 51.5074;
            var lon = -0.1278;
            var currentWeatherJson = "{\"main\": {\"temp\": 280.32}, \"weather\": [{\"icon\": \"10d\"}], \"name\": \"London\"}";
            var forecastWeatherJson = "{\"city\": {\"timezone\": 0}, \"list\": [{\"dt_txt\": \"2023-10-01 12:00:00\", \"main\": {\"temp_max\": 285.32, \"temp_min\": 275.32}, \"weather\": [{\"icon\": \"10d\"}]}]}";

            var currentWeatherResponse = new HttpResponseMessage(HttpStatusCode.OK)
            {
                Content = new StringContent(currentWeatherJson)
            };

            var forecastWeatherResponse = new HttpResponseMessage(HttpStatusCode.OK)
            {
                Content = new StringContent(forecastWeatherJson)
            };

            var responses = new Dictionary<string, HttpResponseMessage>
            {
                { "weather?", currentWeatherResponse},
                { "forecast?", forecastWeatherResponse}
            };

            var httpClient = Substitute.For<HttpClient>(new HttpMessageHandlerStub(responses));
            httpClient.BaseAddress = new Uri("https://api.openweathermap.org/data/2.5/");

            _httpClientFactory.CreateClient(Arg.Any<string>()).Returns(httpClient);

            // Act
            var result = await _weatherService.GetWeatherAsync(null, lat, lon);

            // Assert
            Assert.NotNull(result);
            Assert.Equal("London", result.WeatherData?.Name);
            Assert.NotNull(result.DailyForecasts);
            Assert.Single(result.DailyForecasts);
        }

        [Fact]
        public async Task GetWeatherAsync_WithoutCityOrLatLon_ThrowsArgumentException()
        {
            // Act & Assert
            await Assert.ThrowsAsync<ArgumentException>(() => _weatherService.GetWeatherAsync());
        }

        [Fact]
        public async Task GetWeatherAsync_WithInvalidCity_Throws()
        {
            // Arrange
            var city = "InvalidCity";
            var currentWeatherResponse = new HttpResponseMessage(HttpStatusCode.NotFound);
            var forecastWeatherResponse = new HttpResponseMessage(HttpStatusCode.NotFound);

            var responses = new Dictionary<string, HttpResponseMessage>
            {
                { "weather?", currentWeatherResponse},
                { "forecast?", forecastWeatherResponse}
            };

            var httpClient = Substitute.For<HttpClient>(new HttpMessageHandlerStub(responses));
            httpClient.BaseAddress = new Uri("https://api.openweathermap.org/data/2.5/");

            _httpClientFactory.CreateClient(Arg.Any<string>()).Returns(httpClient);

            // Act & Assert
            await Assert.ThrowsAsync<HttpRequestException>(() => _weatherService.GetWeatherAsync(city));
        }

        [Fact]
        public async Task GetWeatherAsync_WithApiError_ThrowsHttpRequestException()
        {
            // Arrange
            var city = "London";
            var currentWeatherResponse = new HttpResponseMessage(HttpStatusCode.InternalServerError);
            var forecastWeatherResponse = new HttpResponseMessage(HttpStatusCode.InternalServerError);

            var responses = new Dictionary<string, HttpResponseMessage>
            {
                { "weather?", currentWeatherResponse},
                { "forecast?", forecastWeatherResponse}
            };

            var httpClient = Substitute.For<HttpClient>(new HttpMessageHandlerStub(responses));
            httpClient.BaseAddress = new Uri("https://api.openweathermap.org/data/2.5/");

            _httpClientFactory.CreateClient(Arg.Any<string>()).Returns(httpClient);

            // Act & Assert
            await Assert.ThrowsAsync<HttpRequestException>(() => _weatherService.GetWeatherAsync(city));
        }
    }
}