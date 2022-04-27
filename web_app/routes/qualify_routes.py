# web_app/routes/qualify_routes.py

from flask import Blueprint, request, render_template

from app.all_functions import qualifying_time

qualify_routes = Blueprint("qualify_routes", __name__)

@qualify_routes.route("/qualifying")
def index():
    print("HOME...")
    return "Welcome Home"
    #return render_template("home.html")