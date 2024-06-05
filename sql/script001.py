import sqlite3

con = sqlite3.connect("../todo.db")
cur = con.cursor()

cur.execute("CREATE TABLE note(Id INTEGER PRIMARY KEY, Date TEXT, Text TEXT);")