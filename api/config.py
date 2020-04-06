import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__)) + "/.."


class Config(object):
    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://username:password@postgres/candy-shop"
    DEBUG = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "db.sqlite")
    DEBUG = True


class DockerDevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://username:password@postgres/candy-shop"
    DEBUG = True


config = {"dev": DevelopmentConfig, "prod": ProductionConfig, "docker": DockerDevConfig}
