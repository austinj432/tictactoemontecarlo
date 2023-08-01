from flask import Flask, render_template, session, request, redirect, url_for
from flask_socketio import SocketIO, emit
from flask_session import Session
from tempfile import mkdtemp
from uuid import uuid4
import numpy as np

app = Flask(__name__)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config['SECRET_KEY'] = uuid4().hex
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = "filesystem"
socketio = SocketIO(app)
Session(app)

@socketio.on('connect')
def connect():
    session['sid'] = request.sid

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/game", methods=['GET', 'POST'])
def game():
    if request.method == "POST":
        if request.form.get('select') == "3x3":
            session['board_size'] = 3
            session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
            session['turn'] = 'X'
        if request.form.get('select') == "4x4":
            session['board_size'] = 4
            session["board"] = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
            session['turn'] = 'X'
        if request.form['select'] == "5x5":
            session['board_size'] = 5
            session["board"] = [[None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None]]
            session['turn'] = 'X'
    print(session)
    return render_template('game.html', board_size=session['board_size'], board=session['board'], turn=session['turn'])

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    session["board"][row][col] = session["turn"]
    print(session)
    if session['turn'] == 'X':
        session['turn'] = 'O'
    else:
        session['turn'] = 'X'
    return redirect(url_for('game'))

@app.route("/clear")
def clear():
    if session["board_size"] == 3:
        session["board"] = [[None,None,None],
                            [None,None, None],
                            [None,None, None]]
    elif session["board_size"] == 4:
        session["board"] = [[None, None, None, None], 
                            [None, None, None, None], 
                            [None, None, None, None], 
                            [None, None, None, None]]
    else:
        session["board"] = [[None, None, None, None, None], 
                            [None, None, None, None, None], 
                            [None, None, None, None, None], 
                            [None, None, None, None, None], 
                            [None, None, None, None, None]]
    session["turn"] = "X"
    return redirect(url_for("game"))

@app.route("/make-move")
def AIMove():
    for i in range(session['board_size']):
        for j in range(session['board_size']):
            if session['board'][i][j] == None:
                session['board'][i][j] = session['turn']
                i = 1000
                break
        if i == 1000:
            break
    if session['turn'] == 'X':
        session['turn'] = 'O'
    else:
        session['turn'] = 'X'
    return redirect(url_for('game'))