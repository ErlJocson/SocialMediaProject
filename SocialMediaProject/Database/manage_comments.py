from .manage_users import get_db_connection

def get_all_comments():
    """
        This returns all of the comments
    """
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """ 
            SELECT comments.id, comments.content, comments.date, 
            users.first_name, users.last_name
            FROM comments INNER JOIN users ON comments.user_id = users.id
            ORDER BY comments.date
        """
    )
    comments = cur.fetchall()

    cur.close()
    return comments

def add_a_comment(details):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO comments (post_id, user_id, content) VALUES (?,?,?)",
        [details["post_id"],details["user_id"],details["content"]]
    )

    conn.commit()
    conn.close()

def delete_user_comment(comment_id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        'DELETE FROM comments WHERE id=?',
        [comment_id]
    )

    conn.commit()
    conn.close()