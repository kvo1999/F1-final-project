from flask import Blueprint, request, render_template
from app.all_functions import master_function

driver_routes = Blueprint("DRIVER", __name__)

@driver_routes.route("/drivers/<driver_lname>")
def plswork(driver_lname):
    results= master_function(driver_lname)
    return render_template("result_layout.html", results=results, driver_lname=driver_lname)


@driver_routes.route("/driver/form")
def index():
    print("driver form")
    #return "Welcome Home"
    return render_template("driver_form.html")
