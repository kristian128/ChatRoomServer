from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def home():
    return "ChatRoomInc Server is Online! The latest version of ChatRoom is BETA V.01\nUpdates are in progress."

@socketio.on('message')
def handle_message(msg):
    print(f"Message received: {msg}")
    # Broadcast the message to all clients except the sender
    emit('message', msg, broadcast=True)  # Corrected line

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080, allow_unsafe_werkzeug=True)