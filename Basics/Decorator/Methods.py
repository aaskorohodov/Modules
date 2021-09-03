'''
Декорировать можно и методы, причем ниже показано, что декоратор можно размещать внутри класса, даже более того –
– внутри класса можно создавать переменную, которой присваивать результат работы декоратора. PyCharm ругается на ошибки,
но все прекрасно работает.
'''


def decor(decorated_method):
    '''
    Декоратор принимает метод и возвращает новую задекорированную функцию. Важно помнить, что вызов метода автоматически
    передает в себя имя экземпляра класса, так что новая функция (wrapper) должна принимать это имя (self).
    '''
    def wrapper(self):
        lie = 3
        decorated_method(self, lie)
    return wrapper


class Luci:
    def __init__(self):
        self.age = 30

    # def decor(decorated_method):
    #     def wrapper(self):
    #         lie = 3
    #         return decorated_method(self, lie)
    #
    #     return wrapper

    @decor
    def sayAge(self, lie):
        '''
        Это не сильно удачный пример, так как без декорации в sayAge нужно передавать lie, а после декорации – уже
        не нужно (lie объявляется в декораторе).
        '''
        print(f'Мне {self.age - lie}')

    # sayAge = decor(sayAge)


l = Luci()
l.sayAge()