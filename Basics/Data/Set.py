'''Множество - это изменяемый неупорядоченный тип данных. В множестве всегда содержатся только уникальные элементы.
С его помощью можно удалять повторы в списке'''

lis = [1,1,1,2,3,4,5]
st = set(lis)
print(st)


# Варианты создания множества

my_set = set() # empty
my_set = set('long string, that will be reduced to unique literals')
my_set = set(lis)


# операции с множествами

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = set1.union(set2)
print(set3)

set4 = set1 | set2  # same as union, but with simbol |
print(set4)
# generally, it all works like U would expect



# ПОЛЕЗНЫЕ МТОДЫ

# Метод add() добавляет элемент во множество:

set4.add('asd')
print(set4)

# Метод discard() позволяет удалять элементы, не выдавая ошибку, если элемента в множестве нет:

set4.discard('aaaaaa')
set4.discard('asd')
print(set4)