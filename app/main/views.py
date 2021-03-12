from flask import render_template, request, redirect, url_for, flash
from . import main
import requests
from app import db
from ..models import City
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


@main.route('/save', methods = ['GET', 'POST'])
def save():
    
    if request.method == 'POST':
        new_city = request.form.get('city')
        new_city_obj = City(name = new_city)

        if new_city:
            db.session.add(new_city_obj)
            db.session.commit()
			
	# flash('Data saved')
    cities = City.query.order_by(City.date_posted.desc()).all()
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'


    weather_data = []

    api_key = 'a778d9642410a11ed2cbd17c20c246bc'

    for city in cities:

        r = requests.get(url.format(city.name, api_key)).json()

        weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(weather)

    
    page = request.args.get('page', type=int) 
    places = City.query.all()
    print(places)

    return render_template('save.html', weather_data = weather_data, cities = places)


@main.route('/save/delete_city/<int:city_id>', methods = ['GET', 'POST'])
def delete_city(city_id):
    if request.method == 'POST':
        cities = City.query.get_or_404(city_id)
        # if post.author != current_user:
        #     abort(403)
        if cities:
            db.session.delete(cities)
            db.session.commit()

    flash('City deleted', 'success')
    return redirect( url_for('main.save'))