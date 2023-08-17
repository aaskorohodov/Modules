"""Meta-classes are used to describe the process of creating classes themselves, the same way as the class describes
the process of creating its instances.

It looks very similar to what inheritance does, but in a bit fancier way"""


class Meta(type):
    def __new__(cls, name, bases, dct):
        """This method adds an attribute to every new instance"""

        new_instance = super().__new__(cls, name, bases, dct)
        new_instance.attr = 100

        return new_instance


class Foo(metaclass=Meta):
    pass


foo = Foo()
print(foo.attr)     # 100

'''Looks similar to the simple inheritance? You right, there is no difference. Technically, you may have a bit more
control, when using meta-classes, but as the Web says "don't use meta-classes, unless you know that this is your only
option", or something like that.'''
