# web_app/__init__.py

from flask import Flask

from web_app.routes.avgfin_routes import avgfin_routes
from web_app.routes.DNF_routes import DNF_routes
from web_app.routes.podium_routes import podium_routes
from web_app.routes.qualify_routes import qualify_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(avgfin_routes)
    app.register_blueprint(DNF_routes)
    app.register_blueprint(podium_routes)
    app.register_blueprint(qualify_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)