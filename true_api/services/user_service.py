from true_api.core import Service
from true_api.models.user import User

class UserService(Service):
    __model__ = User

    def get_by_username(self, username):
        return self.__model__.query.filter_by(username=username).first()

    def create_user(self, username, password, **kwargs):
        user = self.__model__(username=username, **kwargs)
        user.set_password(password)
        return self.save(user)

    def verify_user(self, username, token):
        user = self.get_by_username(username)
        if user and user.verification_token == token:
            user.is_verified = True
            user.verification_token = None
            user.verification_expires = None
            return self.save(user)
        return None