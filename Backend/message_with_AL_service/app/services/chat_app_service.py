from app.repositories.chat_app_repositoriy import ChatAppRepository
import google.generativeai as genai
import datetime

class ChatAppService:
    def __init__(self):
        self.repository = ChatAppRepository()
        self.model= genai.GenerativeModel("gemini-pro")

    def create_chat(self, data):
        response = self.model.generate_content(data["user_message"]+" trả lời ngắn gọn tối đa là 200 từ và không có xuống dòng")
        ai_response = response.text
        data["ai_response"] = ai_response
        data["time_stamp"] = datetime.datetime.now()
        if self.repository.create_chat(data):
            return ai_response
        return "Something went wrong"

    def get_chat_by_user_id(self, user_id=123, limit=10, pagination=1):
        return self.repository.get_chat_by_user_id(user_id, limit, pagination)

    def delete_chat(self, user_id):
        return self.repository.delete_chat(user_id)