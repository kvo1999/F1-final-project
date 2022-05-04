# web_app/__init__.py

from flask import Flask

from web_app.routes.avgfin_routes import avgfin_routes
from web_app.routes.home_routes import home_routes
from web_app.routes.driver_routes import driver_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(avgfin_routes)
    app.register_blueprint(home_routes)
    app.register_blueprint(driver_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)