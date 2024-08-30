from flask.cli import FlaskGroup
from flask import Flask, jsonify
from utils.extensions import db, migrate, jwt
from utils.config import config
from api import init_app as init_api

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize utils.extensions
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

app = create_app()
cli = FlaskGroup(app)

@app.cli.command("create-db")
def create_db():
    """Creates the db tables."""
    db.create_all()

@app.cli.command("drop-db")
def drop_db():
    """Drops the db tables."""
    db.drop_all()

if __name__ == '__main__':
    cli()