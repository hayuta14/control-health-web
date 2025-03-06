from app.extensions import db
from datetime import datetime

def add_token_to_blacklist(encoded_token):
    db.db.blacklist.insert_one({"token": encoded_token,"expired_at": datetime.now(),"reason": "logout"})
    return True

def is_token_blacklisted(encoded_token):
    token = db.db.blacklist.find_one({"token": encoded_token})
    print(token)
    return token is not None