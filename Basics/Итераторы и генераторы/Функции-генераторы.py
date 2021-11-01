'''
Функции-генераторы возвращает объект-генератор. Делаются с помощью yield:
'''

def GetAllAverage(n):
    count = 0
    S = 0
    for i in range(1, n+1):
        count += 1
        S += 1
        yield S/count

'''
При каждом вызове этой функции вернется генератор, его можно прочитать с помощью next():
'''

def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygenerator = createGenerator() # создаём генератор

for i in mygenerator:
    print(i)