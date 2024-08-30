from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class Service:
    __model__ = None

    def __init__(self):
        self.db = db

    def get(self, id):
        return self.__model__.query.get(id)

    def get_all(self):
        return self.__model__.query.all()

    def create(self, **kwargs):
        instance = self.__model__(**kwargs)
        return self.save(instance)

    def update(self, instance, **kwargs):
        for key, value in kwargs.items():
            setattr(instance, key, value)
        return self.save(instance)

    def save(self, instance):
        self.db.session.add(instance)
        self.db.session.commit()
        return instance

    def delete(self, instance):
        self.db.session.delete(instance)
        self.db.session.commit()