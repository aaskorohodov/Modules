'''
Lock — это объект, который действует как коридор в зал. Только один поток за раз может использовать Lock. Любой другой
поток, который захочет использовать Lock, должен ждать, пока текущий владелец Lock не откажется от нее.
Основными функциями для этого являются .acquire() и .release()

Но, если один поток вызвал блокировку и не вернул ее, а второй поток ждет своей очереди, то все зависнет. Чтобы не забыть
разблокироваться, можно использовать менеджер контекста, который все сделает сам (with). Менеджер контекста умеет сам
ставить и снимать блокировку, ничего дополнительного писать не требуется.
'''
import concurrent.futures
import threading
import time


class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def locked_update(self, name):
        print(f"Thread {name}: starting update")
        print(f"Thread {name} about to lock")
        with self._lock:
            # with сам выполняет блокировку, ничего делать не требуется

            print(f"Thread {name} has lock")
            local_copy = self.value
            local_copy += 1
            time.sleep(1)
            self.value = local_copy
            print(f"Thread {name} about to release lock")
            # а после себя он сам снимает блокировку. Именно после этой строчки, второй поток продолжает работу

        print(f"Thread {name} after release")
        print(f"Thread {name}: finishing update")


if __name__ == "__main__":
    database = FakeDatabase()
    print(f"Testing update. Starting value is {database.value}.")

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.locked_update, index)

    print(f"Testing update. Ending value is {database.value}.")