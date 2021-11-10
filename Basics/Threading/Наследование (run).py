'''Можно делать классы-наследники от Thread, и запускать в них методы в качестве потоков. Для этого надо переопределить
run().'''



from threading import Thread
from time import sleep


class CustomThread(Thread):
    def __init__(self, id, limit, waiting):  # аргументы тут опциональны и для красоты
        Thread.__init__(self)
        self._limit = limit
        self.waiting = waiting
        self.id = id

    def run(self):
        for i in range(self._limit):
            print(f"from CustomThread {self.id}: {i}")
            sleep(self.waiting)


cth = CustomThread(1, 3, 1)
cth2 = CustomThread(2, 3, 1)
cth.start()
cth2.start()