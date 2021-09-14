'''
SQL позволяет вкладывать запрос в запрос. Например, одним запросом можно получить значение, которое использовать во
втором:

SELECT mark FROM marks
WHERE id = 1 AND subject = 'Си'
Это первый запрос, он вернет значение 3. Теперь мы знаем, что у какого-то студента есть оценка 3 по предмету Си, и мы
хотим посмотреть, у кого оценки по этому же предмету выше. Можно так:

SELECT name, subject, mark FROM marks
JOIN students ON students.id = marks.id
WHERE mark > 3 AND subject LIKE 'Си'


А можно объединить это все в 1 запрос:

SELECT name, subject, mark FROM marks
JOIN students ON students.id = marks.id
WHERE mark > (SELECT mark FROM marks WHERE id = 1 AND subject = 'Си') AND subject LIKE 'Си'
'''
import sqlite3


conn = sqlite3.connect(r'SQLite/Second course/saper.db')
cur = conn.cursor()
cur.execute('''SELECT mark FROM marks
WHERE id = 1 AND subject = "Си"''')

print('Оценка:')
for el in cur:
    print(el)




print('')

cur.execute('''SELECT name, subject, mark FROM marks
JOIN students ON students.id = marks.id
WHERE mark > 3 AND subject LIKE "Си"''')

print('У кого оценка выше:')
for el in cur:
    print(el)




print('')

cur.execute('''
SELECT name, subject, mark FROM marks
JOIN students ON students.id = marks.id
WHERE mark > (SELECT mark FROM marks WHERE id = 1 AND subject = 'Си') AND subject LIKE "Си"
''')

print('У кого оценка выше (вложенный запрос):')
for el in cur:
    print(el)




print('')

# Что если вложенный запрос вернет несколько значений? Будет выбрано первое:
cur.execute('''
SELECT name, subject, mark FROM marks
JOIN students ON students.id = marks.id
WHERE mark > (SELECT mark FROM marks WHERE id = 1) AND subject LIKE "Си"
''')

print('У кого оценка выше (вложенный запрос, несколько значений (никакой разницы)):')
for el in cur:
    print(el)




print('')

# Что если вложенный запрос вернет NULL? Тогда и второй запрос вернет NULL:
cur.execute('''
SELECT name, subject, mark FROM marks
JOIN students ON students.id = marks.id
WHERE mark > (SELECT mark FROM marks WHERE id = 10) AND subject LIKE "Си"
''')

print('У кого оценка выше (вложенный запрос вернул NULL):')
for el in cur:
    print(el)




print('')

# Допустимо использовать функции (avg например):
cur.execute('''SELECT avg(mark) FROM marks WHERE id = 1''')
print('средняя оценка:', cur.fetchone()[0], end=' ')
print('')

cur.execute('''
SELECT name, subject, mark FROM marks
JOIN students ON students.id = marks.id
WHERE mark > (SELECT avg(mark) FROM marks WHERE id = 1) AND subject LIKE "Си"
''')

print('У кого оценка выше (вложенный запрос c avg):')
for el in cur:
    print(el)




print('')

# Использование с INSERT. Возьмем всех девочек
cur.execute('''SELECT name, old FROM students WHERE sex = 2''')
print('Все студенты девочки (просто смотрим в начальной таблице):')

for el in cur:
    print(el)

# теперь вставим девочек в новую таблицу (без commit, чтобы можно повторить было):
cur.execute('''
INSERT INTO female
SELECT * FROM students WHERE sex = 2
''')


print('')
cur.execute('''SELECT name, old FROM female''')
print('Девочки из второй таблицы:')
for el in cur:
    print(el)