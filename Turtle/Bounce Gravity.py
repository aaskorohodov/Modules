import random
import turtle
from turtle import *

'''Подробное описание базовых штук смотрите в Bounce2.py'''


window = turtle.Screen()
balls_in_game = 100
window.tracer(balls_in_game*6)

'''Ниже задаются формы для мячей и пустой список для их делегирования в основной цикл'''
shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
balls = []


class Ball(Turtle):
    '''
    Особенные атрибуты:
    init_hight = начальная высота мяча
    grav = гравитация, с которой мяч будет падать
    y/x_speed = скорость движения вбок и вверх
    max_speed = сюда единожды (при первом контакте с землей) записывается максимальная скорость
    angle = рандомный угол, с которым мяч будет крутиться
    first_touch = принимает 0, после первого контакта с землей становится 1. Нужно, чтобы записать max_speed 1 раз
    '''

    def __init__(self):
        super().__init__()
        self.init_hight = random.choice([i for i in range(50, 500)])
        self.hideturtle()
        self.shape(random.choice(shapes))
        self.up()
        self.grav = random.randint(1, 30) * 0.01
        self.y_speed = 0
        self.x_speed = random.random() * random.choice([-1, 1])
        self.goto(0, self.init_hight)
        self.colour_random()
        self.max_speed = 0
        self.showturtle()
        self.angle = random.randint(-5, 5)
        self.first_touch = 0

    def colour_random(self):
        r = random.random()
        g = random.random()
        b = random.random()
        self.color(r,g,b)


def start_the_game(num):
    def make_border():
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
        window.update()

    def make_balls(how_many):
        for i in range(how_many):
            ball = Ball()
            balls.append(ball)

    make_border()
    make_balls(num)


start_the_game(balls_in_game)

while True:
    window.update()
    for ball in balls:
        '''Считает скорость падения, плюсуя к ней гравитацию на каждом шаге цикла'''
        ball.left(ball.angle)
        ball.y_speed = ball.y_speed - ball.grav
        ball.goto(ball.xcor() + ball.x_speed, ball.ycor() + ball.y_speed)

        if ball.ycor() <= -290:
            '''Отрабатывает контакт с землей'''
            if ball.first_touch == 0:
                '''Это первый контакт, в нем записывается максимальная скорость, развитая конкретным мячом.
                Это нужно, чтобы мячи прыгали бесконечно долго, иначе скакание затухает со временем.
                Кроме этого, мяч ставится строго на координату -290, что ликвидирует залипание в границе.
                Движение разворачивается на противоположное (ball.y_speed *= -1)'''
                ball.max_speed = ball.y_speed * -1
                ball.sety(-290)
                ball.y_speed *= -1
                ball.first_touch = 1
            elif ball.first_touch == 1:
                '''Это отработка контакта, после первого. Тут аналогично, только для переворота направления
                используется ранее записанная max_speed'''
                ball.sety(-290)
                ball.y_speed = ball.max_speed
        elif ball.xcor() <= -290 or ball.xcor() >= 290:
            '''Все аналогично, только отрабатывается горизонтальная скорость, сохранение которой (max_speed)
             не требуется, так как проблем с затуханием не возникает (не видны)'''
            if ball.xcor() < 0:
                ball.setx(-290)
            else:
                ball.setx(290)
            ball.x_speed *= -1