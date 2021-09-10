'''
Основные типы данных в SQLite3:
    NULL — значение NULL
    INTEGER — целое число
    REAL — число с плавающей точкой
    TEXT — текст
    BLOB — бинарное представление крупных объектов, хранящееся в точности с тем, как его ввели (например для картинок)
'''

import sqlite3


'''Объект conn представляет базу, создается как показано выше. Тут база будет создана в рабочей папке,
но можно задать другую.
*если файл уже существует, то будет выполнено подключение к нему.
Функция connect() создает объект sqlite3.Connection'''
conn = sqlite3.connect('orders.db')


'''Теперь, чтобы делать запросы к базе, нужен объект Cursor.'''
cur = conn.cursor()


'''Теперь создадим таблицы'''
cur.execute('''CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT);
''')
conn.commit()

cur.execute('''CREATE TABLE IF NOT EXISTS orders(
   orderid INT PRIMARY KEY,
   date TEXT,
   userid TEXT,
   total TEXT);
''')
conn.commit()