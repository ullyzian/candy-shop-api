from flask import Flask
from api.config import Config
from flask_cors import CORS
from flask_migrate import Migrate
from sqlalchemy_utils import create_database, database_exists


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)

    db_url = app.config["SQLALCHEMY_DATABASE_URI"]
    if not database_exists(db_url):
            create_database(db_url)

    from api.models import db

    db.init_app(app)
    Migrate(app, db)

    from api.views import view
    app.register_blueprint(views.view)

    return app
