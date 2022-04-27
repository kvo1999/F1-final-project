# web_app/routes/avgfin_routes.py

from flask import Blueprint, request, render_template

from app.all_functions import average_finish

avgfin_routes = Blueprint("avgfin_routes", __name__)

@avgfin_routes.route("/avgfinish")
def index():
    print("HOME...")
    return "Welcome Home"
    #return render_template("home.html")


