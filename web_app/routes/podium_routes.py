# web_app/routes/podium_routes.py

from flask import Blueprint, request, jsonify

from app.all_functions import podium_result

podium_routes = Blueprint("podium_routes", __name__)

@podium_routes.route("/podium")
def pod_f1_api():
    print("DRIVER STATS")

    url_params = dict(request.args)
    print("URL PARAMS:" , url_params)

    driver_lname = url_params.get("driver_lname") or "hamilton"  

    results = podium_result(driver_lname)

    if results:
        return jsonify(results)
    else:
        return jsonify({"message: Invalid driver ID, please try again."}), 404
