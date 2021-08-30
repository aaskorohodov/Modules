import random
import turtle
from turtle import *

'''
Общие сведения:
joe = turtle.Turtle() – создание объекта
joe.forward(100) – движение объекта
joe.left(90) – поворот объекта
joe.color('blue') – задает цвет рисования
joe.speed(10) – меняет скорость движения черепашки по экрану
joe.begin_fill() – начать заливку
joe.end_fill() – завершить заливку
    *имеет смысл начинать заливку, затем рисование фигуры, затем завершать заливку – так фигура будет залита внутри 

a = turtle.Screen() – создает объект "экран", ему можно задать цвет, например:
    a.bgcolor('black')
    или так: turtle.Screen().bgcolor('black')
    
done() – не дает окну закрыться, вызывая петлю в Tkinter, на котором работает turtle

Ниже приведены практические примеры, на основании класса – класс сделан, чтобы один раз создать объект,
напихать в класс методов по рисованию разных фигур, а затем вызывать методы. Класс наследуется от Turtle.
'''

class Turtles(Turtle):
    '''Класс наследуется от Turtle, чтобы создавать внутри себя функции фигур'''

    def __init__(self, speed=10):
        '''Инициализация класса, которая сразу увеличивает скорость'''
        super().__init__()
        self.speed(speed)

    def square(self, square_size=100):
        '''Рисует квадрат'''
        for i in range(4):
            self.forward(square_size)
            self.left(90)

    def many_squares(self, squares=2, square_size=100):
        '''Рисует много квадратов (квадраты внутри квадратов)'''
        for i in range(squares):
            for i in range(4):
                self.forward(square_size)
                self.left(90)
            square_size /= 1.2

    def spiral_square(self, squares=50, square_size=50, direction='r'):
        '''Рисует спираль из квадратов, с разноцветными сторонами'''
        colors = ['red', 'green', 'blue', 'yellow']
        speed_was = self.speed()  # запоминает текущую скорость черепашки, так как метод временно поднимет ее
        self.speed(150)
        for i in range(squares):
            for i in range (4):
                self.color(colors[i % 4])  # переопределяет цвет, поочередно выбирая его по индексу из списка [colors]
                self.forward(square_size)
                self.left(90)
            square_size +=5
            '''Далее выбирает направление спирали'''
            if direction == 'r':
                self.right(10)
            else:
                self.left(10)
        self.speed(speed_was)

    def spiral_circle(self, circles=50, radius=10):
        '''Рисует спираль из кругов'''
        speed_was = self.speed()
        self.speed(150)
        for i in range(circles):
            self.circle(radius)
            radius += 5
            self.left(10)
        self.speed(speed_was)

    def draw_triangle(self, size=100):
        for i in range(3):
            self.forward(size)
            self.left(120)

    def spiral_triangle(self, triangles=50, size=15):
        '''Рисует спираль из треугольников'''
        speed_was = self.speed()
        self.speed(150)
        for i in range(triangles):
            self.draw_triangle(size)
            self.left(10)
            size +=5
        self.speed(speed_was)

    def draw_any_polygon(self, sides, size=100):
        '''Рисует многоугольник из любого числа сторон.
        Может использоваться, чтобы нарисовать треугольник, квадрат, пятиугольник...'''
        turn = 360/sides
        for i in range(sides):
            self.forward(size)
            self.left(turn)

    def draw_many_polygons(self, poligons=10):
        poligon_sides = 3
        for i in range(poligons):
            self.draw_any_polygon(poligon_sides)
            poligon_sides += 1

    def draw_star(self, n=5, size=150):
        '''Рисует звезду с четным числом сторон, затем закрашивает ее'''
        if n % 2 == 0:
            print('Не могу нарисовать звезду, с четным числом зубьев')
        else:
            self.begin_fill()
            for i in range(n):
                self.forward(size)
                angle = n // 2 * 360 / n
                self.left(angle)
            self.end_fill()

    def turtle_return(self):
        '''Возвращает черепашку в середину экрана'''
        self.up()
        self,setposition(0, 0)
        self.down()

    def speed_up(self):
        self.speed(150)

    def speed_down(self):
        self.speed(5)

    def stars_in_sky(self):
        '''Рисует черное небо и звезды на нем'''
        self.speed_up()  # ускоряем черепашку
        self.color('yellow')  # задаем цвет черепашке
        turtle.Screen().bgcolor('black')  # задаем цвет фона
        turtle.Screen().setup(2000, 1000)  # задаем размер окна
        for i in range(40):
            '''Цикл определяет количество звезд на небе'''
            self.up()  # поднимаем карандаш, чтобы переместиться в другое место и не оставить след
            x = random.randrange(-1000, 1000, 1)  # выбираем рандомное число из этого диапазона (ширина экрана)
            y = random.randrange(-500, 500, 1)  # и еще раз (высота экрана)
            s = random.randrange(4, 30, 1)  # и еще раз (размер звезды)
            self.setposition(x, y)  # отправляем черепаху в рандомное место, которое выбрано 2 строчки выше
            self.down()  # ставим карандаш, чтобы начать рисовать звузду
            self.draw_star(random.choice([5,7,9,11,13,15]), s)  # рисуем звузду с рандомным числом конец и размером
            self.turtle_return()  # возвращаем черепаху в середину экрана, иначе она убежит далеко за пределы окна
        self.speed_down()  # в конце задаем низкую скорость, просто так, без смысла





joe = Turtles()
joe.stars_in_sky()




done()  # вызывает петлю в Tkinter, экран не закрывается