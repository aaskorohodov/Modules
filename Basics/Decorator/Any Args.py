'''
Ниже показан пример универсального декоратора, который умеет принимать любое число аргументов и передавать их дальше
(в декорируемую функцию). Соответственно, если передается 0 аргументов, то ничего и не передается.
'''


def decor(func):
    def wrapper(*args, **kwargs):
        '''
        Тут wrapper принимает любое число *неименованных и **именованных аргументов, печатает их и передает в функцию.
        Если аргументы не были переданы в декоратор, то они и не попадут в функцию.
        '''
        print('args:', args)
        print('kwargs:', kwargs)
        func(*args, **kwargs)
    return wrapper


@decor
def func_no_args():
    print('Some_Func')


func_no_args()


@decor
def func_with_args(a, b, c):
    print(a + b + c)


func_with_args(1, 2, 3)


class Mary:
    def __init__(self):
        self.age = 30

    @decor
    def sayYourAge(self, lie = -3):
        print("Мне {} лет, а ты бы сколько дал?".format(self.age + lie))


m = Mary()
m.sayYourAge()

'''
Желательно всегда пробрасывать *args и **kwargs через декоратор. Это позволит менять декорируемую функцию и не трогать
декоратор.
'''