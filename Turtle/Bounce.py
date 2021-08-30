import random
import turtle
from turtle import *


def drawBorder():
    '''Рисует границу, в которой будет летать мячик. Никаких секретов'''
    border = turtle.Turtle()
    border.speed(0)
    border.hideturtle()
    border.color('red')
    border.up()
    border.pensize(5)
    border.goto(300, 300)
    border.down()
    border.goto(300, -300)
    border.goto(-300, -300)
    border.goto(-300, 300)
    border.goto(300, 300)


drawBorder()

'''Далее:
1. Создается мяч
2. Мяч прячется
3. Мяч меняет форму на круг (по умолчанию он стрелка)
4. Мяч поднимает перо (чтобы не оставлять линию)
5. Мяч идет в рандомные координаты
6. Мяч становится опять видимым
7. мяч повышает скорость (0=мгновенно)
'''
ball = turtle.Turtle()
ball.hideturtle()
ball.shape('circle')
ball.up()
ball.goto(random.randint(-295, 295), random.randint(-295, 295))
ball.showturtle()
ball.speed(0)

'''dx, dy – дельта x и y, это шаг мяча, на сколько пикселей он сдвинется
Затем идет бесконечный цикл, в нем записываем положение мяча в x y, условиями смотрим, чтобы мяч не вышел за края рамки.
Если выходит, то меняем дельту на противоположный знак (dx=-dx, dy=-dy) – тут неважен начальный знак, он просто меняется
на противоположный (минус на минус дает плюс, плюс на минус дает минус).
Затем мяч смешается (goto) на дельту. Готово. 
'''
dx = 3
dy = 2

while True:
    x, y = ball.position()
    if x >= 295 or x <= -295:
        dx = -dx
    if y >= 295 or y <= -295:
        dy = -dy
    ball.goto(x + dx, y + dy)
