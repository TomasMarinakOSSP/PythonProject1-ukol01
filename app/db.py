import sqlite3
from flask import current_app

DB_PATH = 'database.sqlite'

def connect_db(db_path = DB_PATH):
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.SQLITE_ERROR:
        print("Nepodařilo se připojit k databázi")

def create_db():
    """
    Funkce pro vytvoření databáze
    """
    conn = connect_db()
    script = "scheme.sql"
    with open(script, 'r') as file:
        conn.executescript(file.read())
    conn.close()



def execute(command, params=None):
    """
    Funkce pro provedení SQL dotazu
    který mění data v databázi
    """
    with sqlite3.connect(current_app.config["DATABASE"]) as conn:
        if params:
            result = conn.execute(command, params).fetchall()
        else:
            result = conn.execute(command).fetchall()
        conn.commit()
        return result