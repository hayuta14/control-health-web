class ChatAppModel:
    def __init__(self,user_id,user_message,ai_response,time_stamp):
        self.user_id = user_id
        self.user_message = user_message
        self.ai_response = ai_response
        self.time_stamp = time_stamp    

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'user_message': self.user_message,
            'ai_response': self.ai_response,
            'time_stamp': self.time_stamp
        }

    @staticmethod
    def from_dict(json):
        return ChatAppModel(
            user_id=json['user_id'],
            user_message=json['user_message'],
            ai_response=json['ai_response'],
            time_stamp=json['time_stamp']
        )