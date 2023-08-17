# Standard way to pass unnamed and named arguments to a function:
def my_func(*args, **kwargs):
    print(args)
    print(kwargs)


# **kwargs requires named arguments within a function call. Arguments are unpacked into a dictionary
def my_kwargs_func(**kwargs):
    print(kwargs)

    for k, v in kwargs.items():
        print(k, v)


my_kwargs_func(a=1, b=2, c=3)
