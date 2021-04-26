from flask import Blueprint
from flask import Flask, render_template, request, redirect
from repositories import user_repository, city_repository, country_repository, destination_repository
from models.user import User
from models.city import City
from models.country import Country
from models.destination import Destination

# Creates a new instance of Blueprint called users
users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    return render_template('users/index.html', users=users)


@users_blueprint.route("/users/<id>")
def show(id):
    user = user_repository.select(id)
    destinations = destination_repository.select_all()
    return render_template("users/show.html", user=user, destinations=destinations)
