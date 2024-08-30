from services.core import Service
from models.gallery_post import GalleryPost

class GalleryService(Service):
    __model__ = GalleryPost

    def create_gallery_post(self, user_id, username, image_url, caption=None):
        gallery_post = self.__model__(user_id=user_id, username=username, image_url=image_url, caption=caption)
        return self.save(gallery_post)

    def get_gallery_posts(self, page=1, per_page=10):
        return self.__model__.query.order_by(self.__model__.created_at.desc()).paginate(page=page, per_page=per_page, error_out=False)

    def like_post(self, post_id, username):
        post = self.get(post_id)
        if post and username not in post.likes:
            post.likes.append(username)
            return self.save(post)
        return None