import sqlite3
from werkzeug.security import generate_password_hash

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

password = 'pass'
users_to_insert = [
    ('Gicu', generate_password_hash(password), 'Romania'),
    ('Michael Kemp', generate_password_hash(password), 'US'),
    ('Otto Wagner', generate_password_hash(password), 'Germany'),
    ('Chloe Graftiaux', generate_password_hash(password), 'France'),
    ('Jia Li', generate_password_hash(password), 'China'),
    ('Anne Olsen', generate_password_hash(password), 'Norway')
]
cur.executemany("INSERT INTO users (name, password, country) VALUES (?, ?, ?)", users_to_insert)

lb_to_insert = [
    ('45.5','03/12/22'),
    ('100','04/27/22'),
    ('60.1','04/01/22'),
    ('42','05/21/22'),
    ('61.4','05/23/22')
]
cur.executemany("INSERT INTO light(color, time) VALUES (?, ?)", lb_to_insert)

currusg_to_insert = [
    ('1','05/25/22'),
    ('200.1','05/25/22'),
    ('35','05/24/22'),
    ('42.4','05/25/22'),
    ('89.8','05/25/22')
]
cur.executemany("INSERT INTO current_usage(kw, data) VALUES (?, ?)", currusg_to_insert)

lb_to_insert = [
    ('cloudy','03/12/22'),
    ('sunny','04/27/22'),
    ('sunny','04/01/22'),
    ('cloudy','05/21/22'),
    ('cloudy','05/23/22')
]
cur.executemany("INSERT INTO weather(meteo, time1) VALUES (?, ?)", lb_to_insert)

connection.commit()
connection.close()