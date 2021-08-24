import datetime
import pyglet
from time import sleep

music = pyglet.resource.media('03-saga_of_the_low_down_let_down.mp3')
time_now = datetime.datetime.now()

print(time_now)

print('День')
day = str(input())
print('Час')
hour = str(input())
print('Минуты')
minutes = str(input())

if len(day) == 1:
    day = '0' + day
if len(hour) == 1:
    hour = '0' + hour
if len(minutes) == 1:
    minutes = '0' + minutes

while True:
    time_now = datetime.datetime.now()
    if str(time_now.hour) == hour and str(time_now.minute) == minutes and str(time_now.day) == day:
        music.play()
        break
    sleep(1)
pyglet.app.run()