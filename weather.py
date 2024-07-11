import pyowm
from config import *

#функция что бы узнать температуру
def temperature_w(city):
	owm = pyowm.OWM(API_KEY)
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(city)
	w = observation.weather
	temp = w.temperature('celsius')['temp']

	return "В городе " + city + " сейчас " + str(temp) + " градусов"
