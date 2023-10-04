#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import main
from flask import Flask, render_template
# from flask_socketio import SocketIO, send, emit

# global
app = Flask(__name__)
# socketio = SocketIO(app)

# web route
@app.route('/')
def index():
    return render_template("index.html", current_speed=0.0, current_lat=0.0, current_lon=0.0)

@app.route('/update')
def update():
    return main.VehicleData.json_data

def run():
    t = threading.Thread(target=app.run(host="0.0.0.0"))
    t.daemon = True
    t.start()

if __name__ == "__main__":
    print("what?")
