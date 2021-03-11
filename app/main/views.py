from flask import render_template, request, redirect, url_for
from . import main
import requests
# from ..requests import api_key

@main.route('/', methods = ['GET', 'POST'] )
def index():

	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'

	# request.form.get('city')
	new_city = request.form.get('city')
	api_key = 'a778d9642410a11ed2cbd17c20c246bc'

	response = requests.get(url.format(new_city, api_key)).json()

	weather_data = []

	if response:
		weather = {
			'city': new_city,
			'icon': response['weather'][0]['icon'],
			'description': response['weather'][0]['description'],
			'temperature': response['main']['temp']
		}

		
		weather_data.append(weather)
		
		print(weather_data)
	return render_template('index.html', weather_data = weather_data)

@main.route('/feedback')
def feedback():	
		
		return render_template('feedback.html')

@main.route('/about')
def about():	
		
		return render_template('about.html')


