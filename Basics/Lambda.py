# An example of a standard function and a similar lambda
def func(number):
    """This is a standard function"""

    return number + 1


num = 1
print(func(num))

# This is the same function, but made with lambda
print((lambda x: x + 1)(num))  # Lambda expression (lambda x: x + 1), and then its argument (x)


# A bad example of assigning Lambda to a variable, turning it into a standard named function
add_one = lambda x: x + 1
print(add_one(1))

# As any regular function, Lambda can make calls to other callables inside Lambda's body
(lambda x: print(x))(10)


# An example of using several arguments
full_name = lambda first_name, last_name: f'{first_name} {last_name}'
print(full_name('Petr', 'Petrov'))


# Another example
def add(x, y):
    return x + y
print(add(1, 3))

add = lambda x, y: x + y
print(add(1, 3))


# Lambda can be moved to another line, but this requires (parentheses)
func = (
    lambda x:
        x + 1
)


# An example of using Lambda to determine if a number is odd or even
odd_or_even = (
    lambda x:
    (x % 2 and 'odd' or 'even')
)
'''This example illustrates, how your code must never look, because:
1. Lambda is itself is a shitty thing
2. In this case, Lambda is assigned to a variable, instead of using a regular def
3. The body of the Lambda is pretty hard to understand => debug or modify in the future

What and how this hell does:
1. There are 2 main parts in Lambda's body (x % 2) and ('odd' or 'even'), which will be evaluated first
2. The right part ('odd' or 'even') is always True (2 non-empty strings)
3. If (x % 2 is True) and ('odd' is True) -> 'odd' will be taken, because Python takes second operand in this case
4. Then, evaluating ('odd' or 'even'), 'odd' will be returned, because in case or 'or', first operand returned

5. If (x % 2 is False) and ('odd' is True) -> False will be evaluated
6. Then, while evaluating 'False' or 'even' -> 'even' will be returned.

Never-ever do this to your brain again. This is over-engineered bullshit, that requires 1000 kcal to be understood
'''
print(odd_or_even(6))


# The same:
def odd_or_even(number: int) -> str:
    if (number % 2) is True:
        return 'odd'
    else:
        return 'even'


print(odd_or_even(6))


# Default arguments in Lambda
add_xy = lambda x, y = 1: x + y
print(add_xy(5))


# *args and **kwargs in Lambda
add_some = lambda *args: sum(args)
print(add_some(1, 2, 3, 4, 5))

add_some_more = lambda **kwargs: sum(kwargs.values())
print(add_some_more(one=1, two=2, three=3))
