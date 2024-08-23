from flask import Blueprint, jsonify
from truesmp_site.services.user_service import UserService
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('stats', __name__, url_prefix='/stats')
user_service = UserService()

@bp.route('/me', methods=['GET'])
@jwt_required
def get_user_stats():
    user_id = get_jwt_identity()
    user = user_service.get(user_id)
    if user:
        return jsonify({
            'playtime': user.playtime,
            'blocks_placed': user.blocks_placed,
            'blocks_mined': user.blocks_mined,
            'entities_killed': user.entities_killed
        }), 200
    return jsonify({"message": "User not found"}), 404

# Add more stat-related routes as needed