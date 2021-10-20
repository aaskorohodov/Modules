from jinja2 import Template


'''Что происходит: суммируем цену автомобилей'''

cars = [
    {'model': 'Ауди', 'price': 23000},
    {'model': 'Шкода', 'price': 17300},
    {'model': 'Вольво', 'price': 44300},
    {'model': 'Фольксваген', 'price': 21300}
]

'''В {} указываем откуда берем (cs, который объявляется ниже), затем через | просим сложит поле price'''
# sum(iterable, attribute=None, start=0)
# iterable = итерируемый объект (тут его нет)
# attribute = что складываем
# start = не нужно ли что-то дополнительно прибавить к результату (начать с ... по умолчанию там ноль)

tpl = "Суммарная цена автомобилей {{ cs | sum(attribute='price') }}"
tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)


# просто суммируем список
dig = [1,2,3,4,5,6]
tpl = "Суммарная цена автомобилей {{ cs | sum }}"
tm = Template(tpl)
msg = tm.render(cs=dig)

print(msg)


# смотрим максимальное значение и видим словарь
tpl = "Суммарная цена автомобилей {{ cs | max(attribute='price') }}"
tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)

# смотрим максимальное значение и видим только самую дорогую модель
tpl = "Суммарная цена автомобилей {{ (cs | max(attribute='price')).model }}"
tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)

# аналогично, только min
tpl = "Суммарная цена автомобилей {{ (cs | min(attribute='price')).model }}"
tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)


# рандом
tpl = "Суммарная цена автомобилей {{ (cs | random).model }}"
tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)


# замена
tpl = "Суммарная цена автомобилей {{ cs | replace('о', 'О') }}"
tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)



# блок фильтра

persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0}
]

tpl = '''
{%- for u in users -%}
{% filter upper %}{{u.name}}{% endfilter %}
{% endfor -%}
'''

tm = Template(tpl)
msg = tm.render(users=persons)

print(msg)