"""Yu can nest one class into the other"""


class Women:
    def __init__(self, smth):
        self.smth = smth

    class Nested:
        smth_else = 'smth_else'


w = Women('smth')
print(w.smth)               # Main class attribute
print(w.Nested.smth_else)    # Nested class attribute

'''Nested classes make little sense and the same can be done through two regular classes.'''
