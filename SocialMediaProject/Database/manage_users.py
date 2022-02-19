import sqlite3

def get_db_connection():
    conn = sqlite3.connect('social.db')
    return conn

# Use this function before adding images to the database
def convert_to_binary_data(filename):
    """
        Converts digital data to binary data.
    """
    with open(filename, 'rb') as file:
        binary_data = file.read()
    return binary_data

def get_all_users():
    """
        Returns all of the users
    """
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')

    users = cur.fetchall()
    conn.close()

    return users

def check_if_email_exist(email):
    """
        Returns a user if email is in the database
    """
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