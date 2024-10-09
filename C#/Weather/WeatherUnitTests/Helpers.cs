using System.Net;

namespace WeatherUnitTests
{
    internal class Helpers
    {
        internal class HttpMessageHandlerStub : HttpMessageHandler
        {
            private readonly HttpResponseMessage _currentWeatherResponse;
            private readonly HttpResponseMessage _forecastWeatherResponse;

            public HttpMessageHandlerStub(HttpResponseMessage currentWeatherResponse, HttpResponseMessage forecastWeatherResponse)
            {
                _currentWeatherResponse = currentWeatherResponse;
                _forecastWeatherResponse = forecastWeatherResponse;
            }

            protected override async Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
            {
                if (request.RequestUri.ToString().Contains("weather?"))
                {
                    return await Task.FromResult(_currentWeatherResponse);
                }
                else if (request.RequestUri.ToString().Contains("forecast?"))
                {
                    return await Task.FromResult(_forecastWeatherResponse);
                }

                return new HttpResponseMessage(HttpStatusCode.NotFound);
            }
        }
    }
}