from .manage_users import get_db_connection

def add_post(details):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO posts (content, user_id) VALUES (?,?)",
        [details["content"], details["user_id"]]
    )

    conn.commit()
    conn.close()

def get_posts():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM posts ORDER BY date DESC")
    posts = cur.fetchall()
    conn.close()

    return posts