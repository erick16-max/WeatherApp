from django.shortcuts import render
import urllib.request as requests
import json

from matplotlib.style import context

# Create your views here.

def index (request):
    if request.method == 'POST':
        city = request.POST['city']
        API_KEY = "" #enter API generetaed by the openweathermap after signied in
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
        request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
        res =requests.urlopen(request_url).read()
        data = json.loads(res)
        context  = {
            'city': data['name'],
            'country_code':data['sys']['country'],
            'latitude':data['coord']['lat'],
            'longitude':data['coord']['lon'],
            'temperature':round(data['main']['temp'] -273, 2),
            'pressure':data['main']['pressure'],
            'humidity':data['main']['humidity'],
            'weather': data['weather'][0]['description']
        }
    else:
        context = {}
            
    return render(request, 'base/index.html', context)

    
        


