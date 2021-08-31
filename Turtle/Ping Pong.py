import random
import time
import turtle
from turtle import *


FONT = ('Arial', 44)


class Rockets(Turtle):
    def __init__(self, posit):
        super().__init__()
        self.speed(3)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(posit, 0)
        self.bot_speed = 1

    def move_up(self):
        y = self.ycor() + 10
        if y > 350:
            y = 350
        self.sety(y)

    def move_down(self):
        y = self.ycor() - 10
        if y < -350:
            y = -350
        self.sety(y)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.dx = random.choice([-1.5, 1.5])
        self.dy = random.choice([-1, 1])
        self.penup()
        self.ball_speed = self.dx


class Count(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.color('white')
        self.penup()
        self.hideturtle()


def start_game():
    window = turtle.Screen()
    window.title('Ping-Pong')
    window.setup(width=1.0, height=1.0)
    window.bgcolor('black')

    def board():
        board = turtle.Turtle()
        board.speed(0)
        board.hideturtle()
        board.color('green')
        board.pensize(1)
        board.up()
        board.goto(700, 400)
        board.down()
        board.begin_fill()
        board.goto(700, -400)
        board.goto(-700, -400)
        board.goto(-700, 400)
        board.goto(700, 400)
        board.end_fill()

    def net():
        net = turtle.Turtle()
        net.speed(5)
        net.shape('turtle')
        net.color('white')
        net.pensize(5)
        net.penup()
        net.goto(0, 400)
        net.pendown()
        net.right(90)
        for i in range(25):
            if i % 2 == 0:
                net.forward(32)
            else:
                net.penup()
                net.forward(32)
                net.pendown()
        net.hideturtle()

    def make_rockets(num):
        player = Rockets(num)
        return player

    def make_ball():
        ball = Ball()
        return ball

    def make_count():
        p1 = Count()
        p1.setposition(-500, 400)
        p1.write(p1.count, font=FONT)
        p2 = Count()
        p2.setposition(500, 400)
        p2.write(p1.count, font=FONT)
        time.sleep(1)
        return p1, p2

    board()
    net()
    player = make_rockets(700)
    bot = make_rockets(-700)
    ball = make_ball()
    p1, p2 = make_count()

    return window, player, bot, ball, p1, p2


window, player, bot, ball, p1, p2 = start_game()
window.tracer(2)
window.listen()
window.onkeypress(player.move_up, "Up")
window.onkeypress(player.move_down, "Down")


def score():
    p1.clear()
    p2.clear()
    p1.write(p1.count, font=FONT)
    p2.write(p2.count, font=FONT)


def player_fail(stat=None):
    ball.dy = 0
    ball.dx = 0
    if stat is None:
        for i in range(3):
            ball.color('red')
            window.bgcolor('yellow')
            time.sleep(0.1)
            ball.color('white')
            window.bgcolor('black')
            time.sleep(0.1)
    ball.speed(5)
    ball.goto(0, 0)
    ball.speed(0)
    score()
    ball.dy = random.random() * random.choice([-1, 1])
    ball.dx = ball.ball_speed * random.choice([-1, 1])


class Wow(Turtle):
    def __init__(self):
        shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
        super().__init__()
        self.init_hight = random.choice([i for i in range(-300, 700)])
        self.init_space = random.choice([i for i in range(-800, 800)])
        self.hideturtle()
        self.shape(random.choice(shapes))
        self.up()
        self.grav = random.randint(1, 30)
        self.y_speed = 0
        self.x_speed = random.random() * random.choice([-1, 1])
        self.goto(self.init_space, self.init_hight)
        self.colour_random()
        self.showturtle()
        self.angle = random.randint(-5, 5)

    def colour_random(self):
        r = random.random()
        g = random.random()
        b = random.random()
        self.color(r,g,b)


def wow():
    window.tracer(20)
    wows = []
    for i in range(30):
        wow = Wow()
        wows.append(wow)

    for i in range(150):
        for wow in wows:
            wow.left(wow.angle)
            wow.y_speed = wow.y_speed - wow.grav
            wow.goto(wow.xcor() + wow.x_speed, wow.ycor() + wow.y_speed)

    window.tracer(2)


while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 395:
        ball.dy = -ball.dy
    elif ball.ycor() <= -395:
        ball.dy = -ball.dy
    elif ball.xcor() >= 700:
        p1.count += 1
        player_fail()
        bot.bot_speed -= 0.3
        ball.ball_speed -= 0.4
    elif ball.xcor() <= -700:
        p2.count += 1
        player_fail('victory')
        bot.bot_speed += 0.5
        ball.ball_speed += 0.7
        wow()
    if player.ycor() - 50 <= ball.ycor() <= player.ycor() + 50 and player.xcor() - 10 <= ball.xcor() <= player.xcor() + 10:
        ball.dx = -ball.dx * 1.05
        if player.ycor() < ball.ycor():
            distance = ball.distance(player)
            ball.dy = (distance / 40)
        elif player.ycor() > ball.ycor():
            distance = ball.distance(player)
            ball.dy = (distance / 40) * -1
    if bot.ycor() - 50 <= ball.ycor() <= bot.ycor() + 50 and bot.xcor() - 10 <= ball.xcor() <= bot.xcor() + 10:
        ball.dx = -ball.dx * 1.05
        ball.dy = random.random() * random.choice([1, -1])

    if ball.xcor() <= 0:
        if bot.ycor() < ball.ycor():
            bot.goto(bot.xcor(), bot.ycor() + bot.bot_speed)
        elif bot.ycor() > ball.ycor():
            bot.goto(bot.xcor(), bot.ycor() - bot.bot_speed)
