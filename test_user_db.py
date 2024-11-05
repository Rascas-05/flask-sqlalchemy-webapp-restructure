#try and add a new user to site db
import sqlite3

connection = sqlite3.connect('site.db')


#with open('schema.sql') as f:
#    connection.executescript(f.read())

cur = connection.cursor()

# cur.execute("INSERT INTO user (username, email, image_file, password) VALUES (?, ?, ?, ?)",
#             ('Joey', 'joey@hotmail.com', 'default.png', 'password')
#             )

# cur.execute("INSERT INTO user (username, email, image_file, password) VALUES (?, ?, ?, ?)",
#             ('Missy Higgins', 'missyhiggins@yahoo.com', 'default.png', 'mypassword')
#             )

cur.execute("INSERT INTO user (username, email, image_file, password) VALUES (?, ?, ?, ?)",
            ('karolina', 'protsenko@protonmail.com', 'default.png', '$2b$12$F0JSSWlrD598cJHJWa374en8tdJfEgoZdmbyS4n16AwiCpu2ebvm6')
            )
connection.commit()
connection.close() 