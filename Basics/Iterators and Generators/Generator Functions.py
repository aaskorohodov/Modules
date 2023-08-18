"""Generator functions return a generator object. Are done with yield:"""


def get_all_average(n):
    count = 0
    s = 0
    for i in range(1, n+1):
        count += 1
        s += 1
        yield s/count
# Each time this function is called, a generator will be returned, which can be read with next():


def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i*i


my_generator = create_generator()  # Creating a generator

for x in my_generator:
    print(x)
