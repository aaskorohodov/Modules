'''
Вот так можно уйти в зависание:

    l = threading.Lock()
    print("before first acquire")
    l.acquire()
    print("before second acquire")
    l.acquire()
    print("acquired lock twice")

Так как объект нельзя заблокировать дважды, то второй вызов блокировки будет ждать освобождения первого, что не случится.

'''
