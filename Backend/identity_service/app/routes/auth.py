from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, get_jwt
)
from app.services.user_service import create_user, authenticate_user, get_user_id_by_email, updateInformation, get_user_by_email
from app.services.token_blacklist import add_token_to_blacklist, is_token_blacklisted
from app.utils.jwt_helper import create_token


auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    response,err_code = create_user(data)
    if err_code != 200:
        return jsonify({"err": response}) , 500
    return jsonify({"err": response}), 200

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    response,err_code = authenticate_user(data)
    if err_code == 200:
        token = create_token(response)
        return token, 200
    return response, 401

@auth_bp.route("/validate", methods=["POST"])
def validate():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Token is missing"}), 401
    if is_token_blacklisted(token):
        return jsonify({"error": "Token is invalid"}), 401
    
    return jsonify({"message": "Token is valid"}), 200

@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    jwt=get_jwt()["jti"]
    status = add_token_to_blacklist(jwt)
    if status:
        return jsonify({"message": "User logged out successfully"}), 200
    return jsonify({"error": "Something went wrong"}), 500

# Route được bảo vệ bằng JWT
@auth_bp.route("/userProfile", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    user=get_user_by_email(current_user.get("email"))
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

@auth_bp.route("/alterUser", methods=["PUT"])
@jwt_required()
def alter_user():
    data = request.get_json()
    current_user = get_jwt_identity()
    user_id = get_user_id_by_email(current_user.get("email"))
    print(user_id)
    if not user_id:
        return jsonify({"error": "User not found"}), 404
    response,err_code = updateInformation(current_user.get("email"),data,user_id)
    return jsonify({"msg":response}), err_code

@auth_bp.route("/userId",methods=["GET"])
@jwt_required()
def user_id():
    current_user = get_jwt_identity()
    user_id = get_user_id_by_email(current_user.get("email"))
    return jsonify({"msg":str(user_id)}), 200




