import os,requests
from flask import jsonify

def login(request):
    print(request)
    auth = (request["email"], request["password"])

    if not auth:
        return None, ("Please type again", 401)
    
    print(auth)
    response = requests.post("http://identity_service:5000/auth/login",json=auth)

    if response.status_code != 200:
        print(response.text)
        return None, jsonify({"err": response.text})
    else:
        print(2)
        return jsonify({"access_token": response.text}), None
    
def validate(request):
    if not "Authorization" in request.headers:
        return None,("No token provided", 401)
    token = request.headers["Authorization"]
    if not token:
        return None,("Token is missing", 401)
    response = requests.post("http://identity_service:5000/auth/validate", headers={"Authorization": token})
    content=response.json()
    print(response.json())
    if response.status_code != 200:
        return None,("Token is invalid", 401)
    else:
        return token,None
    
def logout(token):
    response = requests.post("http://identity_service:5000/auth/logout",headers={"Authorization": token})
    print(response)
    content=response.json()
    if response.status_code != 200:
        return None,(content["msg"],response.status_code)
    return (content["message"],response.status_code),None