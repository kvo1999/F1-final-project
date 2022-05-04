from flask import Blueprint, request, render_template
from app.all_functions import average_finish


hamilton_routes = Blueprint("hamilton", __name__)

@hamilton_routes.route("/drivers/<driver_lname>")
def plswork(driver_lname):
    #return "Welcome Home"
    return average_finish(driver_lname)
