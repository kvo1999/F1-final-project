# web_app/routes/DNF_routes.py

from flask import Blueprint, request, render_template

from app.all_functions import reason_DNF

DNF_routes = Blueprint("DNF_routes", __name__)

@DNF_routes.route("/DNF")
def index():
    print("HOME...")
    return "Welcome Home"
    #return render_template("home.html")