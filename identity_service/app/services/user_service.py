from app.extensions import db
from app.models.user import User
from werkzeug.security import generate_password_hash
import requests
from flask import jsonify
def create_user(data):
    existing_user = db.db.users.find_one({"email": data["email"]})
    if existing_user:
        return "User already exits", 409
    data["password"] = generate_password_hash(data["password"])
    user = User(data["username"], data["email"], data["password"])
    if db.db.users.insert_one(user.to_dict()):
        user = db.db.users.find_one({"email": data["email"]})
        print(user["_id"])
        user_id = user["_id"]
        data["user_id"] = str(user_id)
        response=requests.post("http://127.0.0.1:5002/user-profile/1",json=data)
        print(response)
        if response.status_code != 200:
            print(response.text)
            return response["message"], 500
        return "User created successfully", 200
    return "User created failed", 500

def authenticate_user(dataOfUser):
    print(dataOfUser)
    
    if isinstance(dataOfUser,dict):
       data = list(dataOfUser.values())
       print("1")
    elif isinstance(dataOfUser,list):
        data = dataOfUser
    else:
        return "Type of data is incorrect",404
    print(data)
    print(type(data))
    user_data = db.db.users.find_one({"email": data[0]})
    if not user_data:
        print("User not found")
        return "User not found", 404
    user = User(user_data["username"], user_data["email"], user_data["password_hash"])
    print(user_data["password_hash"])
    if user.check_password(data[1]):
        return user,200
    return "password is incorrect", 401

def get_user_id_by_email(email):
    user_data = db.db.users.find_one({"email": email})
    if not user_data:
        return None
    print(user_data["_id"])
    return user_data["_id"]

def updateInformation(email,data,user_id):
    user = db.db.users.update_one({"email": email},{"$set": {
        "username": data["username"],
        "password_hash": generate_password_hash(data["password"])
    }})
    if user.modified_count != 0:
        response=requests.put(f"http://127.0.0.1:5002/user-profile/{user_id}", json=data)
        if response.status_code != 200:
            return response.text, 500
        return "Alter User Success", 200
    
    return "User updated failed", 200

def get_user_by_email(email):
    user_data = db.db.users.find_one({"email": email})
    if not user_data:
        return None
    user = User(user_data["username"], user_data["email"], user_data["password_hash"])
    response = requests.get(f"http://127.0.0.1:5002/user-profile/{user_data['_id']}")
    user_profile = response.json()
    user=user.to_dict()
    user["height"] = user_profile["response"]["user_height"]
    user["weight"] = user_profile["response"]["user_weight"]
    user["age"] = user_profile["response"]["user_age"]
    user["sex"] = user_profile["response"]["sex"]
    print(user_profile["response"])
    if response.status_code != 200:
        return response.text, 500
    
    return user