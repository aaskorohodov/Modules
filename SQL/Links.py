'''
Создание таблицы с полями, ссылающимися на другие поля:
CREATE TABLE orders(
    id INT NOT NULL AUTO_INCREMENT,
    orderNumder INT,
    shopId INT,                                     #Это поле будет ссылаться на другое
    personId INT,                                   #Это поле будет ссылаться на другое
    date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id),
    FOREIGN KEY(shopId) REFERENCES shop(id),        #Указание, на ссылку
    FOREIGN KEY(personId) REFERENCES people(id)     #Указание, на ссылку
);


'''