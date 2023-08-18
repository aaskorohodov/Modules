# Multiple assignment example. In the first variable go the first value, in the second all the rest (list)
x, *y = 1, 2, 3, 4, 5, 6
print(x, y)     # 1 [2, 3, 4, 5, 6]

# Similarly, you can pack a tuple, and the list can be added to both the first and second variables:
x, *y = (1, 2, 3, 4)
print(x, y)     # 1 [2, 3, 4]

*x, y = (1, 2, 3, 4)
print(x, y)     # [1, 2, 3] 4

# String:
*x, y, z = "Hello world!"
print(x, y, z)  # ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l'] d !

# But this will cause an error:
#   *y = 1, 2, 3


# Similarly, you can unpack values from a list:
a = [-5, 5]     # Just a list

# If you unpack it to a suitable place (where exactly 2 variables are required), then everything will turn out:
for x in range(*a):  # Here we need a range of two values, just as many are in the list a = [-5, 5]
    print(x, end=" ")   # -5 -4 -3 -2 -1 0 1 2 3 4

# You can make it right inside range-function, is you want to make your code look over-complicated:
for x in range(*[-5, 5]):
    print(x, end=" ")
