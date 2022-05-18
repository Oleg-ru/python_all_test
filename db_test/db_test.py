import sqlite3

with sqlite3.connect("db/database.db") as db:
    cursor = db.cursor()
    query = """ CREATE TABLE IF NOT EXISTS expenses(id INTEGER, name TEXT) """
    cursor.execute(query)