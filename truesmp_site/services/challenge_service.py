from truesmp_site.core import Service
from truesmp_site.models.challenge import Challenge

class ChallengeService(Service):
    __model__ = Challenge

    def create_challenge(self, **kwargs):
        challenge = self.__model__(**kwargs)
        return self.save(challenge)

    def get_active_challenges(self, username):
        return self.__model__.query.filter_by(target_username=username, active=True).all()

    def update_challenge_progress(self, challenge_id, progress):
        challenge = self.get(challenge_id)
        if challenge:
            challenge.current_progress = progress
            return self.save(challenge)
        return None