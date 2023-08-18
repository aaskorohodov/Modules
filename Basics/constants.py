"""
Constants are ordinary variables that cannot be changed. Such variables are declared in capital letters:

    PI = 3.14

At the same time, from the point of view of the interpreter, this is the just a regular variable that can be changed.
Therefore, capital the letters only indicate to themselves and other people that this variable cannot be changed.
"""

CONSTANT_DO_NOT_CHANGE_IT_EVEN_BY_ASSIGNING_NEW_VALUE = 'Some value'

print('Hahaha! I am an evil-developer! I do change constants just for fun!!!11')

CONSTANT_DO_NOT_CHANGE_IT_EVEN_BY_ASSIGNING_NEW_VALUE = 'Another value!! Hahaha!!!'
print(f'CONSTANT_DO_NOT_CHANGE_IT_EVEN_BY_ASSIGNING_NEW_VALUE ='
      f' {CONSTANT_DO_NOT_CHANGE_IT_EVEN_BY_ASSIGNING_NEW_VALUE}')
