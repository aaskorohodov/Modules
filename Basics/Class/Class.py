class Car:
    def __init__(self, brand=None, model=None):
        '''Инициализация объекта класса'''
        self.brand = brand
        self.model = model

    def honk(self):
        '''Метод класса. Метод класса = функция, только она вызывается на объект класса'''
        print(f'{self.brand} {self.model} honks')

    def __str__(self):
        '''Переопределение метода print для объекта класса'''
        return f'{self.brand} {self.model}'


vaz = Car('Vaz', '2107') # создание экземпляра класса
print(vaz) # вызов переопределенного метода print
vaz.honk() # вызов метода honk
vaz.model = 2010 # переписывание атрибута класса
print(vaz)


class YAZ(Car):
    '''Наследование класса'''

    def honk(self):
        print('Переопределенный метод родительского класса')


yaz = YAZ('Yaz', '51444')
print(yaz)
yaz.honk()