from .manage_users import get_db_connection

def get_following(user_id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
            SELECT following.followed, users.first_name, users.last_name
            FROM following INNER JOIN users ON following.followed=users.id
            WHERE following.user_id=?
        """,
        [user_id]
    )

    following = cur.fetchall()
    conn.close()
    return following

def get_followers(users_id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
            SELECT following.user_id, users.first_name, users.last_name
            FROM following INNER JOIN users ON following.user_id=users.id
            WHERE following.followed=?
        """,
        [users_id]
    )

    followers = cur.fetchall()

    conn.close()
    return followers

def follow_a_user(user_id, followed):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO following (user_id, followed) VALUES (?,?)",
        [user_id, followed]
    )

    conn.commit()
    conn.close()

def unfollow_a_user(user_id, followed):
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute(
        'DELETE FROM following WHERE user_id=? AND followed=?',
        [user_id, followed]
    )

    conn.commit()
    conn.close()