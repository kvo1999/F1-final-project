# web_app/routes/avgfin_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash 

from app.all_functions import average_finish

avgfin_routes = Blueprint("avgfin_routes", __name__)

@avgfin_routes.route("/driver/form")
def driver_form():
    print("F1 DRIVER STAT FORM...")
    return render_template("driver_form.html")

@avgfin_routes.route("/avgfin", methods=["GET", "POST"])
def get_avg():

    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST": # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    driver_lname = request_data.get("driver_lname") or "hamilton"

    results = average_finish(driver_lname)
    if results:
        flash("Driver stats generated successfully!", "success")
        return render_template("driver_result.html", driver_lname= driver_lname, results=results)
    else:
        flash("Driver Name Error. Please try again!", "danger")
        return redirect("/home")



