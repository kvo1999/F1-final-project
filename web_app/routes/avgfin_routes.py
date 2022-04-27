# web_app/routes/avgfin_routes.py

from flask import Blueprint, request, jsonify

from app.all_functions import average_finish

avgfin_routes = Blueprint("avgfin_routes", __name__)

@avgfin_routes.route("/avgfinish.json")
def avg_f1_api():
    print("DRIVER STATS")

    url_params = dict(request.args)
    print("URL PARAMS:" , url_params)

    driver_lname = url_params.get("driver_lname") or "hamilton"  

    results = average_finish(driver_lname)

    if results:
        return jsonify(results)
    else:
        return jsonify({"message: Invalid driver ID, please try again."}), 404




