from flask import Flask
from flask import render_template

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    @app.route("/")
    def display_main_page():
        return render_template("index.html")
    
    @app.route("/sport_cars")
    def display_sport_cars_list():
        return render_template("sport_cars_list.html")
    
    @app.route("/not_sport_cars")
    def display_not_sport_cars_list():
        return render_template("not_sport_cars_list.html")

    return app