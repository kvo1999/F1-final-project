from flask import Blueprint, request, jsonify

from app.all_functions import avg_pitstop_time

pitstop_routes = Blueprint("pitstop_routes", __name__)

@pitstop_routes.route("/pitstop")
def pit_f1_api():
    print("DRIVER STATS")

    url_params = dict(request.args)
    print("URL PARAMS:" , url_params)

    driver_lname = url_params.get("driver_lname") or "hamilton"  

    results = avg_pitstop_time(driver_lname)

    if results:
        return jsonify(results)
    else:
        return jsonify({"message: Invalid driver ID, please try again."}), 404