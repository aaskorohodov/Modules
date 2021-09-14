import sqlite3


'''Пример демонстрирует работу rollback – при возникновении исключения, он откатит состояние базы к метке BEGIN
(она в SQL-запросе). Идея в том, что commit не будет выполнен'''


con = None
try:
    con = sqlite3.connect("cars.db")
    cur = con.cursor()

    cur.executescript("""CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price INTEGER
        );
        BEGIN;
        INSERT INTO cars VALUES(NULL,'Audi',52642);
        INSERT INTO cars VALUES(NULL,'Mercedes',57127);
        INSERT INTO cars VALUES(NULL,'Skoda',9000);
        INSERT INTO cars VALUES(NULL,'Volvo',29000);
        INSERT INTO cars VALUES(NULL,'Bentley',350000);
        UPDATE cars2 SET price = price+1000
    """)
    con.commit()

except sqlite3.Error as e:
    if con: con.rollback()
    print("Ошибка выполнения запроса")
finally:
    if con: con.close()