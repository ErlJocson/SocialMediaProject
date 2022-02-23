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
#             profile_pic BLOB,
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

conn.commit()
conn.close()