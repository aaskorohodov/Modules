'''
Include работает как конструктор страницы, он собирает из разных файлов одну страницу.
Есть 2 файла header и footer, мы хотим вставить их в какую-то страницу. Страницу пакуем в файл, вот такой:

{% include 'header.htm' %}
Содержимое страницы
{% include 'footer.htm' %}
'''

from jinja2 import FileSystemLoader, Environment


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('page.htm')
msg = tm.render()

#print(msg)

# *если хочется пропускать шаблоны, которых нет, а не получать ошибку, то можно так:
# {% include "header.html" ignore missing %}
# тут, если файл не будет найден, то результатом будет страница без какого-то куска (который не нашли)
# можно сразу обработать несколько файлов: {% include ['page1.htm', 'page2.htm'] ignore missing %}



'''
import работает похоже, только он не тащит файл целиком, а берет из него макросы.
Есть файл dialogs.htm, в нем диалоговое окно и кнопка "закрыть". Вставим его в страницу, как выше:

{% include 'header.htm' ignore missing %}
{% import 'dialogs.htm' as dlg %}         – берем файл, задаем псевдоним dlg
Содержимое страницы
{{ dlg.dialog_1('Внимание', 'Это тестовый диалог') }}    – в файле макрос, туда надо что-то передать, передаем.
{% include 'footer.htm' %}

'''

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('page2.htm')
msg = tm.render()

print(msg)