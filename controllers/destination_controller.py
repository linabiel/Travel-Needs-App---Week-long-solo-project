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
    return render_template('/destinations.html')
