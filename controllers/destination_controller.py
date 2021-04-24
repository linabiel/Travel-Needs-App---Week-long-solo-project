from flask import Blueprint
from flask import Flask, render_template, request, redirect
from repositories import user_repository, city_repository, country_repository, destination_repository
from models.user import User
from models.city import City
from models.country import Country
from models.destination import Destination

# Creates a new instance of Blueprint called destination
destinations_blueprint = Blueprint("destinations", __name__)

@destinations_blueprint.route("/destinations")
def destinations():
    users = user_repository.select_all()
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    return render_template('/destinations.html', users=users, countries=countries, cities=cities)

@destinations_blueprint.route('/destinations', methods=['POST'])
def add_destination():
    user_id = request.form['user_id']
    country_id = request.form['country_id']
    city_id = request.form['city_id']

    user = user_repository.select(user_id)
    country = country_repository.select(country_id)
    city = city_repository.select(city_id)

    destination = Destination(user, country, city)
    destination_repository.save(destination)
    return render_template('/destinations.html', destination=destination)