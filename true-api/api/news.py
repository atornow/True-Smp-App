from flask import Blueprint, request, jsonify
from services.news_service import NewsService
from flask_jwt_extended import jwt_required, get_jwt_identity # type: ignore

bp = Blueprint('news', __name__, url_prefix='/news')
news_service = NewsService()

@bp.route('/', methods=['POST'])
@jwt_required
def create_news():
    data = request.get_json()
    heading = data.get('heading')
    content = data.get('content')
    image_url = data.get('image_url')

    if not heading or not content:
        return jsonify({"message": "Heading and content are required"}), 400

    news_post = news_service.create_news_post(heading, content, image_url)
    return jsonify(news_post.to_dict()), 201

@bp.route('/', methods=['GET'])
def get_news():
    news_posts = news_service.get_all_news_posts()
    return jsonify([post.to_dict() for post in news_posts]), 200