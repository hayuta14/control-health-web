import os,requests
from flask import jsonify

def register(request):
    print(type(request))
    if not request:
        return None, ("Please type again", 401)
    response=requests.post("http://127.0.0.1:5000/auth/register",json=request)
    content=response.json()
    if response.status_code != 200:
        return None,(content["err"],response.status_code)
    return(content["err"],response.status_code),None

def alterUser(request):
    if not "Authorization" in request.headers:
        return None,("No token provided", 401)
    token = request.headers["Authorization"]
    if not token:
        return None,("Token is missing", 401)
    if not request:
        return None, ("Please type again", 401)
    data=request.get_json()
    response=requests.put("http://127.0.0.1:5000/auth/alterUser",headers={"Authorization": token},json=data)
    content=response.json()
    if response.status_code != 200:
        return None,(content["msg"],response.status_code)
    return(content["msg"],response.status_code),None

def userProfileDetail(token,UserId):
    if not token:
        return None,("Token is missing", 401)
    response=requests.get(f"http://127.0.0.1:5002/user-profile/{UserId}",headers={"Authorization": token})
    content=response.json()
    if response.status_code != 200:
        return None,(content["msg"],response.status_code)
    return(content["response"],response.status_code),None

def userProfile(token):
    if not token:
        return None,("Token is missing", 401)
    response=requests.get("http://127.0.0.1:5000/auth/userProfile",headers={"Authorization": token})
    content=response.json()
    if response.status_code != 200:
        return None,(content["msg"],response.status_code)
    return content,None

def userId(token):
    if not token:
        return None,("Token is missing", 401)
    response=requests.get("http://127.0.0.1:5000/auth/userId",headers={"Authorization": token})
    content=response.json()
    if response.status_code != 200:
        return None,(content["msg"],response.status_code)
    return content["msg"],None

