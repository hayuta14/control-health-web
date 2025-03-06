import os,requests
from flask import jsonify

def alResponse(request):
    if not request:
        return None, ("Please type again", 401)
    response=requests.post("http://message_with_ai_service:5001/chat_ai/1",json=request)
    print(response.text)
    content=response.json()
    if response.status_code != 200:
        return None,(content,response.status_code)
    return(content["response"],response.status_code),None
def getChatHistories(user_id,limit,page):
    response=requests.get(f"http://message_with_ai_service:5001/chat_ai/{user_id}/{limit}/{page}")
    print(response.text)
    content=response.json()
    if response.status_code != 200:
        return None,(content,response.status_code)
    return(content["response"],response.status_code),None
