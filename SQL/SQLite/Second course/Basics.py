'''
SQLite работает по принципу "один пишет - многие читают". Т.е. есть ограничения на запись – один поток в один момент
времени, но нет ограничений на чтение.

Стандартные расширения:
.db
.db3
.sqlite
.sqlite3
'''

import sqlite3 as sq


'''Это безопасные метод открытия базы. close() не требуется.'''
with sq.connect('saper.db') as con:
    cur = con.cursor()

    '''Стандартный метод удаления таблицы. IF EXISTS помогает избежать ошибки'''
    cur.execute('DROP TABLE IF EXISTS users')

    '''Стандартный метод создания таблицы. IF NOT EXISTS можно опустить, но тогда при повторном создании 
    вылезет ошибка. AUTOINCREMENT необязателен, он и так будет увеличивать PRIMARY KEY, так как он обязан быть
    уникальным'''

    cur.execute('''CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sex INTEGER DEFAULT 1,
    old INTEGER,
    score INTEGER
    )''')

    '''rowid это уникальный идентификатор каждой записи (колонки), присваивается автоматически. Можно использовать его
    для связывания таблиц. Автоматически пишется даже если установлен PRIMARY KEY'''

    cur.execute('''SELECT rowid, * FROM users''')
    res = cur.fetchall()
    print(res)


# con.close()  # желательно закрывать соединение после использования
