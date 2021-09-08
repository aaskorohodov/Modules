import sqlite3


conn = sqlite3.connect('orders.db')
cur = conn.cursor()


cur.execute("SELECT * FROM users;")
one_result = cur.fetchone()
print(one_result)
'''fetchone() берет первый результат, и запоминает, где он находится. Если вызвать повторно, то fetchone()
вернет уже следующий результат.'''


cur.execute("SELECT * FROM users;")
three_results = cur.fetchmany(3)
print(three_results)
three_results = cur.fetchmany(3)
print(three_results)
print(type(three_results))  # возвращается питоновский список кортежей
'''fetchmany() работает аналогично и также запоминает, где он остановился.'''


cur.execute("SELECT * FROM users;")
all_results = cur.fetchall()
print(all_results)
'''Тут просто возвращается все, что имеется'''


