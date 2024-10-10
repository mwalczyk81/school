using System.Net;

namespace WeatherUnitTests
{
    internal class Helpers
    {
        internal class HttpMessageHandlerStub(Dictionary<string, HttpResponseMessage> responses, HttpResponseMessage? defaultResponse = null) : HttpMessageHandler
        {
            private readonly Dictionary<string, HttpResponseMessage> _responses = responses;
            private readonly HttpResponseMessage _defaultResponse = defaultResponse ?? new HttpResponseMessage(HttpStatusCode.NotFound);

            protected override async Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
            {
                if (request.RequestUri != null)
                {
                    var requestUri = request.RequestUri.ToString();
                    foreach (var response in _responses)
                    {
                        if (requestUri.Contains(response.Key))
                        {
                            return await Task.FromResult(response.Value);
                        }
                    }
                }

                return _defaultResponse;
            }
        }
    }
}