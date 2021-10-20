from jinja2 import Template, escape

'''Выполняется с помощью блоков {% raw %} … {% endraw %}'''

data = '''{% raw %}Модуль Jinja вместо
определения {{ name }}
подставляет соответствующее значение{% endraw %}'''

tm = Template(data)
msg = tm.render(name='Федор')

print(msg)


# экранирование html тегов (применяется, если нужно вывести тег текстом)

link = '''В HTML-документе ссылки определяются так: 
<a href="#">Ссылка</a>'''

link = '''В HTML-документе ссылки определяются так: 
<a href="#">Ссылка</a>'''

print(escape(link))