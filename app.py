from flask import Flask, render_template, request
from flask_socketio import SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

message_state = {}
ids = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/chat", methods=['POST'])
def chat(name=None):
    if request.method== 'POST':
        idss = request.form["id"]
        names = request.form["name"]
        return render_template("chat.html", chatid=idss, name=names)

@socketio.on('connection_established')
def handler(json):
    if json["id"] in message_state:
        message_state[json["id"]] += 1
        socketio.emit('other_est')
    else:
        message_state[json["id"]] = 1

@socketio.on('chatsend')
def send(json):    
    socketio.emit('chatrecieve', json)


if __name__ == "__main__":
    app.run(debug = True)