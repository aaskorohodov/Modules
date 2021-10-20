from jinja2 import Template


'''
{% call[(параметры)] <вызов макроса> %}
<вложенный шаблон>
{% endcall %}

Предположим, мы хотим сделать вот такой список списков:
<ul>
<li>Алексей 
    <ul>
    <li>age: 
    <li>weight: 78.5
    </ul>
<li>Николай 
    <ul>
    <li>age: 
    <li>weight: 82.3
    </ul>
<li>Иван 
    <ul>
    <li>age: 
    <li>weight: 94.0
    </ul>
</ul>


–Алексей 
    –age: 
    –weight: 78.5
–Николай 
    –age: 
    –weight: 82.3
–Иван 
    –age: 
    –weight: 94.0
    
Сначала сделаем просто список с именами

–Алексей 
–Николай 
–Иван

'''


persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0}
]

'''
Делаем macro, придумываем ему имя list_users, которое будет принимать какую-то переменную (users, но можно хоть x).
Оно сделает <ul>, переберет словарь users (передадим его ниже), возьмет оттуда значение по ключу name.
Затем вызываем это macro {{list_users(users)}}, передавая ему users
'''

html = '''
{% macro list_users(users) -%}
<ul>
{% for u in users -%}
    <li>{{u.name}} 
{%- endfor %}
</ul>
{%- endmacro %}

{{list_users(users)}}
'''

tm = Template(html)
msg = tm.render(users=persons)

print(msg)





'''
Теперь делаем все аналогично, только внутри for вкладываем caller, который сделает вложенные списки. Как оно работает,
а точнее как вызывает я хз, слишком запутано.
'''

html = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{u.name}} {{caller(u)}}
{%- endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
    <li>age: {{user.old}}
    <li>weight: {{user.weight}}
    </ul>
{% endcall -%}
'''

tm = Template(html)
msg = tm.render(users=persons)

print(msg)