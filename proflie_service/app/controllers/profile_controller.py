from flask_restful import Resource, reqparse
from app.services.profile_service import ProfileService
from flask import jsonify

class ProfileController(Resource):
    def __init__(self):
        self.profile_service = ProfileService()

    def get(self, user_id):
        print(user_id)
        profile = self.profile_service.get_profile_by_user_id(user_id)
        print(profile.to_dict())
        return {"response":profile.to_dict()}, 200

    def post(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=str, required=True)
        parser.add_argument('user_height', type=int, required=True)
        parser.add_argument('user_weight', type=int, required=True)
        parser.add_argument('user_age', type=int, required=True)
        parser.add_argument('sex', type=str, required=True)
        data = parser.parse_args()
        print(data)
        if self.profile_service.get_profile_by_user_id(data["user_id"]):
            return {"error": "Profile already exists"},500
        if self.profile_service.create_profile(data):
            return {"msg":"Post success"},200
        return {"error": "Post failed"},500

    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('user_height', type=int, required=True)
        parser.add_argument('user_weight', type=int, required=True)
        parser.add_argument('user_age', type=int, required=True)
        parser.add_argument('sex', type=str, required=True)
        data = parser.parse_args()
        print(data)
        if self.profile_service.get_profile_by_user_id(user_id):
            if self.profile_service.update_profile(user_id, data):
                return {"msg":"Alter User success"},200
            return {"error": "Alter User failed"},500
        return {"error": "Profile does not exists"},500

    def delete(self, user_id):
        return self.profile_service.delete_profile(user_id)