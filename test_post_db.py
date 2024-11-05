#try and add a new user to site db
import sqlite3

connection = sqlite3.connect('site.db')


#with open('schema.sql') as f:
#    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO post (title, content, date_posted, user_id) VALUES (?, ?, ?, ?)",
            ('First Post', 'Content for the first post', 'April 20, 2018', 123)
            )

cur.execute("INSERT INTO post (title, content, date_posted, user_id) VALUES (?, ?, ?, ?)",
            ('Second Post', 'Content for the second post', 'April 21, 2018',124)
            )

connection.commit()
connection.close() 