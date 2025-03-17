import sqlite3
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

def db_execute(command, params=None, path=DB_PATH):
    """
    Funkce pro provedení SQL dotazu
    """
    conn = connect_db(path)
    if params:
        result = conn.execute(command, params).fetchall()
    else:
        result = conn.execute(command).fetchall()
    conn.commit()
    conn.close()
    return result


def db_query(command, params=None, path=DB_PATH):
    """
    Funkce pro provedení SQL dotazu bez commit
    """
    conn = connect_db(path)
    if params:
        result = conn.execute(command, params).fetchall()
    else:
        result = conn.execute(command).fetchall()
    conn.close()
    return result
