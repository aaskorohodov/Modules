'''
assert проверяет, является ли конструкция True или False. Если False, то поднимается исключение, текст исключения
можно задать.

Синтаксис:

assert condition, "message"
'''


assert sum([1,1]) == 2, 'Текст исключение, на случай, если будет не 2'


'''Чтобы превратить это в автотест, можно сделать следующее:'''

from Assert_this import some_sum


def some_test():
    assert type(some_sum([1,1])) == int, 'Возвращен неверный тип данных'
    assert some_sum([1,1]) == 2, 'Вычисления неверны'


if __name__ == '__main__':
    some_test()
    print('Everything is Ok')