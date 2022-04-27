# web_app/routes/podium_routes.py

from flask import Blueprint, request, render_template

#from app.all_functions import ...

podium_routes = Blueprint("podium_routes", __name__)

@podium_routes.route("/podium")
def index():
    print("HOME...")
    return "Welcome Home"
    #return render_template("home.html")