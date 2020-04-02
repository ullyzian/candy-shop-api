from core import app, db
import time
from flask import jsonify
from core.models import User

@app.route("/time")
def get_current_time():
    data = {
        "time": time.time(),
        "user": User.query.all()
    }
    return data
