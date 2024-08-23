from flask import Blueprint, request, jsonify
from true_api.services.user_service import UserService
from true_api.services.challenge_service import ChallengeService
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('admin', __name__, url_prefix='/admin')
user_service = UserService()
challenge_service = ChallengeService()

@bp.route('/users', methods=['GET'])
@jwt_required()
def get_all_users():
    # TODO: Add admin role check
    users = user_service.get_all()
    return jsonify([user.to_dict() for user in users]), 200

@bp.route('/challenges', methods=['POST'])
@jwt_required()
def create_challenge_for_all():
    # TODO: Add admin role check
    data = request.get_json()
    users = user_service.get_all()
    created_challenges = []
    
    for user in users:
        challenge_data = data.copy()
        challenge_data['target_username'] = user.username
        challenge = challenge_service.create_challenge(**challenge_data)
        created_challenges.append(challenge.to_dict())
    
    return jsonify(created_challenges), 201

# Add more admin-related routes as needed