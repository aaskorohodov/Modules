"""Изначально в определяемых пользователем классах нет поддержки функций len и abs, но их можно прописать вручную,
используя свою логику."""


class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        """Тут мы считаем длину тип для линии, вычитая из первой точки последнюю (а можно наоборот). У len есть
        вшитое ограничение - он не может возвращать отрицательное число (типо длина не может быть отрицательной).
        Поэтому чтобы не было ошибки, предварительно делаем abs, никак не связанный с abs в этом классе."""
        listed_coords = list(self.__coords)
        distance = listed_coords[-1] - listed_coords[0]
        if distance < 0:
            distance = abs(distance)
        return distance

    def __abs__(self):
        """А тут делаем список из имеющихся координат, прогоняя каждую через обычный abs (map умеет склеивать функцию
        с какими-то данными, перебирая их (данные))"""
        return list(map(abs, self.__coords))


p = Point(1, 5, -10)
print(len(p))
print(abs(p))