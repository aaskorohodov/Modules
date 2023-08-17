"""
getattr(obj, name [, default]) - returns the value of an object's attribute, or default if there is no such attribute
hasattr(obj, name) - checks for the presence of some attribute in obj;
setattr(obj, name, value) - sets the value of the attribute (if the attribute does not exist -> it will be created);
delattr(obj, name) - removes the attribute
"""


class Point3D:
    x = 1
    y = 1
    z = 1


print(getattr(Point3D, 'z'))
print(hasattr(Point3D, 'x'))
setattr(Point3D, 'q', 5)
print(Point3D.q)
delattr(Point3D, 'q')
print(hasattr(Point3D, 'q'))
