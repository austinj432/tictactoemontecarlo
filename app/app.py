from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit
from flask_session import Session
from uuid import uuid4

app = Flask(__name__)
app.config['SECRET_KEY'] = uuid4().hex
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = "filesystem"
socketio = SocketIO(app)
Session(app)

@socketio.on('connect')
def connect():
    session['sid'] = request.sid

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('select') == "3x3":
            session['board'] = 3
        if request.form['select'] == "4x4":
            session['board'] = 4
        if request.form['select'] == "5x5":
            session['board'] = 5
        return render_template('game.html', board=session['board'])
        
    return render_template('index.html')


def generate_board(board):
    return