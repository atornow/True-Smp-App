from true_api.extensions import db
from datetime import datetime

class NewsPost(db.Model):
    __tablename__ = 'news_posts'

    id = db.Column(db.Integer, primary_key=True)
    heading = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<NewsPost {self.heading}>'