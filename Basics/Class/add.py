class Time:
    def __init__(self, hour, min, sec):
        self.hour = hour
        self.min = min
        self.sec = sec

    def __add__(self, other):
        '''Переопределение логики сложения для экземпляров класса'''
        hours = self.hour + other.hour
        mins = self.min + other.min
        secs = self.sec + other.sec
        new_time = Time(hours, mins, secs)
        return new_time

    def __str__(self):
        return f'{self.hour}:{self.min}:{self.sec}'


t1 = Time(10, 30, 0)
t2 = Time(5, 5, 5)

print(t1 + t2)