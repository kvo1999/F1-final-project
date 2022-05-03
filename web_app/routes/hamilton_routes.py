from flask import Blueprint, request, render_template

hamilton_routes = Blueprint("hamilton", __name__)

@hamilton_routes.route("/drivers/<driver_lname>")
def plswork(driver_lname):
    #return "Welcome Home"
    return driver_lname
