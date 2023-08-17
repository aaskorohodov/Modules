"""
If you need to create several instances with identical attributes, and so that the attributes change for everyone at
once, and if you create a new attribute, then it also changed for everyone (or if deleting it):
"""


class ThreadData:
    """__shared_attrs is a shared dictionary, when instantiated, these properties will be automatically assigned to
    all instances, and not as a dictionary, but as separate attributes, i.e.

    a = ThreadData()
    print(a.name)
    >> thread_1

    By changing these attributes in any other instance, they will change in all instances.
    """
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1,
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


a = ThreadData()
print(a.name)       # thread_1
b = ThreadData()
print(b.name)       # thread_1
b.name = 'other_name'
print(a.name)       # other_name
b.new_atr = 'new_attr'
print(a.new_atr)    # new_attr
