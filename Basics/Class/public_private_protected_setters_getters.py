"""
public, protected, private  = режимы доступа к атрибутам и методам классов.

public = обычные переменные и методы, полный доступ
protected = аналогично, только перед ним стоит _ 1шт (никакой защиты нет)
private = доступ напрямую закрыт (даже прочитать нельзя), но можно обратится внутри класса

Чтобы менять или читать private, нужно создавать методы, которые обычно начинают с get и set, потому их называют геттеры
и сеттеры. Идя в том, что внутри такого метода можно сделать, например, проверку на тип данных (чтобы строку в числовой
атрибут не записать)
"""


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def set_coord(self, x, y):
        # Тут можно сделать проверку на тип данный
        self.__x = x
        self.__y = y

    def get_coord(self):
        return self.__x, self.__y

