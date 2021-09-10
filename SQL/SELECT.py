'''
SELECT * FROM people;  # выборка всего из таблицы
SELECT name, bio FROM people;  # выборка всех полей name и bio из таблицы
SELECT name, bio FROM people WHERE id >= 2 AND id < 4;

SELECT * FROM people WHERE id <> 5 AND id <> 4 AND name = 'Bob' AND bio IS NULL;
* ставить можно любое число условий
* is используется со значением NULL. Еще есть IS NOT

SELECT * FROM people WHERE name = 'Ivan' OR id = 5;
* or оператор или

SELECT DISTINCT name FROM people;
* выборка только неповторяющихся значений. Если есть несколько повторов одного имени, то в выводе будет только 1 из них

SELECT * FROM people LIMIT 2
* выводит не более 2 записей

SELECT * FROM people LIMIT 2, 3
* пропускает первые 2 элемента, затем показывает следующие 3 элемента. LIMIT всегда записывается в конце!

SELECT * FROM people ORDER BY email
* выводить в порядке возрастания по email (алфавитный порядок, NULL первый). ORDER BY ставится после WHERE!
...ORDER BY email DESC... = обратный (нисходящий) порядок вывода

SELECT * FROM people WHERE id BETWEEN 2 and 6
* выборка между значениями

SELECT * FROM people WHERE id IN(2, 4, 3)
* перечисляются допустимые значения

SELECT * FROM people WHERE name LIKE 'M%'
* M% = начинается с М (идет М и потом другие знаки). % = любой знак или никакой знак.

Операторы LIKE:
% = любой знак
_ = только 1 знак
\% = экранирование, чтобы найти сам знак %


Операторы WHERE:
>
<
>=
<=
=                       равно
<>                      не равно
!=                      тоже не равно
BETWEEN х AND у         между х и у
ORDER BY (DESC/ASC)     сортировка в нисходящем или возрастающем порядке
LIMIT 1/2/3/...         ограничение на вывод записей
OFFSET 1/2/3/...        пропускает некоторое количество записей

*LIMIT можно прописать так – (LIMIT 2, 5)   что будет равняться   (LIMIT 5 OFFSET 2)
'''