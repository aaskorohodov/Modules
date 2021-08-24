import datetime


'''
Класс datetime.date(year, month, day) – стандартная дата. Атрибуты: year, month, day. Неизменяемый объект.
Класс datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None) – стандартное время, не зависит от даты. Атрибуты: hour, minute, second, microsecond, tzinfo.
Класс datetime.timedelta – разница между двумя моментами времени, с точностью до микросекунд.
Класс datetime.tzinfo – абстрактный базовый класс для информации о временной зоне (например, для учета часового пояса и / или летнего времени).
Класс datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None) – комбинация даты и времени.


Методы класса datetime:

datetime.today() - объект datetime из текущей даты и времени. Работает также, как и datetime.now() со значением tz=None.
datetime.fromtimestamp(timestamp) - дата из стандартного представления времени.
datetime.fromordinal(ordinal) - дата из числа, представляющего собой количество дней, прошедших с 01.01.1970.
datetime.now(tz=None) - объект datetime из текущей даты и времени.
datetime.combine(date, time) - объект datetime из комбинации объектов date и time.
datetime.strptime(date_string, format) - преобразует строку в datetime (так же, как и функция strptime из модуля time).
datetime.strftime(format) - см. функцию strftime из модуля time.
datetime.date() - объект даты (с отсечением времени).
datetime.time() - объект времени (с отсечением даты).
datetime.replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]]) - возвращает новый объект datetime с изменёнными атрибутами.
datetime.timetuple() - возвращает struct_time из datetime.
datetime.toordinal() - количество дней, прошедших с 01.01.1970.
datetime.timestamp() - возвращает время в секундах с начала эпохи.
datetime.weekday() - день недели в виде числа, понедельник - 0, воскресенье - 6.
datetime.isoweekday() - день недели в виде числа, понедельник - 1, воскресенье - 7.
datetime.isocalendar() - кортеж (год в формате ISO, ISO номер недели, ISO день недели).
datetime.isoformat(sep='T') - красивая строка вида "YYYY-MM-DDTHH:MM:SS.mmmmmm" или, если microsecond == 0, "YYYY-MM-DDTHH:MM:SS"
'''


print(datetime.datetime.today())
print(datetime.datetime.now())
'''Различается только возможностью передавать во второй временную зону'''


d1 = datetime.datetime.today()
d1 = d1 + datetime.timedelta(days=1)
print(d1)
'''Прибавляет 1 день'''

d2 = d1 + datetime.timedelta(days=10)
print(d2)
'''Прибавляет 10 дней'''

print(d2 - d1)
'''Вычитание дат'''

print((d2 - d1).days)
'''Смотрим только атрибут дни'''

print(d1.strftime('%A %d %B %Y'))
'''Вывод в удобночитаемом формате. strftime принимает много разных атрибутов, для форматирования представления'''

d = datetime.date(2021, 7, 21)
t = datetime.time(12, 30)
dt = datetime.datetime.combine(d, t)
print(dt)
'''Создание объектов вручную и их сложение'''

dt = dt.timetuple()
for el in dt:
    print(el)
'''
Создает кортеж, его можно перебирать
2021    # year
7      # month
21      # day
12      # hour
30      # minute
0       # second
2       # weekday (0 = Monday)
202     # number of days since 1st January
-1      # dst - method tzinfo.dst() returned None
'''

tday = datetime.date.today()
print(tday.weekday())
print(tday.isoweekday())

'''
.date.weekday – неделя начинается с 0 (пн = 0, вс = 6)
.date.isoweekday – неделя начинается с 1 (пн = 1, вс = 7)
'''

# немного примеров работы с datetime:

tdelta = datetime.timedelta(days=7)
print('Какая дата будет через 7 дней:', tday + tdelta)

bday = datetime.date(tday.year, 10, 2)
till_bday = bday - tday
print('До дня рождения осталось', till_bday.days, 'дней')
print('До дня рождения осталось', till_bday.total_seconds(), 'секунд')


t = datetime.time(9, 30, 45)
'''Только время. Можно дополнительно добавить миллисекунды'''
d = datetime.date(2021, 5, 21)
'''Только дата'''
dt = datetime.datetime(2021, 5, 21, 9, 30, 45)
'''И дата, и время'''

print(dt.time())
'''Достает time из datetime'''


import pytz
'''Дает информацию о временных зонах. Рекомендован в документации datetime'''


def tz():
    '''Показывает все доступные временные зоны'''
    for tz in pytz.all_timezones:
        print(tz)


dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
dt_mtn = dt_utcnow.astimezone((pytz.timezone('US/Mountain')))
print(dt_mtn)