import sqlite3

conn = sqlite3.connect('social.db')
cur = conn.cursor()

# cur.execute(
#     """
#         CREATE TABLE users(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             first_name TEXT NOT NULL,
#             last_name TEXT NOT NULL,
#             middle_name TEXT,
#             email TEXT NOT NULL UNIQUE,
#             profile_pic TEXT,
#             password TEXT NOT NULL
#         )
#     """
# )

# cur.execute(
#     """
#         CREATE TABLE posts(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             content TEXT NOT NULL,
#             date TIMESTAMP DEFAULT (DATETIME('now')),
#             user_id INTEGER NOT NULL,
#             FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
#         )
#     """
# )

# cur.execute(
#     """
#         CREATE TABLE likes(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_id INTEGER NOT NULL,
#             post_id INTEGER NOT NULL,
#             is_like INTEGER NOT NULL DEFAULT 0,
#             FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
#             FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE
#         )
#     """
# )

# cur.execute(
#     """
#         CREATE TABLE comments(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             content TEXT NOT NULL,
#             date TIMESTAMP DEFAULT (DATETIME('now')),
#             post_id INTEGER NOT NULL,
#             user_id INTEGER NOT NULL,
#             FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
#             FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
#         )
#     """
# )

# cur.execute(
#     """
#         CREATE TABLE following(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_id INTEGER NOT NULL,
#             followed INTEGER NOT NULL,
#             FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
#             FOREIGN KEY (followed) REFERENCES users(id) ON DELETE CASCADE
#         );
#     """
# )

# cur.execute(
#     """
#         INSERT INTO following (user_id, followed) VALUES (?,?)
#     """, [1, 2]
# )

cur.execute(
        """
            SELECT following.followed, users.first_name, users.last_name
            FROM following INNER JOIN users ON following.followed=users.id
            WHERE following.user_id=?
        """,
        [1]
    )

print(cur.fetchall())

conn.commit()
conn.close()