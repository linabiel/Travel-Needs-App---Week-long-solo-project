from flask import Blueprint
from flask import Flask, render_template, request, redirect
from repositories import user_repository, city_repository, country_repository
from models.user import User
from models.city import City
from models.country import Country

# Creates a new instance of Blueprint called destination
destinations_blueprint = Blueprint("destinations", __name__)

@destinations_blueprint.route("/destinations")
def destinations():
    users = user_repository.select_all()
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    return render_template('/destinations.html', users=users, countries=countries, cities=cities)
