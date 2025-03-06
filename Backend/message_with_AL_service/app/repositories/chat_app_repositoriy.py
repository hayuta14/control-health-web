from app.extensions import db
from app.models.chat_app_model import ChatAppModel


class ChatAppRepository:
    def __init__(self):
        self.collection = db.db.chat_app

    def create_chat(self, data):
        chat = ChatAppModel(data["user_id"], data["user_message"], data["ai_response"], data["time_stamp"])
        self.collection.insert_one(chat.to_dict())
        return chat

    def get_chat_by_user_id(self, user_id, limit=10,pagination=1):
        skip = (pagination - 1) * limit
        chat_data = self.collection.find({"user_id": str(user_id)}).sort("time_stamp", -1).skip(skip).limit(limit)
        data= list(chat_data)
        for datas in data:
            datas["_id"] = str(datas["_id"])
            datas["time_stamp"] = str(datas["time_stamp"])
        print(data)
        if not data:
            return None
        return data

    def delete_chat(self, user_id):
        chat = self.collection.delete_one({"user_id": user_id})
        if chat.deleted_count == 0:
            return None
        return chat