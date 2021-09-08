'''
SQL это собственный язык запросов к реляционной базе данных. Его используют разные базы данных, например MySQL, SQLite,
Oracle итд.

Основные команды:
CREATE DATABASE name;  # создание базы
DROP DATABASE name;  # удаление базы


Создание таблицы:
CREATE TABLE name(
    id INT
);

Другой пример:
CREATE TABLE people(
    id INT NOT NULL AUTO_INCREMENT,  # NOT NULL = не может быть пустым, AUTO_INCREMENT = повышать на 1
    name VARCHAR(30),
    name VARCHAR(50),
    bio TEXT,
    birth DATE,
    PRIMARY KEY(id)  # так указывает основной ключ
);

Таблицам следует задавать PRIMARY KEY, который является идентификатором конкретной записи. По нему можно обратиться
к записи, следовательно идентификатор должен быть уникальным. Часто для этого используют поле id

Расширение таблицы:
ALTER TABLE name ADD pass VARCHAR(32);  # 32, потому что пароли обычно хешированны, их длина обычно = 32

Удаления колонки из таблицы:
ALTER TABLE people DROP COLUMN pass;
'''