from flask import Blueprint
from flask import Flask, render_template, request, redirect
from repositories import user_repository
from models.user import User

# Creates a new instance of Blueprint called visits
visits_blueprint = Blueprint("visits", __name__)

@visits_blueprint.route("/visits")
def visits():
    # visits = user_repository.select_all()
    return render_template('/user.html')
