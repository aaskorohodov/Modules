import random
import time
import turtle
from turtle import *
import pygame


pygame.mixer.init()
hit = pygame.mixer.Sound('sounds/hit.mp3')
fail = pygame.mixer.Sound('sounds/fail.mp3')
score_sound = pygame.mixer.Sound('sounds/score.mp3')
super_hit_sound = pygame.mixer.Sound('sounds/super_hit.mp3')
super_power = pygame.mixer.Sound('sounds/super_power.mp3')
victory = pygame.mixer.Sound('sounds/victory.mp3')
wall_hit = pygame.mixer.Sound('sounds/wall_hit.mp3')
freeze = pygame.mixer.Sound('sounds/freeze.mp3')

FONT = ('Arial', 44)
super_hit = 0


class Rockets(Turtle):
    def __init__(self, posit):
        super().__init__()
        self.speed(2)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(posit, 0)
        self.bot_speed = 1
        self.freeze = 0

    def move_up(self):
        y = self.ycor() + 20
        if y > 350:
            y = 350
        self.sety(y)

    def move_down(self):
        y = self.ycor() - 20
        if y < -350:
            y = -350
        self.sety(y)

    def super_hit(self):
        global super_hit
        self.color('red')
        super_hit = 1
        super_power.play()

    def freeze_hit(self):
        global super_hit
        self.freeze = 1
        self.color('blue')
        freeze.play()
        super_hit = 0


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.dx = random.choice([-2, 2])
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
    player = make_rockets(650)
    bot = make_rockets(-650)
    ball = make_ball()
    p1, p2 = make_count()

    return window, player, bot, ball, p1, p2


window, player, bot, ball, p1, p2 = start_game()
window.tracer(10)
window.listen()
window.onkeypress(player.move_up, "Up")
window.onkeypress(player.move_down, "Down")
window.onkeypress(player.super_hit, "space")
window.onkeypress(player.freeze_hit, "w")


def score():
    p1.clear()
    p2.clear()
    score_sound.play()
    p1.write(p1.count, font=FONT)
    p2.write(p2.count, font=FONT)


def player_fail(stat=None):
    ball.dy = 0
    ball.dx = 0
    if stat is None:
        for i in range(3):
            fail.play()
            ball.color('red')
            window.bgcolor('yellow')
            time.sleep(0.1)
            ball.color('white')
            window.bgcolor('black')
            time.sleep(0.1)
    time.sleep(1)
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
    victory.play()
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

    window.tracer(10)


while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 395:
        ball.dy = -ball.dy
        wall_hit.play()
    elif ball.ycor() <= -395:
        ball.dy = -ball.dy
        wall_hit.play()
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
    if player.ycor() - 50 <= ball.ycor() <= player.ycor() + 50 and player.xcor() - 10 <= ball.xcor() <= player.xcor() + 30:
        if super_hit == 0 and player.freeze == 0:
            ball.dx = -ball.dx * 1.1
            hit.play()
        elif player.freeze == 1 and super_hit == 0:
            ball.dx = -ball.dx / 3
            player.color('white')
            hit.play()
        else:
            ball.dx = -ball.dx * 3
            super_hit = 0
            player.color('white')
            super_hit_sound.play()
        if player.ycor() < ball.ycor():
            distance = ball.distance(player)
            ball.dy = (distance / 30)
        elif player.ycor() > ball.ycor():
            distance = ball.distance(player)
            ball.dy = (distance / 30) * -1
    if bot.ycor() - 50 <= ball.ycor() <= bot.ycor() + 50 and bot.xcor() - 30 <= ball.xcor() <= bot.xcor() + 10:
        ball.dx = -ball.dx * 1.1
        hit.play()
        ball.dy = random.random() * random.choice([1, -1])

    if ball.xcor() <= 0:
        if bot.ycor() < ball.ycor():
            bot.goto(bot.xcor(), bot.ycor() + bot.bot_speed)
        elif bot.ycor() > ball.ycor():
            bot.goto(bot.xcor(), bot.ycor() - bot.bot_speed)
