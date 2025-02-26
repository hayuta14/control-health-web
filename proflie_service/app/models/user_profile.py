
class UserProfile:
    def __init__(self, user_id, user_height, user_weight, user_age, sex, BMI, body_fat, BMR):
        self.user_id = user_id
        self.user_height = user_height
        self.user_weight = user_weight
        self.user_age = user_age
        self.sex=sex
        self.BMI=BMI
        self.body_fat=body_fat
        self.BMR=BMR

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'user_height': self.user_height,
            'user_weight': self.user_weight,
            'user_age': self.user_age,
            'sex': self.sex,
            'BMI': self.BMI,
            'body_fat': self.body_fat,
            'BMR': self.BMR
        }

    @staticmethod
    def from_dict(json):
        return UserProfile(
            user_id=json['user_id'],
            user_height=json['user_height'],
            user_weight=json['user_weight'],
            user_age=json['user_age'],
            sex=json['sex'],
            BMI=json['BMI'],
            body_fat=json['body_fat'],
            BMR=json['BMR']
        )