from truesmp_site.extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=True)
    is_verified = db.Column(db.Boolean, default=True)  # Change to False for production
    verification_token = db.Column(db.String(255))
    verification_expires = db.Column(db.DateTime)
    blocks_placed = db.Column(db.ARRAY(db.Integer))
    blocks_mined = db.Column(db.ARRAY(db.Integer))
    playtimes = db.Column(db.ARRAY(db.Integer))
    last_update = db.Column(db.DateTime, default=datetime(2024, 3, 1))
    uuid = db.Column(db.String(255))
    team_id = db.Column(db.String(255), default='No Team')
    entities_killed = db.Column(db.ARRAY(db.Integer))
    points = db.Column(db.Integer, default=0)
    groups = db.Column(db.ARRAY(db.String), default=['member'])

    def __repr__(self):
        return f'<User {self.username}>'