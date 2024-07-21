from django.shortcuts import render
from .forms import CityForm
from .utils import get_weather_forecast

def weather_view(request):
    forecast = None
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            forecast = get_weather_forecast(city)
    else:
        form = CityForm()
    return render(request, 'weather/weather.html', {'form': form, 'forecast': forecast})

