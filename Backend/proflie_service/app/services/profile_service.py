from app.repositories.profile_repositories import ProfileRepository
from app.models.user_profile import UserProfile

class ProfileService:
    def __init__(self):
        self.profile_repository = ProfileRepository()

    def create_profile(self, data):
        print(data)
        print(type(data))
        height = data["user_height"]
        weight = data["user_weight"]
        age = data["user_age"]
        sex = data["sex"]
        BMI = self.BMI_caculate(height, weight)
        body_fat = self.Body_fat_caculate(BMI,age,sex)
        BMR = self.BMR_caculate(weight,height,age,sex)
        data["BMI"] = BMI
        data["body_fat"] = body_fat
        data["BMR"] = BMR
        print(data)
        return self.profile_repository.create_profile(data)

    def get_profile_by_user_id(self, user_id):
        return self.profile_repository.get_profile_by_user_id(user_id)

    def update_profile(self, user_id, data):
        print(data)
        print(type(data))
        height = data["user_height"]
        weight = data["user_weight"]
        age = data["user_age"]
        sex = data["sex"]
        BMI = self.BMI_caculate(height, weight)
        body_fat = self.Body_fat_caculate(BMI,age,sex)
        BMR = self.BMR_caculate(weight,height,age,sex)
        data["BMI"] = BMI
        data["body_fat"] = body_fat
        data["BMR"] = BMR
        print(data)
        return self.profile_repository.update_profile(user_id, data)

    def delete_profile(self, user_id):
        return self.profile_repository.delete_profile(user_id)
    
    def BMI_caculate(self, height, weight):
        return round(weight/(height/100*height/100),1)
    
    def Body_fat_caculate(self,BMI,age,sex):
        if sex == "male":
            return round(1.2*BMI+0.23*age-16.2,2)
        else:   
            return round(1.2*BMI+0.23*age-5.4,2)
    
    def BMR_caculate(self,weight,height,age,sex):
        if sex == "male":
            return round(88.362+13.397*weight+4.799*height-5.677*age,2)
        return round(447.593+9.247*weight+3.098*height-4.330*age,2)
