import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy_utils import create_database, database_exists

# Local files import
from api.config import Config

app = Flask(__name__)

# Cors
CORS(app)

app.config.from_object(Config)

# Models
db_url = app.config["SQLALCHEMY_DATABASE_URI"]
if not database_exists(db_url):
    create_database(db_url)
db = SQLAlchemy(app)
Migrate(app, db)

# Schemas
ma = Marshmallow(app)


def create_app():
    # Routes
    from api import routes
    from api import seeds

    return app
