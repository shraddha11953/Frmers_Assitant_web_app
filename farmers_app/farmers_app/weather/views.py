# import requests
# from django.shortcuts import render

# def weather_home(request):
#     weather_data = None
#     city = ''
#     if request.method == 'POST':
#         city = request.POST.get('city')
#         api_key = '336b872cb8ba3108fc5bbc42202cdf68'  # Replace with your API key
#         url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
#         response = requests.get(url)
#         if response.status_code == 200:
#             weather_data = response.json()
#         else:
#             weather_data = {'error': 'City not found or API limit exceeded'}

#     return render(request, 'weather/weather.html', {
#         'weather_data': weather_data,
#         'city': city
#     })
# PythonFinalizationError
import requests
from django.shortcuts import render

def weather_home(request):
    weather_data = None
    city = ''
    rain_alert = False

    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = '336b872cb8ba3108fc5bbc42202cdf68'  # Replace with your API key
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
                description = weather_data['weather'][0]['description'].lower()
                if 'rain' in description:
                    rain_alert = True
            else:
                weather_data = {'error': 'City not found or API limit exceeded'}
        except Exception as e:
            weather_data = {'error': f'Error fetching data: {e}'}

    return render(request, 'weather/weather.html', {
        'weather_data': weather_data,
        'city': city,
        'rain_alert': rain_alert
    })
