from flask import Blueprint, request, jsonify

from app.all_functions import to_seconds

seconds_routes = Blueprint("seconds_routes", __name__)

@seconds_routes.route("/seconds")
def sec_f1_api():
    print("DRIVER STATS")

    url_params = dict(request.args)
    print("URL PARAMS:" , url_params)

    driver_lname = url_params.get("driver_lname") or "hamilton"  

    results = to_seconds(driver_lname)

    if results:
        return jsonify(results)
    else:
        return jsonify({"message: Invalid driver ID, please try again."}), 404