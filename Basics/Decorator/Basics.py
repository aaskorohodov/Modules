"""
Decorators ar a way to wrapp one function call into the other, that can execute some additional logic before or/and
ofter the main function, that is wrapped
"""


def decor(func_to_decorate):
    """decor makes a new function (below) and returns it. You can call decor in a usual way:
         show = decor(show)

    After that, the call to show() will execute the already wrapped function, since show is wrapper. But there is
    syntactic sugar to do just the same thing:
        @decor
        def show():
            print('Function')

    * it is important to understand that the result of decor is a new function, which consists of the original +
    wrapper. But it's a function, and a new one, so by calling show we're calling this new function."""

    def wrapper():
        print("Logic before main function's call")
        func_to_decorate()
        print("Logic after main function's call")
    return wrapper


# You can use several decorators at once
def decor2(func_to_decorate):
    def wrapper():
        print('Some more additional code before')
        func_to_decorate()
        print('Some more additional code after')
    return wrapper


@decor
@decor2
def show():
    print('Function')


show()
