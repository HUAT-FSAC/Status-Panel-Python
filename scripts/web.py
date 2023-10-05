#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# this code must run in python3, otherwise socketio will not work

from flask import Flask, render_template
from flask_socketio import SocketIO

# global
app = Flask(__name__, template_folder='./template')
socketio = SocketIO(app)

# web route
@app.route('/')
def index():
    return render_template("index.html", current_speed=0.0, current_lat=0.0, current_lon=0.0)

@socketio.on('connect')
def handle_connection():
    print('frontend has connected')
    socketio.emit("connection", "backend connected")

@socketio.on('disconnect')
def handle_disconnect():
    print('frontend disconnected')
    socketio.emit("connection", "backend disconnected")

@socketio.on('msg')
def msg(data):
    # actually msg callback
    print("msg" + data)
    pass

@socketio.on("control")
def control(cmd):
    #TODO
    pass

def update(data):
    socketio.emit("server_response", data)

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)
