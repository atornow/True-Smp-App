import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    COREPROTECT_DB_HOST = os.environ.get('COREPROTECT_DB_HOST')
    COREPROTECT_DB_USER = os.environ.get('COREPROTECT_DB_USER')
    COREPROTECT_DB_PASSWORD = os.environ.get('COREPROTECT_DB_PASSWORD')
    COREPROTECT_DB_NAME = os.environ.get('COREPROTECT_DB_NAME')
    TEAMS_DB_HOST = os.environ.get('TEAMS_DB_HOST')
    TEAMS_DB_USER = os.environ.get('TEAMS_DB_USER')
    TEAMS_DB_PASSWORD = os.environ.get('TEAMS_DB_PASSWORD')
    TEAMS_DB_NAME = os.environ.get('TEAMS_DB_NAME')

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URL')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}