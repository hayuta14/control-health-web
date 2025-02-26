import os, gridfs, pika, json
from flask import Flask, request,jsonify
from flask_pymongo import PyMongo
from app.auth import *
from app.userProfile import *
from app.chatBox import *
from flask_cors import CORS

server = Flask(__name__)
CORS(server)
#validate router
@server.route("/login", methods=["POST"])
def Login():
    token,err = login(request.get_json())
    if not err:
        return token, 200
    return err, 401

@server.route("/logout", methods=["POST"])
def Logout():
    token,err = validate(request)
    if err:
        err_res,err_code=err
        return jsonify({"err":err_res}) , err_code

    success,error=logout(token)
    if error:
        err_res,err_code=error
        print(err_res)
        return jsonify({"err":err_res}) , err_code
    success_res,success_code=success
    return jsonify({"err":success_res}) , success_code
    

#user router

@server.route("/register", methods=["POST"])
def Register():
    success,error=register(request.get_json())
    if error:
        err_res,err_code=error
        print(err_res)
        return jsonify({"err":err_res}) , err_code
    success_res,success_code=success
    return jsonify({"err":success_res}) , success_code

@server.route("/alterUser", methods=["PUT"])
def AlterUser():
    success,error=alterUser(request)
    if error:
        err_res,err_code=error
        print(err_res)
        return jsonify({"err":err_res}) , err_code
    success_res,success_code=success
    return jsonify({"err":success_res}) , success_code

@server.route("/userProfile", methods=["GET"])
def UserProfile():
    token,err = validate(request)
    if err:
        err_res,err_code=err
        return jsonify({"err":err_res}) , err_code

    UserId,error1 = userId(token)
    if error1:
        return "Sth was wrong"
    success,error=userProfileDetail(token,UserId)
    if error:
        err_res,err_code=error
        print(err_res)
        return jsonify({"err":err_res}) , err_code
    success_res,success_code=success
    userDetail,error2=userProfile(token)
    if error2:
        return"User Profile Not Find"

    userDetail1 = dict(userDetail)
    success_res["email"]=userDetail1["email"]
    success_res["username"]= userDetail1["username"]
    success_res["password_hash"]=userDetail1["password_hash"]
    del success_res["user_id"]
    return jsonify(success_res) , success_code
    

#Chat Al router
@server.route("/alResponse",methods=["POST"])
def AlResponse():
    token,err = validate(request)
    if err:
        err_res,err_code=err
        return jsonify({"err":err_res}) , err_code
    UserId,error=userId(token)
    if error:
        err_res,err_code=error
        print(err_res)
        return jsonify({"err":err_res}) , err_code
    data=request.get_json()
    data["user_id"]=UserId
    print(type(data))
    success,error=alResponse(data)
    if error:
        err_res,err_code=error
        print(err_res)
        return jsonify({"err":err_res}) , err_code
    success_res,success_code=success
    return jsonify({"response":success_res}) , success_code

@server.route("/chatHistories/<int:limit>/<int:page>",methods=["GET"])
def chatHistories(limit,page):
    token,err = validate(request)
    if err:
        err_res,err_code=err
        return jsonify({"err":err_res}) , err_code
    UserId,error=userId(token)
    if error:
        err_res,err_code=error
        print(err_res)
        return jsonify({"err":err_res}) , err_code
    success,error=getChatHistories(UserId,limit,page)
    if error:
        err_res,err_code=error
        print(err_res)
        return jsonify({"err":err_res}) , err_code
    success_res,success_code=success
    return jsonify(success_res) , success_code






if __name__ == "__main__":
    server.run(debug=True,port=3001)