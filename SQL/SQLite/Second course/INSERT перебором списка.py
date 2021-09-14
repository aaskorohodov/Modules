import sqlite3


# это будем вставлять в таблицу
cars = [
    ('Audi', 52642),
    ('Mercedes', 57127),
    ('Skoda', 9000),
    ('Volvo', 29000),
    ('Bentley', 350000)
]


with sqlite3.connect('cars.db') as conn:
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS cars (
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    )''')

    # ниже реализация. Интересно, что в качестве car_id передается NULL, который сам повышается до нужного
    # for el in cars:
    #     cur.execute('''
    #         INSERT INTO cars VALUES (NULL, ?, ?)
    #     ''', el)

    print('Результат – данные в таблице:')
    cur.execute('''SELECT * FROM cars''')
    for el in cur:
        print(el)