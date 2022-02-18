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

    cur.execute(
        """
            SELECT posts.id, posts.content, posts.date, posts.likes, posts.user_id, users.first_name, users.last_name 
            FROM posts INNER JOIN users on posts.id=users.id
        """
    )
    posts = cur.fetchall()
    conn.close()

    return posts

def add_a_like(post_id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur .execute(
        "UPDATE posts SET likes = likes + 1 WHERE id=?",
        [post_id]
    )
    
    conn.commit()
    conn.close()
    return True