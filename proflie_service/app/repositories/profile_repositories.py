from app.extensions import db
from app.models.user_profile import UserProfile

class ProfileRepository:
    def __init__(self):
        self.collection = db.db.user_profiles

    def create_profile(self, data):
        profile = UserProfile(data["user_id"], data["user_height"], data["user_weight"], data["user_age"],data["sex"],data["BMI"],data["body_fat"],data["BMR"])
        self.collection.insert_one(profile.to_dict())
        print(type(profile.to_dict()))
        return profile

    def get_profile_by_user_id(self, user_id):
        profile_data = self.collection.find_one({"user_id": str(user_id)})
        if not profile_data:
            return None
        profile = UserProfile.from_dict(profile_data)

        return profile

    def update_profile(self, user_id, data):
        profile = self.collection.update_one({"user_id": str(user_id)}, {"$set": {
            "user_height": data["user_height"],
            "user_weight": data["user_weight"],
            "user_age": data["user_age"],
            "sex": data["sex"],
            "BMI": data["BMI"],
            "body_fat": data["body_fat"],
            "BMR": data["BMR"]
        }})
        print(profile)
        if profile.matched_count == 0 and profile.modified_count == 0:
            return None
        return profile

    def delete_profile(self, user_id):
        profile = self.collection.delete_one({"user_id": user_id})
        if profile.deleted_count == 0:
            return None
        return profile