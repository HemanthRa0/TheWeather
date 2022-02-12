import requests
from django.shortcuts import render
import datetime
import time
# Create your views here.

def index(request):
    city ="Hyderabad"
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=254ff59c3428476a8fb4886da28d43ea'
    if request.method == 'POST':
        data = request.POST.get('city')
        city = data
    r= requests.get(url.format(city)).json()
    if r['cod'] == '404':
        city_weather = {
        'city' : "In English Please!",
        'temperature' : '0',
        'description' : 'Not a valid input',
        'icon' : "/static/images/error.gif",
        'bgimg' : "/static/images/staticerror.jpg",
    }
        context = {'city_weather' : city_weather}
        return render(request, 'weather/weather.html', context)
    city_weather = {
        'city' : city,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : "http://openweathermap.org/img/wn/10d@2x.png",
        'bgimg' : "/static/images/autmn.jpg",
    }

    t = time.localtime()
    current_time = time.strftime("%H", t)

    if city_weather['temperature'] < 20:
        city_weather['bgimg'] = "/static/images/{}.jpg".format("snow" if int(current_time) < 18 else "coldnight")
    elif city_weather['temperature'] > 20 and city_weather['temperature'] < 27:
        city_weather['bgimg'] = "/static/images/{}.jpg".format("clear" if int(current_time) < 18 else "clearnight")
    elif city_weather['temperature'] >28:
        city_weather['bgimg'] = "/static/images/{}.jpg".format("sunny" if int(current_time) < 18 else "clearnight")

    if "cloud" in city_weather['description']:
        city_weather['icon'] = "/static/images/cloudy.gif"
    elif "mist" or "haze" in city_weather['description']:
        city_weather['icon'] = "/static/images/haze.gif"
    elif "snow" in city_weather['description']:
        city_weather['icon'] = "/static/images/snow.gif"
    elif "rain" in city_weather['description']:
        city_weather['icon'] = "/static/images/rain.gif"
    elif "thunder" or "storm" in city_weather['description']:
        city_weather['icon'] = "/static/images/thunder.gif"
    elif "wind" in city_weather['description']:
        city_weather['icon'] = "/static/images/windy.gif"
    elif "rain" in city_weather['description']:
        city_weather['icon'] = "/static/images/rain.gif"
    elif "clear" in city_weather['description']:
        city_weather['icon'] = "/static/images/clearsky.jpg"

    context = {'city_weather' : city_weather}
    return render(request, 'weather/weather.html', context)