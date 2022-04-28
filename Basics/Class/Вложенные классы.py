"""В классы можно вкладывать другие классы"""


class Women:
    def __init__(self, smth):
        self.smth = smth

    class Meta:
        smth_else = 'smth_else'


w = Women('smth')
print(w.smth)  # Обращение к атрибуту основного класса
print(w.Meta.smth_else)  # Обращение к атрибуту вложенного класса

'''Вложенные классы имеют мало смысла и все то же самое можно сделать через два обычных класса.'''
