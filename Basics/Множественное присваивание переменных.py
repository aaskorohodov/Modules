# пример множественного присваивания. В первую переменную идут первой значение, во вторую все остальные (списком)
x, *y = 1,2,3,4,5,6
print(x, y)

# аналогично можно поковать кортеж, причем список можно сложить как в первую, так и во вторую переменную:
x,*y = (1,2,3,4)
print(x, y)

*x,y = (1,2,3,4)
print(x, y)

# строки:
*x, y, z = "Hello world!"
print(x, y, z)

# но так нельзя: *y = 1,2,3


# подобным образом можно распаковывать значения из списка:
a = [-5, 5] # это просто список из двух значений
# если распаковать его в подходящее место (где требуется именно 2 переменных), то все получится:

for x in range(*a): # тут нужен диапазон из двух значений, как раз столько есть в списке a = [-5, 5]
    print(x, end = " ")

print('\nпробел')

# распаковывать можно и сразу в range:
for x in range(*[-5, 5]):
    print(x, end=" ")