# web_app/routes/qualify_routes.py

from flask import Blueprint, request, jsonify

from app.all_functions import qualifying_time

qualify_routes = Blueprint("qualify_routes", __name__)

@qualify_routes.route("/qualifying")
def avg_f1_api():
    print("DRIVER STATS")

    url_params = dict(request.args)
    print("URL PARAMS:" , url_params)

    circuit = url_params.get("circuit") or "bahrain"  

    results = qualifying_time(circuit)

    if results:
        return jsonify(results)
    else:
        return jsonify({"message: Invalid driver ID, please try again."}), 404
