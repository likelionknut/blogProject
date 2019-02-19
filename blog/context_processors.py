from pyowm import OWM

def get_weather(request):
    owm = OWM(API_key='f74e57b358712ff9b0bae5f6d02ec271')
    obs = owm.weather_at_place('Seoul')
    obs = owm.weather_at_id(1835848)
    obs = owm.weather_at_coords(37.5667, 126.9783)
    
    w = obs.get_weather()
    wStatus = w.get_status()
    
    return {'weather' : wStatus}