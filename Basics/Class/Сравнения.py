class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __lt__(self, other):
        '''<'''
        t1 = self.hour, self.minute, self.second  # создает кортеж из атрибутов
        t2 = other.hour, other.minute, other.second  # создает кортеж из атрибутов
        return t1 < t2  # сравнивает кортежи, но логика процесса может быть любой

    def __gt__(self, other):
        '''>'''
        t1 = self.hour, self.minute, self.second
        t2 = other.hour, other.minute, other.second
        return t1 > t2

    def __eq__(self, other):
        '''=='''
        t1 = self.hour, self.minute, self.second
        t2 = other.hour, other.minute, other.second
        return t1 == t2

    r'''Также есть le (less equal <=), ne (not equal) и qe (greater or equal)'''


t1 = Time(0, 1, 0)
t2 = Time(0, 1, 0)

print(t1 == t2)
