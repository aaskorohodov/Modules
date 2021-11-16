'''Вызов функции в потоке делается через класс Thread. Он требует именованных параметров:
Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
    group – пока не используется, резерв под будующий функционал
    target – что вызывать
    name – имя потока
    args – аргументы для вызываемого объекта. В документации надо передавать кортеж, но можно список
    kwargs – неименованные аргументы, нужен словарь
    daemon – можно поставить True, тогда поток станет демоническим. По умолчанию наследует это значение от класса выше
'''


from threading import Thread
from time import sleep


def func(length):
    for i in range(5):
        print(f"from child thread: {i}")
        sleep(length)


th1 = Thread(target=func, args=[0.5])
th2 = Thread(target=func, args=(1,))
th1.start()
th2.start()