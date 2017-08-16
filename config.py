import fractions
import requests
import json
token = '314198607:AAHEH_pjSxa3jURE3IIofTk9zK8Y5-rHq2k'

api = 'ece1d9e5fc8e443e9c3c1243184cbbb3'

url = 'http://api.openweathermap.org/data/2.5/forecast'

def weather(city):
	
	params = {'q' : city, 'appid' : api, 'units' : 'metric'}
	s  = requests.get(url, params = params)
	c = s.json()['list']
	lst = []
	for a in c:
		string = a['dt_txt'] + '\n' + str(a['main']['temp_min'] ) +'°C' +  '\n' + str(a['main']['temp_max']) + '°C' +  '\n' + a['weather'][0]['description'] 
		lst.append(string)
	return lst

def gcd(a, b):
	return fractions.gcd(a, b)