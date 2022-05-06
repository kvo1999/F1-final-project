from flask import Blueprint, request, render_template
from app.all_functions import master_function
from app.processed_results import processed_data
from app.all_functions import driverinfolist
from app.processed_results import driverinfolist


driver_routes = Blueprint("DRIVER", __name__)


#this route runs all the functions in the web app, pulls data from API which takes a long time 

@driver_routes.route("/drivers/<driver_lname>")
def plswork(driver_lname):
    print("driver results...")
    results= master_function(driver_lname)
    driver=driverinfolist(driver_lname)
    return render_template("result_layout.html", results=results, driver_lname=driver_lname, driver=driver)


@driver_routes.route("/driver/form")
def index():
    print("driver form...")
    #return "Welcome Home"
    return render_template("driver_form.html")

#to load from CSV
#@driver_routes.route("/drivers/<driver_lname>")
#def altroute(driver_lname):
    #print("driver results...")
    #results = processed_data(driver_lname)
    #driver=driverinfolist(driver_lname)
    #return render_template("resultcsv_layout.html", results=results, driver_lname=driver_lname, driver=driver)


