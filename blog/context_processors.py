from pyowm import OWM
from django.contrib.auth.models import User # 유저에 대한 기능
from django.contrib import auth # 계정에 대한 권한

def get_weather(request):    
    
    username = auth.get_user(request)

    if username.is_anonymous:
        username = 'Guest'    

    owm = OWM(API_key='f74e57b358712ff9b0bae5f6d02ec271')
    obs = owm.weather_at_place('Seoul')
    obs = owm.weather_at_id(1835848)
    obs = owm.weather_at_coords(37.5667, 126.9783)
    
    w = obs.get_weather()
    wStatus = w.get_status()
    
    return {'weather' : wStatus, 'username':username}