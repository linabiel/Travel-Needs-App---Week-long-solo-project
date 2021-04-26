from flask import Blueprint
from flask import Flask, render_template, request, redirect
from repositories import user_repository, city_repository, country_repository, destination_repository
from models.user import User
from models.city import City
from models.country import Country
from models.destination import Destination

# Creates a new instance of Blueprint called destination
destinations_blueprint = Blueprint("destinations", __name__)

# NEW
# GET '/destinations'
# Returns an html form to the browser at the /destinations
@destinations_blueprint.route("/destinations")
def destinations():
    users = user_repository.select_all()
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    destinations = destination_repository.select_all()
    return render_template('destinations/index.html', users=users, countries=countries, cities=cities, destinations=destinations)

# CREATE
# POST '/destinations'
# Recieves the data that we sent from the form to insert into the database
@destinations_blueprint.route('/destinations', methods=['POST'])
def add_destination():
    user_id = request.form['user']
    country_name = request.form['country']
    city_name = request.form['city']

    # For drop down menu
    user = user_repository.select(user_id)
    # country = country_repository.select(country_id)
    # country_repository.save(country)
    # city = city_repository.select(city_id)
    # city_repository.save(city)

    new_country = Country(country_name)
    country_id = country_repository.save(new_country)


    new_city = City(city_name, country_id)
    city_id = city_repository.save(new_city)

    new_destination = Destination(user, country_id, city_id)
    destination_repository.save(new_destination)
    return redirect('/destinations')

# EDIT 
@destinations_blueprint.route('/destinations/<id>/edit')
def edit_destination(id):
    destination = destination_repository.select(id)
    return render_template('destinations/edit.html', user=destination.user, country=destination.country, city=destination.city, destination=destination)

# UPDATE
@destinations_blueprint.route('/destinations/<id>', methods=['POST'])
def update_destination_get(id):
    visited = request.form['visited']
    destination = destination_repository.select(id)
    destination.visited = visited
    destination_repository.update(destination)
    return redirect('/destinations')