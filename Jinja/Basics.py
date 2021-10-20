from jinja2 import Template

a = "Федор"  # это будет подставлять

tm = Template("Привет {{ name }}")  # ставим на место {{ name }}
msg = tm.render(name=a)

print(msg)

'''
{% %} – спецификатор шаблона;
{{ }} – выражение для вставки конструкций Python в шаблон;
{# #} – блок комментариев;
# ## – строковый комментарий.
'''

name = 'Федор'
age = 28
tm = Template('Меня зовут {{ name.upper() }}, мне {{ age*2 }} лет')  # позволяет работать методам питона
msq = tm.render(name=name, age=age)
print(msq)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

per = Person("Федор", 33)

tm = Template("Мне {{p.age}} лет и зовут {{ p.name }}.")  # передаются атрибуты экземпляра
print(tm.render(p=per))  # объявляется экземпляр класса
