'''
count()             подсчет количества чего-либо
sum()               считает сумму указанного поля (например, если в поле число, то сложит все числа из полей)
avr()               считает среднее в выбранных полях
min() max()         ищет минимальное и максимальное значение в найденных полях


SELECT count(user_id) FROM table WHERE ...
*count ведет подсчет найденных записей и выводит таблицу с единственной строкой, где стоит посчитанное число чего-то

В результирующей таблице можно менять имена полей:
SELECT count(user_id) as blabla

'''