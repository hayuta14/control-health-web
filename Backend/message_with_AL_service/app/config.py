import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    MONGO_URI = os.getenv("MONGO_URI")
    EXPIRATION_TIME = os.getenv("JWT_ACCESS_TOKEN_EXPIRES")
    PORT= os.getenv("PORT", 5000)
    AL_API_KEY = os.getenv("API_KEY")