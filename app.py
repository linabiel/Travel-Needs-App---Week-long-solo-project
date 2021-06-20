from flask import Flask, render_template, request

from controllers.visits_controller import visits_blueprint
from controllers.destinations_controller import destinations_blueprint
from controllers.users_controller import users_blueprint

app = Flask(__name__)

app.register_blueprint(visits_blueprint)
app.register_blueprint(destinations_blueprint)
app.register_blueprint(users_blueprint)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
