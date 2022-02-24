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

def admin_get_posts():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM posts")
    posts = cur.fetchall()

    conn.close()
    return posts

def get_likes(post_id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT COUNT(is_like) FROM likes WHERE post_id=?",
        [post_id]
    )

    likes = cur.fetchone()
    conn.close()
    return likes

def get_posts():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
            SELECT posts.id, posts.content, posts.date, 
            posts.user_id, users.first_name, users.last_name
            FROM posts INNER JOIN users ON posts.user_id=users.id
            ORDER BY posts.date DESC
        """
    )
    posts = cur.fetchall()
    conn.close()
    
    return posts

def get_post_by_id(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
            SELECT posts.id, posts.content, posts.date, posts.user_id, users.first_name, users.last_name
            FROM posts INNER JOIN users ON posts.user_id = users.id
            WHERE posts.id=?
        """,
        [id]
    )

    post = cur.fetchone()
    conn.close()
    return post

def add_a_like(user_id, post_id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO likes (user_id, post_id, is_like) VALUES (?,?,?)",
        [user_id, post_id, 1]
    )

    conn.commit()
    conn.close()
    return True
