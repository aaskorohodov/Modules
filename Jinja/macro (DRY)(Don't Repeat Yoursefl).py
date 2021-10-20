from jinja2 import Template


'''
macro = ключевое слово Джинджи
input после macro = имя этого макро-определения. По нму его потом можно вызвать, примерно как функцию
value="{{ value|e }}" – |e это экранирование
В открывающей части выражения, мы передаем переменные (name, value='', type='text', size=20), часть из них имеют
значение по умолчанию, name не имеет. Поэтому ниже (3 поля) мы передаем только name
'''

html = '''
{% macro input(name, value='', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
{%- endmacro %}

{{ input('username') }}
{{ input('email') }}
{{ input('password') }}
'''

tm = Template(html)
msq = tm.render()

print(msq)