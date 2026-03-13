import sqlite3

def create_db():
    conn = sqlite3.connect("student.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        username TEXT,
        password TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS predictions(
        username TEXT,
        reading INTEGER,
        writing INTEGER,
        predicted REAL
    )
    """)

    conn.commit()
    conn.close()


def add_user(username,password):
    conn = sqlite3.connect("student.db")
    c = conn.cursor()

    c.execute("INSERT INTO users VALUES (?,?)",(username,password))

    conn.commit()
    conn.close()


def login_user(username,password):
    conn = sqlite3.connect("student.db")
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password))

    data = c.fetchall()

    conn.close()

    return data


def save_prediction(username,reading,writing,predicted):
    conn = sqlite3.connect("student.db")
    c = conn.cursor()

    c.execute("INSERT INTO predictions VALUES (?,?,?,?)",
              (username,reading,writing,predicted))

    conn.commit()
    conn.close()