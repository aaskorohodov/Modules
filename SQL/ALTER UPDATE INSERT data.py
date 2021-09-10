'''
Добавление записей в таблицу:
INSERT INTO people (name, bio, birth, email) VALUES('Aleksei', 'He is a programmer', '1990-4-4', 'aleksei@mail.ru')

*Порядок перечисления столбцов (name, bio, birth, email) неважен, можно в любой последовательности. Каждому столбцу
соответствует передаваемое значение:
(name,       bio,                  birth,      email)
('Aleksei', 'He is a programmer', '1990-4-4', 'aleksei@mail.ru')
В этом примере id не передается, так как ему установленно значение AUTO_INCREMENT, она подставится автоматически.
Также тут дата передается как строка. Передавать все поля необязательно, можно передать лишь часть полей.

Необязательно указывать поля, в которые идет запись, можно просто перечислить VALUES по порядку:
INSERT INTO people VALUES (.......)


Изменение столбца:
ALTER TABLE people CHANGE birth birth DATE NOT NULL;
Изменяется условие записи – теперь это поле не может быть пустым. После CHANGE:
1. Имя столбца, который меняем (birth)
2. На что меняем имя (birth = остается без изменений)
3. DATE NOT NULL = будет дата, которая теперь не может быть равна нулю


Добавление нескольких столбиков:
INSERT INTO people (name, email, bio, birth)
    VALUES
    ('Sam', 'sam99@gmail.com', 'He is a gamer', '1995-10-14'),
    ('Kate', 'kate@gmail.com', 'She is a tester', '1980-11-02'),
    ('Max', 'max95@yahoo.com', 'He is a bugfixer', '1994-02-25');

*Это все можно записать в 1 строку, но так лучше читаемость. Перечисление значений идет через запятую, в конце ;


Перезапись значения:
UPDATE `people` SET `name` = 'Maxim' WHERE id = 6;

*кавычки `` используются для красоты, в них нельзя записывать сами данные, только имена столбцов и таблиц.
Тут перезаписывается то поле name, у которого id = 6. Перезаписывается на 'Maxim'.


Еще пример:
UPDATE people SET name = 'Max', email = 'max_new_mail@gmail.com' WHERE id > 4;

Обновляются все поля, где id > 4.


Еще пример:
UPDATE people SET name = 'Ivan', email = 'ivan@mail.ru' WHERE name = 'Max' AND id = 5;

*Тут используется условие AND, все интуитивно.
'''