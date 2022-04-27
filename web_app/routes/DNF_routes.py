# web_app/routes/DNF_routes.py

from flask import Blueprint, request, jsonify

from app.all_functions import reason_DNF

DNF_routes = Blueprint("DNF_routes", __name__)

@DNF_routes.route("/DNF")
def dnf_f1_api():
    print("DRIVER STATS")

    url_params = dict(request.args)
    print("URL PARAMS:" , url_params)

    driver_lname = url_params.get("driver_lname") or "hamilton"  

    results = reason_DNF(driver_lname)

    if results:
        return jsonify(results)
    else:
        return jsonify({"message: Invalid driver ID, please try again."}), 404
