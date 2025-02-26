from flask import Flask
from app.extensions import db, jwt
from app.config import Config
from flask_restful import Api
from flask_cors import CORS
from app.controllers.profile_controller import ProfileController


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    api = Api(app)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    api.add_resource(ProfileController, '/user-profile/<string:user_id>')


    return app