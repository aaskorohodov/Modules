import sqlite3 as sq


'''
con.row_factory = sq.Row дает объект, который работает аналогично словарю.
'''


with sq.connect("cars.db") as con:
    con.row_factory = sq.Row
    cur = con.cursor()

    cur.execute("SELECT model, price FROM cars")

    for result in cur:
        print(result['model'], result['price'])
        print(type(result))