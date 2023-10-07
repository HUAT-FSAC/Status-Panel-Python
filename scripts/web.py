#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# this code must run in python3, otherwise socketio will not work

from flask import Flask, render_template
from flask_socketio import SocketIO
import pprint, json, os
from threading import Lock

# global
app = Flask(__name__)
# socketio = SocketIO(app, cors_allowed_origins='*', async_mode='eventlet', logger=True, engineio_logger=True)
socketio = SocketIO(app, cors_allowed_origins='*', async_mode='eventlet')
thread = None
lock = Lock()
_json_raw = ""

# web route
@app.route('/')
def index():
    return render_template(
        "index.html", 
        speed=0.0, 
        lat=0.0, 
        lon=0.0,
        alt=0.0
    )

@socketio.on('connect')
def handle_connection():
    print("\n\n\nFrom web:")
    pprint.pprint(socketio.__dict__)

    global thread
    with lock:
        if thread == None:
            thread = socketio.start_background_task(target=update)
    pass

@socketio.on('disconnect')
def handle_disconnect():
    pass

@socketio.on('message')
def msg(data):
    # actually msg callback
    print("msg: " + data)
    pass

def read(file_path):
    global _json_raw
    with open(file_path, "r",) as f:
        _json_raw = f.read()

        try:
            json.loads(_json_raw)
        except ValueError:
            print("Invalid JSON")
        else:
            print("Valid JSON")
            return _json_raw
        return ""


def update():
    while True:
        socketio.emit("message", read("/home/" + os.getlogin() + "/.status-panel/data.json"))
        # socketio.sleep(2)
        # socketio.emit("message", "ads")

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
