from truesmp_site.extensions import db
from datetime import datetime

class Challenge(db.Model):
    __tablename__ = 'challenges'

    id = db.Column(db.Integer, primary_key=True)
    amount_goal = db.Column(db.Integer, nullable=False)
    current_progress = db.Column(db.Integer, default=0)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    initial_progress = db.Column(db.Integer, default=0)
    target_username = db.Column(db.String(80), nullable=False)
    active = db.Column(db.Boolean, default=True)
    category_id = db.Column(db.Integer)
    data_type = db.Column(db.String(50))
    points = db.Column(db.Integer, default=0)
    data_name = db.Column(db.String(255), nullable=False)
    block_action = db.Column(db.String(50))

    def __repr__(self):
        return f'<Challenge {self.description}>'