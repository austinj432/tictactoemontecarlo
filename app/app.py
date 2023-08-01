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
            session['xWin'] = False
            session['oWin'] = False
        if request.form.get('select') == "4x4":
            session['board_size'] = 4
            session["board"] = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
            session['turn'] = 'X'
            session['xWin'] = False
            session['oWin'] = False
        if request.form['select'] == "5x5":
            session['board_size'] = 5
            session["board"] = [[None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None], [None, None, None, None, None]]
            session['turn'] = 'X'
            session['xWin'] = False
            session['oWin'] = False
    print(session)
    return render_template('game.html', board_size=session['board_size'], board=session['board'], turn=session['turn'], xWin = session['xWin'], oWin = session['oWin'])

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    session["board"][row][col] = session["turn"]
    if session['board_size'] == 3:
        if session['board'][0] == ['X', 'X', 'X'] or session['board'][1] == ['X', 'X', 'X'] or session['board'][2] == ['X', 'X', 'X'] or (session['board'][0][0] == 'X' and session['board'][1][1] == 'X' and session['board'][2][2] == 'X') or (session['board'][0][2] == 'X' and session['board'][1][1] == 'X' and session['board'][2][0] == 'X') or (session['board'][0][0] == 'X' and session['board'][1][0] == 'X' and session['board'][2][0] == 'X') or (session['board'][0][1] == 'X' and session['board'][1][1] == 'X' and session['board'][2][1] == 'X') or (session['board'][0][2] == 'X' and session['board'][1][2] == 'X' and session['board'][2][2] == 'X'):
            session['xWin'] = True
        elif session['board'][0] == ['O', 'O', 'O'] or session['board'][1] == ['O', 'O', 'O'] or session['board'][2] == ['O', 'O', 'O'] or (session['board'][0][0] == 'O' and session['board'][1][1] == 'O' and session['board'][2][2] == 'O') or (session['board'][0][2] == 'O' and session['board'][1][1] == 'O' and session['board'][2][0] == 'O') or (session['board'][0][0] == 'O' and session['board'][1][0] == 'O' and session['board'][2][0] == 'O') or (session['board'][0][1] == 'O' and session['board'][1][1] == 'O' and session['board'][2][1] == 'O') or (session['board'][0][2] == 'O' and session['board'][1][2] == 'O' and session['board'][2][2] == 'O'):
            session['oWin'] = True
    if session['board_size'] == 4:
        if session['board'][0] == ['X', 'X', 'X', 'X'] or session['board'][1] == ['X', 'X', 'X', 'X'] or session['board'][2] == ['X', 'X', 'X', 'X'] or session['board'][3] == ['X', 'X', 'X', 'X'] or (session['board'][0][0] == 'X' and session['board'][1][1] == 'X' and session['board'][2][2] == 'X' and session['board'][3][3] == 'X') or (session['board'][0][3] == 'X' and session['board'][1][2] == 'X' and session['board'][2][1] == 'X' and session['board'][3][0] == 'X') or (session['board'][0][0] == 'X' and session['board'][1][0] == 'X' and session['board'][2][0] == 'X' and session['board'][3][0] == 'X') or (session['board'][0][1] == 'X' and session['board'][1][1] == 'X' and session['board'][2][1] == 'X' and session['board'][3][1] == 'X') or (session['board'][0][2] == 'X' and session['board'][1][2] == 'X' and session['board'][2][2] == 'X' and session['board'][3][2] == 'X') or (session['board'][0][3] == 'X' and session['board'][1][3] == 'X' and session['board'][2][3] == 'X' and session['board'][3][3] == 'X'):
            session['xWin'] = True
        elif session['board'][0] == ['O', 'O', 'O', 'O'] or session['board'][1] == ['O', 'O', 'O', 'O'] or session['board'][2] == ['O', 'O', 'O', 'O'] or session['board'][3] == ['O', 'O', 'O', 'O'] or (session['board'][0][0] == 'O' and session['board'][1][1] == 'O' and session['board'][2][2] == 'O' and session['board'][3][3] == 'O') or (session['board'][0][3] == 'O' and session['board'][1][2] == 'O' and session['board'][2][1] == 'O' and session['board'][3][0] == 'O') or (session['board'][0][0] == 'O' and session['board'][1][0] == 'O' and session['board'][2][0] == 'O' and session['board'][3][0] == 'O') or (session['board'][0][1] == 'O' and session['board'][1][1] == 'O' and session['board'][2][1] == 'O' and session['board'][3][1] == 'O') or (session['board'][0][2] == 'O' and session['board'][1][2] == 'O' and session['board'][2][2] == 'O' and session['board'][3][2] == 'O') or (session['board'][0][3] == 'O' and session['board'][1][3] == 'O' and session['board'][2][3] == 'O' and session['board'][3][3] == 'O'):
            session['oWin'] = True
    if session['board_size'] == 5:
        if session['board'][0] == ['X', 'X', 'X', 'X', 'X'] or session['board'][1] == ['X', 'X', 'X', 'X', 'X'] or session['board'][2] == ['X', 'X', 'X', 'X', 'X'] or session['board'][3] == ['X', 'X', 'X', 'X', 'X'] or session['board'][4] == ['X', 'X', 'X', 'X', 'X'] or (session['board'][0][0] == 'X' and session['board'][1][1] == 'X' and session['board'][2][2] == 'X' and session['board'][3][3] == 'X' and session['board'][4][4] == 'X') or (session['board'][0][4] == 'X' and session['board'][1][3] == 'X' and session['board'][2][2] == 'X' and session['board'][3][1] == 'X' and session['board'][4][0] == 'X') or (session['board'][0][0] == 'X' and session['board'][1][0] == 'X' and session['board'][2][0] == 'X' and session['board'][3][0] == 'X' and session['board'][4][0] == 'X') or (session['board'][0][1] == 'X' and session['board'][1][1] == 'X' and session['board'][2][1] == 'X' and session['board'][3][1] == 'X' and session['board'][4][1] == 'X') or (session['board'][0][2] == 'X' and session['board'][1][2] == 'X' and session['board'][2][2] == 'X' and session['board'][3][2] == 'X' and session['board'][4][2] == 'X') or (session['board'][0][3] == 'X' and session['board'][1][3] == 'X' and session['board'][2][3] == 'X' and session['board'][3][3] == 'X' and session['board'][4][3] == 'X') or (session['board'][0][4] == 'X' and session['board'][1][4] == 'X' and session['board'][2][4] == 'X' and session['board'][3][4] == 'X' and session['board'][4][4] == 'X'):
            session['xWin'] = True
        elif session['board'][0] == ['O', 'O', 'O', 'O', 'O'] or session['board'][1] == ['O', 'O', 'O', 'O', 'O'] or session['board'][2] == ['O', 'O', 'O', 'O', 'O'] or session['board'][3] == ['O', 'O', 'O', 'O', 'O'] or session['board'][4] == ['O', 'O', 'O', 'O', 'O'] or (session['board'][0][0] == 'O' and session['board'][1][1] == 'O' and session['board'][2][2] == 'O' and session['board'][3][3] == 'O' and session['board'][4][4] == 'O') or (session['board'][0][4] == 'O' and session['board'][1][3] == 'O' and session['board'][2][2] == 'O' and session['board'][3][1] == 'O' and session['board'][4][0] == 'O') or (session['board'][0][0] == 'O' and session['board'][1][0] == 'O' and session['board'][2][0] == 'O' and session['board'][3][0] == 'O' and session['board'][4][0] == 'O') or (session['board'][0][1] == 'O' and session['board'][1][1] == 'O' and session['board'][2][1] == 'O' and session['board'][3][1] == 'O' and session['board'][4][1] == 'O') or (session['board'][0][2] == 'O' and session['board'][1][2] == 'O' and session['board'][2][2] == 'O' and session['board'][3][2] == 'O' and session['board'][4][2] == 'O') or (session['board'][0][3] == 'O' and session['board'][1][3] == 'O' and session['board'][2][3] == 'O' and session['board'][3][3] == 'O' and session['board'][4][3] == 'O') or (session['board'][0][4] == 'O' and session['board'][1][4] == 'O' and session['board'][2][4] == 'O' and session['board'][3][4] == 'O' and session['board'][4][4] == 'O'):
            session['oWin'] = True
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
        session['board_size'] = 3
    elif session["board_size"] == 4:
        session["board"] = [[None, None, None, None], 
                            [None, None, None, None], 
                            [None, None, None, None], 
                            [None, None, None, None]]
        session['board_size'] = 4
    else:
        session["board"] = [[None, None, None, None, None], 
                            [None, None, None, None, None], 
                            [None, None, None, None, None], 
                            [None, None, None, None, None], 
                            [None, None, None, None, None]]
        session['board_size'] = 5
    session["turn"] = "X"
    session['xWin'] = False
    session['oWin'] = False
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