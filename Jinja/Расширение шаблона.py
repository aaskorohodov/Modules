'''
Работает как в Django (в Джанго работает как тут)
'''

from jinja2 import Environment, FileSystemLoader


file_loader = FileSystemLoader('templates')  # указываем папку
env = Environment(loader=file_loader)  # создаем загрузчик

template = env.get_template('about.htm')  # берем то, чем будем расширять. Там уже написано что расширять

output = template.render()
print(output)