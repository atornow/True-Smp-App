from flask import Blueprint, request, jsonify
from services.user_service import UserService
from utils.extensions import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta

bp = Blueprint('auth', __name__, url_prefix='/auth')
user_service = UserService()

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    existing_user = user_service.get_by_username(username)
    if existing_user:
        return jsonify({"message": "Username already exists"}), 400

    user = user_service.create_user(username, password)
    return jsonify({
        "message": "User registered successfully",
        "user_id": user.id
    }), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = user_service.get_by_username(username)
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id, expires_delta=timedelta(days=1))
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401

@bp.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    username = data.get('username')
    token = data.get('token')

    if user_service.verify_user(username, token):
        return jsonify({"message": "User verified successfully"}), 200
    else:
        return jsonify({"message": "Invalid verification token"}), 400

@bp.route('/me', methods=['GET'])
@jwt_required
def get_current_user():
    user_id = get_jwt_identity()
    user = user_service.get(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({"message": "User not found"}), 404