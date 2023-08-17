"""Arguments can be passed through the decorator, in this case wrapper must accept arguments and pass them to the
wrapped function:"""


def decor(func):
    def wrapper(arg1, arg2):
        print('Wrapper got:', arg1, arg2)
        func(arg1, arg2)

    return wrapper


@decor
def names(name, name2):
    print('Function got:', name, name2)


names('Ivan', 'Petrov')
