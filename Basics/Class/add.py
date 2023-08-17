"""Method class.add() defines the behavior of the operator '+', when used on the instance of some class"""


class Time:
    def __init__(self, hour, mins, sec):
        self.hour = hour
        self.min = mins
        self.sec = sec

    def __add__(self, other):
        """Defining logic for '+'."""

        print(f'Custom method {self.__class__.__name__}.add() is called')
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
