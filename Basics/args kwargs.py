# стандартный метод передачи в функцию неименованных и именованных аргументов:
def my_func(*args, **kwargs):
    pass


# **kwargs требует именования аргументов внутри вызова функции (см. вызов функции). Аргументы распаковываются в словарь
def my_kwargs_func(**kwargs):
    print(kwargs)

    for k, v in kwargs.items():
        print(k, v)


my_kwargs_func(a = 1, b = 2, c = 3)