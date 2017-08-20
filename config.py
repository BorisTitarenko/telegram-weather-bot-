
import requests
import json
token = input('you token')

api = input('your api key')

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

