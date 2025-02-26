from flask import Flask
from app.extensions import db
from app.config import Config
from flask_restful import Api
from flask_cors import CORS
from app.controllers.chat_app_controller import ChatAppController,ChatAppHistory


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    api = Api(app)

    # Initialize extensions
    db.init_app(app)


    api.add_resource(ChatAppController, '/chat_ai/<string:user_id>')
    api.add_resource(ChatAppHistory, '/chat_ai/<string:user>/<int:limit>/<int:pagination>')


    return app