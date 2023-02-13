from pyowm import OWM
from pyowm.utils import timestamps
from pyowm.utils import config as cfg


config = cfg.get_default_config()
config['language'] = 'ru'


owm = OWM('bb745a423261ed0bd4b416152d2b7ef7' )
mgr = owm.weather_manager()

place = input("В каком городе/стране?: ")

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]
print("В городе " + place + " сейчас " + w.detailed_status)
print("Температура сейчас в районе " + str(temp))
