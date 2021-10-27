'''
getattr(obj, name [, default]) — возвращает значение атрибута объекта, либо default, если такого атрибута нет
hasattr(obj, name) — проверяет на наличие атрибута name в obj;
setattr(obj, name, value) — задает значение атрибута (если атрибут не существует, то он создается);
delattr(obj, name) — удаляет атрибут с именем name.
'''


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