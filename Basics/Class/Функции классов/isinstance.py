class Time:
    def __init__(self, hour, min, sec):
        self.hour = hour
        self.min = min
        self.sec = sec

    def __add__(self, other):
        if isinstance(other, Time):
            '''Проверяет, что объект находится в класса'''
            hours = self.hour + other.hour
            mins = self.min + other.min
            secs = self.sec + other.sec
            new_time = Time(hours, mins, secs)
            return new_time
        else:
            return 'Это не экземпляр класса'

    def __str__(self):
        return f'{self.hour}:{self.min}:{self.sec}'


t1 = Time(10, 30, 0)
t2 = 122552

print(t1 + t2)

print(isinstance(t2, Time))  # более простая проверка
