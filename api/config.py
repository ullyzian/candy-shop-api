import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # General Config
    DEBUG = True

    # Database
    SQLALCHEMY_DATABASE_URI = (
        'postgresql://username:password@postgres/candy-shop'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
