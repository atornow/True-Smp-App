from true_api.extensions import db
from datetime import datetime

class GalleryPost(db.Model):
    __tablename__ = 'gallery_posts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    caption = db.Column(db.Text)
    likes = db.Column(db.JSON, default=list)
    username = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<GalleryPost {self.id}>'