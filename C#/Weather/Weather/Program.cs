using MudBlazor;
using MudBlazor.Services;
using Polly;
using Polly.Extensions.Http;
using System.Text.Json;
using Weather.Components;
using Weather.Services;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddRazorComponents()
    .AddInteractiveServerComponents();

builder.Services.AddHttpClient<IWeatherService, WeatherService>("Weather", client =>
{
    client.Timeout = TimeSpan.FromSeconds(10);
    client.BaseAddress = new Uri("https://api.openweathermap.org/data/2.5/");
}).AddResilienceHandler("RetryPipline", (p, c) => GetRetryPolicy());

builder.Services.AddHttpClient<ICitySuggestionService, CitySuggestionService>("Cities", client =>
{
    client.Timeout = TimeSpan.FromSeconds(10);
    client.BaseAddress = new Uri("http://api.geonames.org/searchJSON");
}).AddResilienceHandler("RetryPipline", (p, c) => GetRetryPolicy());

builder.Services.AddSingleton(new JsonSerializerOptions
{
    PropertyNameCaseInsensitive = true
});

builder.Services.AddScoped<IWeatherService, WeatherService>();
builder.Services.AddScoped<ICitySuggestionService, CitySuggestionService>();
builder.Services.AddMudServices(config =>
{
    config.SnackbarConfiguration.PositionClass = Defaults.Classes.Position.BottomCenter;
    config.SnackbarConfiguration.PreventDuplicates = true;
    config.SnackbarConfiguration.NewestOnTop = false;
    config.SnackbarConfiguration.ShowCloseIcon = true;
    config.SnackbarConfiguration.VisibleStateDuration = 5000;
    config.SnackbarConfiguration.HideTransitionDuration = 500;
    config.SnackbarConfiguration.ShowTransitionDuration = 500;
    config.SnackbarConfiguration.SnackbarVariant = Variant.Filled;
});

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error", createScopeForErrors: true);
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();

app.UseStaticFiles();
app.UseAntiforgery();

app.MapRazorComponents<App>()
    .AddInteractiveServerRenderMode();

app.Run();

static IAsyncPolicy<HttpResponseMessage> GetRetryPolicy()
{
    return HttpPolicyExtensions
        .HandleTransientHttpError()
        .WaitAndRetryAsync(3, retryAttempt => TimeSpan.FromSeconds(Math.Pow(2, retryAttempt)));
}