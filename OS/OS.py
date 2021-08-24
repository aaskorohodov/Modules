import os

print(os.name)
'''Имя операционной системы'''

#print(os.environ)
'''Список переменных окружений. Показывает пути до системных папок'''

print(os.listdir('C:/'))
'''Список папок в какой-либо дирректории'''

os.makedirs('C:/Users/Аркадий/Trash/asd', exist_ok=True)
'''Создает папку по указанному пути'''

#if os.path.exists('C:/Users/Аркадий/Trash/asd'):
#    os.remove('C:/Users/Аркадий/Trash/asd')
'''Удаляет папку. Столкнулся с проблемой доступа, не смог решить'''

if os.path.exists('C:/Users/Аркадий/Trash/asd/asd.txt'):
    os.replace('C:/Users/Аркадий/Trash/asd/asd.txt', 'C:/Users/Аркадий/Trash/asd.txt')
'''Перемещает файл'''

if os.path.exists('C:/Users/Аркадий/Trash/asd.txt'):
    os.startfile('C:/Users/Аркадий/Trash/asd.txt')
'''Открывает файл программой по умолчанию (системной)'''

print(os.getpid())