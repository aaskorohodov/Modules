'''Если поток нужно прервать, то можно сделать это с помощью какой-то переменной, которую поток будет проверять'''


from threading import Thread, Lock
from time import sleep


lock = Lock()
stop_thread = False


def infinit_worker():
    print("Start infinit_worker()")
    while True:
        print("--> thread work")

        if stop_thread is True:
           break

        sleep(0.5)

    print("Stop infinit_worker()")


th = Thread(target=infinit_worker)
th.start()

sleep(1)
stop_thread = True
