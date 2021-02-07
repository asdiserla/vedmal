import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('vedmal.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_bet(bet_id):
    conn = get_db_connection()
    bet = conn.execute('SELECT * FROM bets WHERE id = ?',
                        (bet_id,)).fetchone()
    conn.close()
    if bet is None:
        abort(404)
    return bet

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    bets = conn.execute('SELECT * FROM bets').fetchall()
    conn.close()
    return render_template('index.html', bets=bets)

@app.route('/<int:bet_id>')
def bet(bet_id):
    bet = get_bet(bet_id)
    return render_template('bet.html', bet=bet)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        bet = request.form['bet']
        better1 = request.form['better1']
        better2 = request.form['better2']

        if not bet:
            flash('Veðmál is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO bets (bet, better1, better2) VALUES (?, ?, ?)',
                         (bet, better1, better2))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')

# tafla með betters
# tengja id a betti við betters
# max length 128 stafir
