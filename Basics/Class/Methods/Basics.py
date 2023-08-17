"""Basics examples of methods"""


class Point:
    x = 1
    y = 1
    
    def set_coords(self, x, y):
        self.x = x
        self.y = y


pt = Point()
print(pt.__dict__)  # {}

# First way to set attributes to an instance:
pt.x = 10
pt.y = 10
print(pt.__dict__)  # {'x': 10, 'y': 10}

# Second way:
pt.set_coords(5, 5)
print(pt.__dict__)  # {'x': 5, 'y': 5}

# Third way:
Point.set_coords(pt, 3, 3)
print(pt.__dict__)  # {'x': 5, 'y': 5}
