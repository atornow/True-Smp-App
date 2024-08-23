from .auth import bp as auth_bp
from .news import bp as news_bp
from .challenges import bp as challenges_bp
from .gallery import bp as gallery_bp
from .stats import bp as stats_bp
from .admin import bp as admin_bp

def init_app(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(news_bp)
    app.register_blueprint(challenges_bp)
    app.register_blueprint(gallery_bp)
    app.register_blueprint(stats_bp)
    app.register_blueprint(admin_bp)