import random
import turtle
from turtle import *
'''Тут можно рисовать клавиатурой, использую черепашку как курсор'''


speed = 5  # это переменная, для управления скоростью черепашки


class Pen(Turtle):
    '''Этот класс создан, чтобы положить разные функции в одно место'''

    def moveUp(self):
        '''Двигает черепашку вверх'''
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

    def draw(self):
        '''Дает возможность двигать курсор и не рисовать (поднять карандаш). Для этого проверяется и меняется
        внешний вид курсора'''
        if self.shape() == 'classic':  # если курсор классический, то поднять карандаш и изменить курсор на другой
            self.up()
            self.shape('arrow')
        else:
            self.down()
            self.shape('classic')

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

    def randomColor(self):
        '''Задает черепашке рандомный цвет'''
        r = random.random()
        g = random.random()
        b = random.random()
        self.color(r,g,b)


pen = Pen()
window = turtle.Screen()


def bgColor():
    '''Задает экрану рандомный цвет'''
    r = random.random()
    g = random.random()
    b = random.random()
    window.bgcolor(r, g, b)


'''Ниже для объекта экран вызывается метод onkey. В него надо передать имя функции или метода, а также название кнопки.
По нажатию на эту кнопку, будет вызываться функция или метод'''
window.onkey(pen.moveUp, 'Up')
window.onkey(pen.moveDown, 'Down')
window.onkey(pen.moveLeft, 'Left')
window.onkey(pen.moveRight, 'Right')
window.onkey(pen.draw, 'space')
window.onkey(pen.speedUp, '+')
window.onkey(pen.speedDown, '-')
window.onkey(pen.randomColor, 'r')
window.onkey(bgColor, 'b')


window.listen()  # Ждет ввод от пользователя (ответ на разные кнопки)
window.mainloop()  # Один из способов не дать окну закрыться
