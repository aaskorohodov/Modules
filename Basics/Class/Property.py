"""
property дает возможность работать с приватными атрибутами так, как если бы они были обычными. Это нужно, чтобы
ограничить лишь часть функционала, например чтобы можно было записать данные, но нельзя удалить.

property задается как атрибут, которому дается любое имя, а сам property последовательно принимает сеттеры, геттеры и
делитеры, (именно в таком порядке) в качестве аргументов. property сам вызовет свой первый, второй или третий аргумент,
в зависимости от обстоятельств, сделает что нужно и если там геттер, то вернет то, что возвращает геттер, а если
сеттер, то сделает то, что делает сеттер.
"""


class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    old = property(get_old, set_old)

    # Полный аналог того, что выше (но так не надо, будет PyCharm будет ошибки подчеркивать, но все будет работать)
    # Даем ссылку на property
    # old = property()
    # Даем ссылку на самого себя, но со встроенным сеттером
    # old = old.setter(set_old)
    # А теперь встраиваем геттер
    # old = old.getter(get_old)


p = Person('Peter', 30)
d = Person('Dave', 15)
p.old = 35
print(p.old)
print(d.old)

# это вызовет ошибку, потому что свойство приватное, удалить нельзя, делитера нет
# del p.old


class Person:
    """Тоже самое, только с декораторами"""
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    # !Первым обязательно прописывается геттер!
    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

print('')
s = Person('Sam', 25)
print(s.old)
s.old = 35
print(s.old)
