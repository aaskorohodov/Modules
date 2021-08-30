import random
import turtle
from turtle import *

window = turtle.Screen()
window.tracer(20)


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
    window.update()


drawBorder()

balls = []

class Balls(Turtle):
    def __init__(self):
        super().__init__()
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        r = random.random()
        g = random.random()
        b = random.random()
        self.color(r, g, b)

    def changeColour(self):
        r = random.random()
        g = random.random()
        b = random.random()
        self.color(r, g, b)


for i in range(20):
    ball = Balls()
    ball.hideturtle()
    ball.shape('circle')
    ball.up()
    ball.goto(random.randint(-280, 280), random.randint(-280, 280))
    ball.showturtle()
    balls.append(ball)


while True:
    window.update()
    for ball in balls:
        x, y = ball.position()
        if x >= 290 or x <= -290:
            ball.dx *= -1
            ball.changeColour()
        elif y >= 290 or y <= -290:
            ball.dy *= -1
            ball.changeColour()
        ball.goto(x + ball.dx, y + ball.dy)

    for i in range(0, len(balls)):
        for j in range(i+1, len(balls)):
            if balls[i].distance(balls[j]) < 22:
                if balls[i].dy > 0 > balls[j].dy:
                    balls[i].dy *= -1
                    balls[j].dy *= -1
                elif balls[i].dy < 0 < balls[j].dy:
                    balls[i].dy *= -1
                    balls[j].dy *= -1
                elif balls[i].dx < 0 < balls[j].dx:
                    balls[i].dx *= -1
                    balls[j].dx *= -1
                elif balls[i].dx > 0 > balls[j].dx:
                    balls[i].dx *= -1
                    balls[j].dx *= -1
                else:
                    balls[i].dx *= -1
                    balls[i].dy *= -1
                    balls[j].dx *= -1
                    balls[j].dy *= -1
                balls[i].changeColour()
                balls[j].changeColour()

