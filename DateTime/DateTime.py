import datetime


'''
class datetime.date(year, month, day) is a standard date. Attributes: year, month, day. An immutable object.
The datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None) class is a standard time, independent of the 
    date. Attributes: hour, minute, second, microsecond, tzinfo.
The datetime.timedelta class is the difference between two points in time, accurate to microseconds.
The datetime.tzinfo class is an abstract base class for time zone information (for example, to account for time zone
    and/or daylight saving time).
class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None) is a combination of
    date and time.


datetime class methods:

datetime.today() is a datetime object from the current date and time. Works the same as datetime.now() with tz=None.
datetime.fromtimestamp(timestamp) - date from standard time representation.
datetime.fromordinal(ordinal) - a date from a number representing the number of days since 01/01/1970.
datetime.now(tz=None) - a datetime object from the current date and time.
datetime.combine(date, time) - a datetime object from a combination of date and time objects.
datetime.strptime(date_string, format) - converts a string to a datetime (same as the strptime function from the time 
    module).
datetime.strftime(format) - see the strftime function from the time module.
datetime.date() is a date object (with time clipping).
datetime.time() is a time object (with date clipping).
datetime.replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]) - returns a new datetime
    object with the attributes changed.
datetime.timetuple() - returns struct_time from datetime.
datetime.toordinal() - number of days since 01/01/1970.
datetime.timestamp() - returns the time in seconds since the epoch.
datetime.weekday() - the day of the week as a number, Monday is 0, Sunday is 6.
datetime.isoweekday() - the day of the week as a number, Monday is 1, Sunday is 7.
datetime.isocalendar() is a tuple (ISO year, ISO week number, ISO day of the week).
datetime.isoformat(sep='T') - nice string like "YYYY-MM-DDTHH:MM:SS.mmmmmm" or if microsecond == 0,
    "YYYY-MM-DDTHH:MM:SS"
'''


print(datetime.datetime.today())
print(datetime.datetime.now())
# Differs only in the ability to accept time zone (by the second one)


d1 = datetime.datetime.today()
d1 = d1 + datetime.timedelta(days=1)
print(d1)
# Adds 1 day

d2 = d1 + datetime.timedelta(days=10)
print(d2)
# Adds 10 days

print(d2 - d1)
# Date subtraction

print((d2 - d1).days)
# Taking anly days

print(d1.strftime('%A %d %B %Y'))
# Output in human-readable format. strftime takes many different attributes to format the view

d = datetime.date(2021, 7, 21)
t = datetime.time(12, 30)
dt = datetime.datetime.combine(d, t)
print(dt)
# Creating DT-object by combining date and time

dt = dt.timetuple()
for el in dt:
    print(el)
'''
Creates a tuple that can be iterated over
2021    # year
7       # month
21      # day
12      # hour
30      # minutes
0       # second
2       #weekday (0 = Monday)
202     # number of days since 1st January
-1      # dst - method tzinfo.dst() returned None
'''

tday = datetime.date.today()
print(tday.weekday())
print(tday.isoweekday())

'''
.date.weekday - week starts at 0 (Mon = 0, Sun = 6)
.date.isoweekday - week starts at 1 (Mon = 1, Sun = 7)
'''

# Some examples

tdelta = datetime.timedelta(days=7)
print('What date will be in 7 days:', tday + tdelta)

bday = datetime.date(tday.year, 10, 2)
till_bday = bday - tday
print('Till birthday ', till_bday.days, 'дней')
print('Till birthday ', till_bday.total_seconds(), 'секунд')


t = datetime.time(9, 30, 45)
# Time only. You can optionally add milliseconds
d = datetime.date(2021, 5, 21)
# Date only
dt = datetime.datetime(2021, 5, 21, 9, 30, 45)
# Date and time

print(dt.time())
# Getting time from DT


import pytz
# Provides info about time zones. Recommended in datetime documentation


def tz():
    """Shows all available time-zones"""

    for tz in pytz.all_timezones:
        print(tz)


dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
dt_mtn = dt_utcnow.astimezone((pytz.timezone('US/Mountain')))
print(dt_mtn)
