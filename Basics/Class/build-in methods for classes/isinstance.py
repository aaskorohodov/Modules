"""isinstance checks, if an object belongs to some class"""


class Time:
    def __init__(self, hour, mins, sec):
        self.hour = hour
        self.min = mins
        self.sec = sec

    def __add__(self, other):
        """Overrides action to perform, when operator '+' is used on that instance"""

        # Checking, that provided object belongs to class Time
        if isinstance(other, Time):
            hours = self.hour + other.hour
            mins = self.min + other.min
            secs = self.sec + other.sec
            new_time = Time(hours, mins, secs)
            print('asdasd')
            return new_time
        else:
            return 'Not an instance'

    def __str__(self):
        return f'{self.hour}:{self.min}:{self.sec}'


t1 = Time(10, 30, 0)
t2 = 122552

print(t1 + t2)

print(isinstance(t2, Time))
