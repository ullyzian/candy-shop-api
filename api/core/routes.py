from core import app
import time


@app.route("/time")
def get_current_time():
    data = {"time": time.time()}
    return data
