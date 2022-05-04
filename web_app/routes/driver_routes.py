from flask import Blueprint, request, render_template
from app.MASTER_FUNCTION import driver_results

driver_routes = Blueprint("DRIVER", __name__)

@driver_routes.route("/drivers/<driver_lname>")
def plswork(driver_lname):
    return driver_results(driver_lname)
