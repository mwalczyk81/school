namespace WeatherUnitTests.Services
{
    using FluentAssertions;
    using NSubstitute;
    using NSubstitute.ExceptionExtensions;
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
            var result = await _weatherService.GetWeatherAsync(lat, lon);

            // Assert
            result.Should().NotBeNull();
            result!.WeatherData?.Name.Should().Be("London");
            result.DailyForecasts.Should().NotBeNull().And.HaveCount(1);
        }

        [Fact]
        public async Task GetWeatherAsync_WithNullLatitude_ThrowsArgumentNullExceptionAsync()
        {
            // Arrange
            double? lat = null;
            double? lon = -0.1278;

            // Act & Assert
            Func<Task> action = async () => await _weatherService.GetWeatherAsync(lat, lon);
            await action.Should().ThrowAsync<ArgumentNullException>();
        }

        [Fact]
        public void GetWeatherAsync_WithNullLongitude_ThrowsArgumentNullException()
        {
            // Arrange
            double? lat = 51.5074;
            double? lon = null;

            // Act & Assert
            Action action = async () => await _weatherService.GetWeatherAsync(lat, lon);
            action.Should().Throws<ArgumentNullException>();
        }

        [Fact]
        public async Task GetWeatherAsync_WithEmptyForecastData_ReturnsNull()
        {
            // Arrange
            var lat = 51.5074;
            var lon = -0.1278;
            var currentWeatherJson = "{\"main\": {\"temp\": 280.32}, \"weather\": [{\"icon\": \"10d\"}], \"name\": \"London\"}";
            var forecastWeatherJson = "{\"city\": {\"timezone\": 0}, \"list\": []}";

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
            var result = await _weatherService.GetWeatherAsync(lat, lon);

            // Assert
            result?.WeatherData.Should().NotBeNull();
            result?.DailyForecasts.Should().BeEmpty();
        }

        [Fact]
        public async Task GetWeatherAsync_WithEmptyCurrentWeatherData_ReturnsNull()
        {
            // Arrange
            var lat = 51.5074;
            var lon = -0.1278;
            var currentWeatherJson = "{}";
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
            var result = await _weatherService.GetWeatherAsync(lat, lon);

            // Assert
            result?.WeatherData?.Weather.Should().BeNullOrEmpty();
            result?.DailyForecasts.Should().NotBeNull();
        }

        [Fact]
        public async Task GetWeatherAsync_WithHttpRequestFailure_ThrowsHttpRequestExceptionAsync()
        {
            // Arrange
            var lat = 51.5074;
            var lon = -0.1278;
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
            Func<Task> action = async () => await _weatherService.GetWeatherAsync(lat, lon);
            await action.Should().ThrowAsync<HttpRequestException>();
        }
    }
}