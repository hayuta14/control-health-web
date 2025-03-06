from flask_jwt_extended import create_access_token,jwt_required,get_jwt,get_jwt_identity
import jwt
import uuid
from datetime import datetime, timedelta
from app.config import Config

def create_token(user):
    minutes=int(Config.EXPIRATION_TIME)
    print(user)
    token = create_access_token(identity={"username":user.username,"email":user.email}, additional_claims={"jti": str(uuid.uuid4())},expires_delta=timedelta(minutes=minutes))
    return token
