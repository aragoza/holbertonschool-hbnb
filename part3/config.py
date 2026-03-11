import os
import secrets

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret-dev-3Ap5U43NcuL8Nk3f') or secrets.token_hex(32)
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
