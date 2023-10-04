#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

# global
app = Flask(__name__)
# socketio = SocketIO(app)

# web route
@app.route('/')
def index():
    return render_template("index.html", current_speed=0.0, current_lat=0.0, current_lon=0.0)

@app.route('/update')
def update():
    return '{"speed": 100}';

if __name__ == "__main__":
    app.run()
