'''
Объекты Lock не блокируют что-то конкретное, наоборот – поток обращается к Lock, блокирует его, и пока Lock заблокирован
(acquire), другой поток не может получить доступ к этому-же объекту Lock.

Ниже пример, когда 2 потока используют 2 блока, дико сложно блокируя друг друга в нужные моменты и в нужном месте.
'''



import concurrent.futures
import random
import threading
import time

SENTINEL = object()


def producer(pipeline):
    """Pretend we're getting a message from the network."""
    for index in range(10):
        message = random.randint(1, 101)
        print(f"Producer got message: {message}\n")
        pipeline.set_message(message, "Producer")
    # Send a sentinel message to tell consumer we're done
    pipeline.set_message(SENTINEL, "Producer")


def consumer(pipeline):
    """ Pretend we're saving a number in the database. """
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message("Consumer")
        if message is not SENTINEL:
            print(f"Consumer storing message: {message}\n")



class Pipeline:
    '''Представляет трубу, по которой происходит обмен данными'''
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def get_message(self, name):
        print(f"{name}:about to acquire getlock\n")
        self.consumer_lock.acquire()
        print(f"{name}:have getlock\n")
        message = self.message
        print(f"{name}:about to release setlock\n")
        self.producer_lock.release()
        print(f"{name}:setlock released\n")
        return message

    def set_message(self, message, name):
        print(f"{name}:about to acquire setlock\n")
        self.producer_lock.acquire()
        print(f"{name}:have setlock\n")
        self.message = message
        print(f"{name}:about to release getlock\n")
        self.consumer_lock.release()
        print(f"{name}:getlock released\n")



if __name__ == "__main__":
    pipeline = Pipeline()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)