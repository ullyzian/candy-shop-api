import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy_utils import create_database, database_exists

# Local files import
from api.config import config

app = Flask(__name__)

# Cors
CORS(app)

# Config
env = os.environ.get("FLASK_ENV", "dev")
app.config.from_object(config[env])

# Models
db_url = app.config["SQLALCHEMY_DATABASE_URI"]
if not database_exists(db_url):
    create_database(db_url)
db = SQLAlchemy(app)
Migrate(app, db)

# Shemas
ma = Marshmallow(app)


def create_app():
    # Routes
    from api import routes
    return app
