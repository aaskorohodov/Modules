import random
import turtle
from turtle import *

'''
balls_in_game =                     число мячей в игре
window = turtle.Screen()            создает переменную, для манипуляции окном приложения
window.tracer(balls_in_game * 2)    задает скорость анимации (вдвое выше, чем число мячей ~ норм)
speed = 5                           переменная для управления скоростью игрока
balls_catched = 0                   число пойманных мячей
catched_dy = 0                      место для хранения пойманных мячей по y
catched_dx = 330                    место для хранения пойманных мячей по x
'''


balls_in_game = 100
window = turtle.Screen()
window.tracer(balls_in_game * 2)
speed = 5
balls_catched = 0
catched_dy = 0
catched_dx = 330


def drawBorder():
    '''Рисует границу, в которой проходит игра. Ни на что не влияет, просто отрисовка границы в вакууме'''
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
balls = []  # список всех мячей, хранит экземпляры класса, ниже пригодится

class Balls(Turtle):
    '''Класс мячей (кроме игрока).
    dx = доступный шаг по x, dy = доступный шаг по y. Шаг = на сколько мяч может сместиться вверх и в сторону.
    rgb = цвет мяча
    super = атрибут, который отличает бото-мячи от игрока (0=бот, 1=игрок)
    '''
    def __init__(self):
        super().__init__()
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        r = random.random()
        g = random.random()
        b = random.random()
        self.color(r, g, b)
        self.super = 0

    def changeColour(self):
        '''Метод смены увета мяча. Выбирает цвет рандомно'''
        r = random.random()
        g = random.random()
        b = random.random()
        self.color(r, g, b)


for i in range(balls_in_game):
    '''Создает мячи. Мяч создается в центре экрана, прячется, меняет форму на круг, поднимает перо (он умеет рисовать),
    идет на рандомные координаты, снвоа становится видимым, заносится в список'''
    ball = Balls()
    ball.hideturtle()
    ball.shape('circle')
    ball.up()
    ball.goto(random.randint(-280, 280), random.randint(-280, 280))
    ball.showturtle()
    balls.append(ball)


class SuperBall(Turtle):
    '''Создает игрока. Все очень похоже на бото-мяч, только еще хранит переменные x,y (позиция), это потом пригодится.
    dx и dy нужны, чтобы использовать идентичную логику коллизий ниже.'''
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.up()
        self.dx = 0
        self.dy = 0
        self.super = 1
        self.x, self.y = self.position()

    def changeColour(self):
        '''Нужно, чтобы использовать идентичную логику смены цвета. Ничего не делает.'''
        pass

    def moveUp(self):
        '''Двигает мяч вверх'''
        x, y = self.position()  # создаем две переменные, в которые записываем текущую позицию курсора на экране
        self.setposition(x, y+speed)  # меняем позицию, увеличивая значение одной переменной на speed

    def moveDown(self):
        x, y = self.position()
        self.setposition(x, y-speed)

    def moveLeft(self):
        x, y = self.position()
        self.setposition(x-speed, y)

    def moveRight(self):
        x, y = self.position()
        self.setposition(x+speed, y)

    def speedUp(self):
        '''Увеличиает скорость, меняя переменную speed'''
        global speed
        speed += 5

    def speedDown(self):
        global speed
        if speed == 5:
            pass
        else:
            speed -= 5


me = SuperBall()  # создание игрока, чуть ниже игрок также идет в общий список.
balls.append(me)

'''Все ниже нужно, чтобы отслеживать нажатия на кнопки. Аргументы = что вызвать и по какой кнопке'''
window.onkey(me.moveUp, 'Up')
window.onkey(me.moveDown, 'Down')
window.onkey(me.moveLeft, 'Left')
window.onkey(me.moveRight, 'Right')
window.onkey(me.speedUp, '+')
window.onkey(me.speedDown, '-')
window.listen()  # это чтобы отслеживать любое нажатие, само слежение за нажатиями


def catch(num):
    '''Отправляет пойманные мячи в бок экрана. Кладет друг над другом, если место заканчивается, смещается чуть вбок'''
    global catched_dy, catched_dx
    balls[num].goto(catched_dx, 0 + catched_dy)
    balls[num].dx = 0
    balls[num].dy = 0
    catched_dy += 30
    if catched_dy >= 330:
        catched_dx += 30
        catched_dy = 0


while True:
    '''Основной цикл игры, держит мячи внутри поля, делает коллизии, меняет цвета и все прочее.'''
    me.x, me.y = me.position()  # переменные для отслеживания игрока на поле, чтоб не залазил за края
    window.update()  # делает анимацию чуть плавнее, принудительно обновляя экран на каждом шаге цикла
    for ball in balls:
        '''Следит, чтобы мячи не ушли за края. Если их координаты больше заданых, то меняет dx и dy yа противоположные, 
        и меняет цвет. dx = delta x, это значение, на которое нужно сместить мяч при каждом проходе цикла.
        В последней строчке видно, что это значение просто плюсуется к текущему и мяч направляется в эту точку.'''
        x, y = ball.position()
        if x >= 290 or x <= -290:
            ball.dx *= -1
            ball.changeColour()
        elif y >= 290 or y <= -290:
            ball.dy *= -1
            ball.changeColour()
        ball.goto(x + ball.dx, y + ball.dy)

    '''
    Это цикл для отслеживания столкновений (коллизий) между мячами и для отслеживания ловли игроком мячей-ботов.
    Первой строчкой обходятся все мячи, для каждого мяча проверяются все другие мячи. Я украл первые 2 строчки с
    одного канала и не совсем понимаю, как они работают.
    4 первые условия смотрят, как мячи летят друг в друга, чтобы отлетать физически корректно. Это сложно объяснить,
    но если вы бросаете мяч в стену под углом, то он продолжает лететь "вперед", но отлетает от стены в то же время.
    Дальше проверяется, не столкнулся ли игрок с ботом, по атрибуту super. Если это случилось, то вызывается функция.
    Затем проверяется, что игрок не заполз за края экрана, а если заполз, то его бросает в центр (такая кара).
    Последнее условие – разворот мяча, это ситуация коллизии лоб в лоб.
    Затем меняется цвет мяча (это происходит при коллизии).
    '''
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
                elif balls[i].super == 0 and balls[j].super == 1:
                    catch(i)
                elif balls[j].super == 0 and balls[i].super == 1:
                    catch(j)
                elif me.x not in range(-300, 300) or me.y not in range(-300, 300):
                    me.goto(0,0)
                else:
                    balls[i].dx *= -1
                    balls[i].dy *= -1
                    balls[j].dx *= -1
                    balls[j].dy *= -1
                balls[i].changeColour()
                balls[j].changeColour()

