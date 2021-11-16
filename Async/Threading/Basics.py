'''
Стандартная библиотека Python предоставляет библиотеку threading, которая содержит необходимые классы
для работы с потоками. Основной класс в этой библиотеки – Thread.
Чтобы запустить отдельный поток, нужно создать экземпляр потока Thread и затем запустить его с помощью метода .start():

    x = threading.Thread(target=thread_function, args=(1,))

Thread просит имя функции (target=thread_function), а также аргументы для нее в виде итератора (можно передать и список)

По умолчанию запускается не демонический поток, то есть такой поток, который нельзя убить, пока он не завершиться.
Чтобы изменить поток на демонический, нужно поставить daemon=True:

    x = threading.Thread(target=thread_function, args=(1,), daemon=True)

В этом случае, main не будет ждать таймер sleep и сразу завершиться. Но, если поставить на Thread .join(), то поток
придется подождать, будь он демоническим или нет.

'''


import logging
import threading
import time


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")

    '''Создается поток, ему нужно указать имя функции и передать аргумент'''
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)

    logging.info("Main    : before running thread")

    '''Запускаем поток'''
    x.start()
    logging.info("Main    : wait for the thread to finish")
    x.join()
    logging.info("Main    : all done")