import sqlite3

connection = sqlite3.connect('vedmal.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO bets (bet, better1, better2) VALUES (?, ?, ?)",
            ('Content for the first post', 'Asdis', 'Egill')
            )

connection.commit()
connection.close()
