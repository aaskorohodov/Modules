import random
import turtle
from turtle import *


def drawBorder():
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
ball = turtle.Turtle()
ball.hideturtle()
ball.shape('circle')
ball.up()
ball.goto(random.randint(-295, 295), random.randint(-295, 295))
ball.showturtle()
ball.speed(100)
dx = 3
dy = 2



while True:
    x, y = ball.position()
    if x >= 295 or x <= -295:
        dx = -dx
    if y >= 295 or y <= -295:
        dy = -dy
    ball.goto(x + dx, y + dy)
