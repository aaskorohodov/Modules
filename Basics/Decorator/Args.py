'''
Через декоратор можно передавать аргументы, в этом случае wrapper должен принимать аргументы и передавать их в вызов
оборачиваемой функции:
def wrapper(arg1, arg2):
    print('Wraper получил:', arg1, arg2)
    func(arg1, arg2)
'''


def decor(func):
    def wrapper(arg1, arg2):
        print('Wraper получил:', arg1, arg2)
        func(arg1, arg2)
    return wrapper


@decor
def names(name, name2):
    print('Функция получила:', name, name2)


names('Иван', 'Петров')