from flask import Blueprint, request, jsonify
from truesmp_site.services.challenge_service import ChallengeService
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('challenges', __name__, url_prefix='/challenges')
challenge_service = ChallengeService()

@bp.route('/', methods=['POST'])
@jwt_required()
def create_challenge():
    data = request.get_json()
    challenge = challenge_service.create_challenge(**data)
    return jsonify(challenge.to_dict()), 201

@bp.route('/', methods=['GET'])
@jwt_required()
def get_challenges():
    user_id = get_jwt_identity()
    challenges = challenge_service.get_active_challenges(user_id)
    return jsonify([challenge.to_dict() for challenge in challenges]), 200

@bp.route('/<int:challenge_id>/progress', methods=['PUT'])
@jwt_required()
def update_challenge_progress(challenge_id):
    data = request.get_json()
    progress = data.get('progress')
    
    if progress is None:
        return jsonify({"message": "Progress is required"}), 400

    updated_challenge = challenge_service.update_challenge_progress(challenge_id, progress)
    if updated_challenge:
        return jsonify(updated_challenge.to_dict()), 200
    return jsonify({"message": "Challenge not found"}), 404