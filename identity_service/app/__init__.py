from flask import Flask
from app.extensions import db, jwt
from app.routes import auth_bp
from app.config import Config
from flask_cors import CORS
from app.services.token_blacklist import is_token_blacklisted

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_in_revoked(header,decrypted_token):
        print("sadasdasdasd")
        return is_token_blacklisted(decrypted_token["jti"])
    
    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app