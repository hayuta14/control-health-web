from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
import google.generativeai as genai
from app.config import Config

db = PyMongo()
jwt = JWTManager()
genai.configure(api_key=str(Config.AL_API_KEY))