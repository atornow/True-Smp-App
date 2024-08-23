from true_api.core import Service
from true_api.models.news_post import NewsPost

class NewsService(Service):
    __model__ = NewsPost

    def create_news_post(self, heading, content, image_url=None):
        news_post = self.__model__(heading=heading, content=content, image_url=image_url)
        return self.save(news_post)

    def get_all_news_posts(self):
        return self.__model__.query.order_by(self.__model__.created_at.desc()).all()