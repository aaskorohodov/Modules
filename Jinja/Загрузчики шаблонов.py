from jinja2 import Environment, FileSystemLoader

persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0}
]


file_loader = FileSystemLoader('templates')  # указываем папку, ее он ищет внутри текущего каталога
env = Environment(loader=file_loader)  # создаем загрузчик, который будет брать все файлы из каталога (выше)

'''Далее на объект выше (env) зовем метод get_template, которому указываем нужный файл. Этот метод сформирует
экземпляр класса Template, то есть сделает шаблон. Идея в том, что в этом шаблоне, то есть в файле, будет какой-либо
jinja-код. Затем render выполнит этот jinja-код.'''

tm = env.get_template('main.htm')
msg = tm.render(users=persons)

print(msg)



# теперь другой загрузчик FunctionLoader, он работает на функциях

from jinja2 import FunctionLoader


def loadTpl(path):  # придумываем функцию
    if path == "index":
        return '''Имя {{u.name}}, возраст {{u.old}}'''
    else:
        return '''Данные: {{u}}'''


file_loader = FunctionLoader(loadTpl)
env = Environment(loader=file_loader)

tm = env.get_template('index')
msg = tm.render(u=persons[0])