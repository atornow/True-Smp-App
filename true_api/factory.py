from flask import Flask, jsonify
from .extensions import db, migrate, jwt
from .config import config
from .api import init_app as init_api

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    # Register blueprints
    init_api(app)
    
    # Register error handlers
    register_error_handlers(app)
    
    return app

def register_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify(error=str(e)), 400

    @app.errorhandler(404)
    def not_found(e):
        return jsonify(error="Not found"), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify(error="Internal server error"), 500

    # Add more error handlers as needed