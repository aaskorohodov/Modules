import sqlite3


'''
Передача именованного параметра, это передача данных для вставки в таблицу.
'''


with sqlite3.connect('cars.db') as conn:
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS cars (
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    )''')

    # :Price это то, что нужно подставить. Чтобы подставить на это место что-то, надо передать словарь, в котором
    # мы укажем ключ = именованный параметр для вставки, значение = значение для вставки
    # A% чтобы выбрать машины на букву А
    cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'A%'", {'Price': 0})

    print('Результат – данные в таблице:')
    cur.execute('''SELECT * FROM cars''')
    for el in cur:
        print(el)