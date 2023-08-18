"""
A global variable is a variable that is available anywhere in the program (in the main body).
However, it is considered bad practice to set a variable in the body of main other than constants
(A, AAA, HIGHT, SMSHIT...)

A local variable is a variable declared within a program block.
Local variables are not visible in the main loop of the program, and after the execution of the block they are erased.
     * Variables declared inside loops are preserved.

When accessing a variable from the body of a function, the variable is first looked up in the local scope, and if it
is not there, the search is done in global scope.
"""

name = 'Tom'  # Global scoped variable


def say_hi():
    print('Hi', name)


def say_bye():
    name = 'Bob'  # Local scope with the same name. Global variable will remain unchanged
    print('Bye', name)


say_hi()
say_bye()


'''
'global' keyword is used to declare a variable in a global scope. However, if you declare a variable global,
and then assign it a value inside the function (create a variable inside the function), then it will be visible from 
the main body.
'''


def global_a():
    global a
    a = 10


global_a()
print(a)


'''
There is also a 'nonlocal' keyword that works similar to global, but only goes up 1 level,
you can climb from a nested function to a higher one.
     * with nonlocal you can't go up to main, only from function to function
'''

x = 0


def outer():
    x = 1

    def inner():
        x = 2
        print('Inner x =', x)
    inner()
    print('Outer x =', x)


print('Main x =', x)
outer()


def outer():
    x = 1

    def inner():
        nonlocal x  # Now x is taken from 1 level up
        x = 2
        print('Inner x =', x)
    inner()
    print('Outer x =', x)


print('Main x =', x)
outer()
