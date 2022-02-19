from .manage_users import get_db_connection

def get_all_comments():
    """
        This returns all of the comments
    """
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM comments')
    comments = cur.fetchall()

    cur.close()
    return comments