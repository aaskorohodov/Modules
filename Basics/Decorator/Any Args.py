"""Below is an example of a universal decorator that can take any number of arguments and pass them on
(into the decorated function). If no arguments are passed, it will still work."""


def decor(func):
    def wrapper(*args, **kwargs):
        """Here wrapper takes any number of *unnamed and **named arguments, prints them and passes them to
        its function. If the arguments were not passed to the decorator - still works"""

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
    def say_your_age(self, lie=-3):
        print("I am {} years old".format(self.age + lie))


m = Mary()
m.say_your_age()

'''It's always a good idea to pass *args and **kwargs through the decorator. This will allow you to change the 
decorated function with out touching decorator.'''
