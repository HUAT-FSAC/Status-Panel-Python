from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)
# TODO: using socket.io to update values in realtime

@app.route('/')
def index():
    return render_template("index.html", current_speed=0.0, current_lat=0.0, current_lon=0.0)

@app.route('/settings')
def settings():
    return "das"

if __name__ == "__main__":
    # app.run(debug=True)
    socketio.run(app)