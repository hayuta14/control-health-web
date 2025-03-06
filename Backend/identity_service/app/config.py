import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
    MONGO_URI = os.getenv("MONGO_URI")
    EXPIRATION_TIME = os.getenv("JWT_ACCESS_TOKEN_EXPIRES")
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]
    PORT= os.getenv("PORT", 5000)
