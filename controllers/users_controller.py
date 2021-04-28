from flask import Blueprint
from flask import render_template

from repositories import user_repository, destination_repository

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
