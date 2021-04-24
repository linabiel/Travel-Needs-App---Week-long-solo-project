from flask import Blueprint
from flask import Flask, render_template, request, redirect
from repositories import user_repository
from models.user import User

# Creates a new instance of Blueprint called users
users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/user")
def users():
    users = user_repository.select_all()
    return render_template('index.html', users=users)
