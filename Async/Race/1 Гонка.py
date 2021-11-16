'''
Условия гонки могут возникать, когда два или более потока обращаются к общему фрагменту данных или ресурсу.

Ниже пример, в котором класс FakeDatabase имитирует базу данных. В экземпляре класса будет 1 значение (value), которое
инициируется в 0. Метод update записывает это значение в переменную local_copy, добавляет туда 1, спит 1 секунду и
записывает 1 обратно в экземпляр класса.

Если запустить 2 и более потоков (что делает if ниже), то каждый поток сначала прочитает исходное значение экземпляра
(а он один на все потоки и там будет 0), потом каждый поток прибавить единицу к нулю, потом каждый поток запишет 1 в
экземпляр класса, переписывая сначала 0 на 1, потом 1 на 1, потом 1 на 1, ... То есть потоки работают бессмысленно.
'''
import concurrent.futures
import time


class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self, name):
        print(f"Thread {name}: starting update")
        local_copy = self.value
        local_copy += 1
        time.sleep(1)
        self.value = local_copy
        print(f"Thread {name}: finishing update\n")


if __name__ == "__main__":
    database = FakeDatabase()
    print(f"Testing update. Starting value is {database.value}.")

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)

    print(f"Testing update. Ending value is {database.value}.")