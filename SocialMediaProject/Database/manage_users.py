import sqlite3

def get_db_connection():
    conn = sqlite3.connect('social.db')
    return conn

def get_all_users():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')

    users = cur.fetchall()
    conn.close()

    return users

def check_if_email_exist(email):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM users WHERE email=?",
        [email]
    )
    data = cur.fetchone()
    conn.close()
    return data

def adding_new_users(details):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO users (first_name, last_name, middle_name, email, password) VALUES (?,?,?,?,?)',
        [details['first_name'], details['last_name'], details['middle_name'], details['email'], details['password']]
    )

    cur.execute('SELECT * FROM users WHERE email=?', [details['email']])
    new = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return new