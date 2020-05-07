import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__)) + "/.."


class Config(object):
    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "db.sqlite")
    SECRET_KEY = "7ZoEeQHjysXszcVUWhdTK2b1UUPc84nt"
