from flask import Flask
from app.controllers.web.task_controller import task_bp


def create_app():
    app = Flask(__name__)

    # Blueprints
    app.register_blueprint(task_bp)

    return app
