from flask import Blueprint
from flask import render_template

from repositories import user_repository, destination_repository

visits_blueprint = Blueprint("visits", __name__)

@visits_blueprint.route("/visits")
def users():
    users = user_repository.select_all()
    return render_template('visits/index.html', users=users)


@visits_blueprint.route("/visits/<id>")
def show(id):
    user = user_repository.select(id)
    destinations = destination_repository.select_all()
    return render_template('visits/show.html', user=user, destinations=destinations)
