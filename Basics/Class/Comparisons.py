class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __lt__(self, other):
        """<"""

        # Creating 2 tuples (by using 2 different ways)
        self_values = (self.hour, self.minute, self.second)
        other_values = other.hour, other.minute, other.second

        # Comparing these tuples
        return self_values < other_values

    def __gt__(self, other):
        """>"""

        self_values = self.hour, self.minute, self.second
        other_values = other.hour, other.minute, other.second

        return self_values > other_values

    def __eq__(self, other):
        """==="""

        self_values = self.hour, self.minute, self.second
        other_values = other.hour, other.minute, other.second

        return t1 == t2

    '''There are also le (less equal <=), ne (not equal) and qe (greater or equal)'''


t1 = Time(0, 1, 0)
t2 = Time(0, 1, 0)

print(t1 == t2)
