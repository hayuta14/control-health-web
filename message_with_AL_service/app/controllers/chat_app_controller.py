from app.services.chat_app_service import ChatAppService
from flask_restful import Resource, reqparse

class ChatAppController(Resource):
    def __init__(self):
        self.chat_service = ChatAppService()

    def post(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=str, required=True)
        parser.add_argument('user_message', type=str, required=True)
        data = parser.parse_args()
        return {"response":self.chat_service.create_chat(data)}, 200

    def delete(self, user_id):
        return self.chat_service.delete_chat(user_id), 200
    
class ChatAppHistory(Resource):
    def __init__(self):
        self.chat_service = ChatAppService()

    def get(self,user,limit,pagination):
        return {"response":self.chat_service.get_chat_by_user_id(user,limit,pagination)}, 200