'''
Индексы нужны для быстрого поиска по содержанию поля.

Создание индекса:
CREATE INDEX Nindex ON people(name);

Nindex = произвольное имя индекса. Указываем таблицу people, затем колонку (name = имя колонки, это имя человека)

Удаление индекса:
DROP INDEX Nindex ON people;
*тут уже не нужно указывать колонку, на которую применялся индекс

'''