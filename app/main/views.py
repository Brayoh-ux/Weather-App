from flask import render_template, request, redirect, url_for
from . import main

@main.route('/')
def index():

    return render_template('index.html')

@main.route('/feedback')
def feedback():	
		
		return render_template('feedback.html')

@main.route('/about')
def about():	
		
		return render_template('about.html')
