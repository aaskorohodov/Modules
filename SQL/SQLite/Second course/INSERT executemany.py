import sqlite3


'''
.executemany() очень похож на перебор циклом for, только цикл не требуется. Вместо этого, метод просто принимает вторым
аргументом список, который надо перебрать и делаем все сам.
'''

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

    # аналогичен перебору циклом for, только проще
    # cur.executemany('''
    #     INSERT INTO cars VALUES (NULL, ?, ?)
    #     ''', cars)

    print('Результат – данные в таблице:')
    cur.execute('''SELECT * FROM cars''')
    for el in cur:
        print(el)