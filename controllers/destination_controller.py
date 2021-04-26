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
def select_destination():
    user_id = request.form['user']
    country_id = request.form['country']
    city_id = request.form['city']

    user = user_repository.select(user_id)
    country = country_repository.select(country_id)
    city = city_repository.select(city_id)
    destination = Destination(user, country, city)
    destination_repository.save(destination)
    return redirect('/destinations')


@destinations_blueprint.route('/destinations/add')
def add_destination_get():
    return render_template('destinations/add.html')

@destinations_blueprint.route('/destinations/add', methods=['POST'])
def add_destination():
    country_name = request.form['country']
    city_name = request.form['city']

    country = Country(country_name)
    country = country_repository.save(country)

    new_city = City(city_name, country)
    city_repository.save(new_city)
    return render_template('destinations/add.html')

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

# DELETE
@destinations_blueprint.route('/destinations/<id>/delete')
def delete_task_get(id):
    destination_repository.delete(id)
    return redirect('/destinations')

@destinations_blueprint.route('/destinations/<id>/delete', methods=['POST'])
def delete_task(id):
    destination_repository.delete(id)
    return redirect('/destinations')