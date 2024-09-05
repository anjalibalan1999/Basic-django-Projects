from django.shortcuts import render
import requests

def index(request):
    weather_data = None
    error_message = None
    API_KEY = 'b7956d8703134cc483c94625240509'  # Replace this with your actual Weather API key
    BASE_URL = 'http://api.weatherapi.com/v1'

    if request.method == 'POST':
        city = request.POST.get('city')

        if not city:
            error_message = "Please enter a valid city."
        else:
            request_url = f"{BASE_URL}/current.json?key={API_KEY}&q={city}&aqi=no"
            response = requests.get(request_url)

            if response.status_code == 200:
                weather_data = response.json()
            else:
                error_message = "City not found or an error occurred."

    return render(request, 'index.html', {'weather_data': weather_data, 'error_message': error_message})
