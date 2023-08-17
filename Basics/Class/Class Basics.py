class Car:
    def __init__(self, brand=None, model=None):
        """Initializing a class object"""

        self.brand = brand
        self.model = model

    def honk(self):
        """Class method. Class method == function, only it is called on the instance of that class"""

        print(f'{self.brand} {self.model} honks')

    def __str__(self):
        """Overriding default method, which returns the string representation of that instance"""

        return f'{self.brand} {self.model}'


vaz = Car('Vaz', '2107')    # Creating instance
print(vaz)                  # Calling for overriden __str__ (it will be called automatically by the print())
vaz.honk()                  # Calling method honk()
vaz.model = 2010            # Overriding some attribute's value
print(vaz)


class YAZ(Car):
    """Inheritance"""

    def honk(self):
        print('Overriding method of the parent class')


yaz = YAZ('Yaz', '51444')
print(yaz)
yaz.honk()


print(YAZ.__doc__)      # Documentation for that class (will print 'Inheritance')
print(yaz.__dict__)     # All attributes of that instance
