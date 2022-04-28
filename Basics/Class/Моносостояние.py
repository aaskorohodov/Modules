"""
Если нужно создать несколько экземпляров с идентичными атрибутами, и чтобы атрибуты менялись сразу у всех, и если
создаешь новый атрибут, то он тоже менялся у всех (или удаляешь):
"""


class ThreadData:
    """__shared_attrs = общий словарь, при создании экземпляров, им автоматически присвоятся эти свойства, причем
    не как словарь, а как отдельный атрибуты, т.е.

    a = ThreadData()
    print(a.name)
        >> thread_1

    Меняя эти атрибуты в любом другом экземпляре, они изменятся во всех экземплярах.
    """
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1,
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


a = ThreadData()
print(a.name)  # thread_1
b = ThreadData()
print(b.name)  # thread_1
b.name = 'asdasd'
print(a.name)  # asdasd
b.new_atr = 'ddd'
print(a.new_atr)  # ddd