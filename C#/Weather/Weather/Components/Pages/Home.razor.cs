using ApexCharts;
using Microsoft.AspNetCore.Components;
using Microsoft.JSInterop;
using MudBlazor;
using Weather.Models;
using Weather.Models.Location;
using Weather.Models.Weather;
using Weather.Services;

namespace Weather.Components.Pages
{
    public partial class Home
    {
        [Inject] private IWeatherService WeatherService { get; set; } = default!;
        [Inject] private ICitySuggestionService CitySuggestionService { get; set; } = default!;
        [Inject] private IJSRuntime JSRuntime { get; set; } = default!;
        [Inject] private ISnackbar Snackbar { get; set; } = default!;
        [Inject] private IDialogService DialogService { get; set; } = default!;

        public CitySuggestion? SelectedCity { get; set; }
        internal WeatherDataModel _weatherData = new();

        private List<ChartModel>? LowTemps { get; set; }
        private List<ChartModel>? HighTemps { get; set; }
        private ApexChartOptions<ChartModel>? ChartOptions { get; set; }

        protected override void OnInitialized()
        {
            ConfigureChartOptions();
        }

        private void OpenWeatherDetail(string dayName, IEnumerable<ForecastItem> hourlyDetails)
        {
            var options = new DialogOptions { CloseOnEscapeKey = true };
            DialogService.Show<WeatherDetail>(null, new DialogParameters
            {
                { "DayName", dayName },
                { "HourlyDetails", hourlyDetails }
            }, options);
        }

        private void ClearSelectedCity()
        {
            SelectedCity = null;
        }

        private void OnInputTextChanged(string input)
        {
            if (string.IsNullOrWhiteSpace(input))
            {
                SelectedCity = null;
            }
        }

        public async Task<IEnumerable<CitySuggestion?>>? SearchCitySuggestions(string value, CancellationToken cancellationToken)
        {
            if (string.IsNullOrWhiteSpace(value))
            {
                SelectedCity = null;
                return [];
            }

            return await CitySuggestionService.GetCitySuggestionsAsync(value, cancellationToken);
        }

        public async Task GetWeatherAsync()
        {
            if (SelectedCity == null || string.IsNullOrEmpty(SelectedCity.Lat) || string.IsNullOrEmpty(SelectedCity.Lng))
            {
                DisplayError("Please select a valid city.");
                return;
            }

            await FetchWeatherData(() => WeatherService.GetWeatherAsync(double.Parse(SelectedCity.Lat), double.Parse(SelectedCity.Lng)));
        }

        public async Task GetWeatherByLocationAsync()
        {
            try
            {
                var location = await JSRuntime.InvokeAsync<LocationItem>("getUserLocation");

                if (location?.Latitude == null || location?.Longitude == null)
                {
                    DisplayError("Failed to retrieve location.");
                    return;
                }

                await FetchWeatherData(() => WeatherService.GetWeatherAsync(location.Latitude.Value, location.Longitude.Value));
            }
            catch (Exception ex)
            {
                DisplayError($"There was a problem retrieving your location. {ex.Message}");
            }
        }

        private async Task FetchWeatherData(Func<Task<WeatherResponse?>> fetchWeatherTask)
        {
            _weatherData.IsLoading = true;

            try
            {
                _weatherData.WeatherResponse = await fetchWeatherTask();

                if (_weatherData.WeatherResponse == null)
                {
                    DisplayError("No weather data available.");
                    return;
                }

                await Task.Run(() =>
                {
                    HighTemps = GetHighTempData();
                    LowTemps = GetLowTempData();
                });

                ResetExpandedDay();
            }
            catch (Exception ex)
            {
                DisplayError($"An error occurred: {ex.Message}");
            }
            finally
            {
                _weatherData.IsLoading = false;

                await InvokeAsync(StateHasChanged);
            }
        }

        private void ConfigureChartOptions()
        {
            ChartOptions = new ApexChartOptions<ChartModel>
            {
                Yaxis =
                [
                    new YAxis
                    {
                        Labels = new YAxisLabels
                        {
                            Formatter = Constants.ApexCharts.TempFormatter
                        }
                    }
                ],
                Tooltip = new Tooltip
                {
                    Enabled = true,
                    Theme = Mode.Dark,
                    CssClass = "custom-tooltip",
                    FollowCursor = true,
                    FillSeriesColor = true,
                    Style = new TooltipStyle
                    {
                        FontSize = "14px",
                        FontFamily = "Arial"
                    },
                }
            };
        }

        private List<ChartModel> GetTempData(Func<DailyForecast, double?> selector)
        {
            return _weatherData.WeatherResponse?.DailyForecasts?.Values
                .Where(forecast => forecast.Details != null && forecast.Details.Count != 0 && selector(forecast).HasValue)
                .Select(forecast => new ChartModel
                {
                    Date = DateOnly.FromDateTime(DateTime.Parse(forecast.Details?[0].Dt_Txt ?? "")),
                    Temperature = Math.Round(selector(forecast).GetValueOrDefault())
                }).ToList() ?? [];
        }

        private void DisplayError(string message)
        {
            _weatherData.ErrorMessage = message;
            Snackbar.Add(message, Severity.Error);
        }

        private List<ChartModel> GetHighTempData() => GetTempData(forecast => forecast.High);

        private List<ChartModel> GetLowTempData() => GetTempData(forecast => forecast.Low);

        private static string GetIconUrl(string icon) => $"{Constants.Weather.WeatherIconBaseUrl}{icon}.png";

        private void ResetExpandedDay() => _weatherData.ExpandedDay = "";

        private bool CanFetchWeather() => SelectedCity != null && !_weatherData.IsLoading;
    }
}