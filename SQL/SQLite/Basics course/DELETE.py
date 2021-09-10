import sqlite3


conn = sqlite3.connect('orders.db')
cur = conn.cursor()


cur.execute("DELETE FROM users WHERE lname='Parker';")
conn.commit()

cur.execute("select * from users where lname='Parker'")
print(cur.fetchall())  # вернет пустой список