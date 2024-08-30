from flask import Blueprint, request, jsonify
from services.gallery_service import GalleryService
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('gallery', __name__, url_prefix='/gallery')
gallery_service = GalleryService()

@bp.route('/', methods=['POST'])
@jwt_required()
def create_gallery_post():
    user_id = get_jwt_identity()
    data = request.get_json()
    image_url = data.get('image_url')
    caption = data.get('caption')
    username = data.get('username')

    if not image_url or not username:
        return jsonify({"message": "Image URL and username are required"}), 400

    post = gallery_service.create_gallery_post(user_id, username, image_url, caption)
    return jsonify(post.to_dict()), 201

@bp.route('/', methods=['GET'])
def get_gallery_posts():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    posts = gallery_service.get_gallery_posts(page, per_page)
    return jsonify({
        'items': [post.to_dict() for post in posts.items],
        'total': posts.total,
        'pages': posts.pages,
        'page': page
    }), 200

@bp.route('/<int:post_id>/like', methods=['POST'])
@jwt_required()
def like_post(post_id):
    user_id = get_jwt_identity()
    updated_post = gallery_service.like_post(post_id, user_id)
    if updated_post:
        return jsonify(updated_post.to_dict()), 200
    return jsonify({"message": "Post not found or already liked"}), 404