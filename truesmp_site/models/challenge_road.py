# truesmp_site/models/challenge_road.py
from truesmp_site.extensions import db

class ChallengeRoad(db.Model):
    __tablename__ = 'challenge_roads'

    id = db.Column(db.Integer, primary_key=True)
    rewards = db.Column(db.JSON)
    category_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<ChallengeRoad {self.id}>'