'''
Теги используются, например, для обращения к базе, чтобы минимизировать дублирование кода. Например, если views.py
обращается к базе и читает одни и теже данные для разных страниц, то это обращение можно вынести в отдельный тег.

Есть простой тег – возвращает какие-то данные в имеющийся шаблон
И включающий тег – возвращает кусок шаблона с данными (примерно как {% extends ... %}

Сначала создается папка templatetags внутри приложения, которая должна быть пакетом (__init__.py).
Сами теги располагаются внутри этого каталога, отдельным файлом. Имя произвольное.

Для работы потребуется template и моедли:
    from django import template
    from women.models import *

Собственные шаблонные теги регистрируются через класс Library(), пакуем его экземпляр в переменную:

    register = template.Library()

*по документации, переменная должна именоваться register, и накак иначе.

Затем описывается механизм работы тега, например этот возвращается все категории:

    def get_categories():
        return Category.objects.all()

*Category = модель, из которой читаем все записи
'''

# ПРОСТОЙ ТЕГ

'''
Чтобы превратить функцию в тег, оборачиваем ее в выше созданные экземпляр Library:

    @register.simple_tag()
    def get_categories():
        return Category.objects.all()


Затем, в нужном шаблоне, загружаем файл с тегом:

    {% load women_tags %}

Теперь в шаблоне можно использовать тег по имени функции (get_categories):

    {% get_categories %}

Чтобы в шаблоне с данными этого тега можно было работать, нужно извлечь их:

    {% get_categories as categories %}

Теперь переменную categories можно, например, перебирать:

    {% for c in categories %}
        ...
        ...
'''

# ВКЛЮЧАЮЩИЙ ТЕГ

'''
Отличается декоратором:

@register.inclusion_tag('women/list_categories.html')
    def show_categories():  # любое имя
        cats = Category.objects.all()  # читаем все категории, данные пакуем в cats
        return {"cats": cats}  # кладем эти данные в словарь (в значение), ключем задаем тоже cats.
                               # Этот словарь автоматически передастся в шаблон, указанный выше в декораторе

В декораторе прописывается путь к шаблону, шаблон кладется к другим шаблонам и представляет собой кусок страницы,
который можно вставить в другой шаблон. В самом шаблоне остается только вызвать тег:

    {% show_categories %}
'''

# ПЕРЕДАЧА ПАРАМЕТРОВ В ТЕГ

'''
Так как теги вызываются из какого-то шаблона, то мы можем прямо в шаблоне передать в тег какие-то данные, чтобы изменить
его поведение. Сначала простой тег:
    
    @register.simple_tag(name='getcats')
    def get_categories(filter=None):
        if not filter:
            return Category.objects.all()
        else:
            return Category.objects.filter(pk=filter)

Тут передается параметр filter (произвольное имя) с дефолтным значением None. Используется, чтобы выбрать определенную
запись из базы. Теперь можно в шаблоне передать в тег данные {% getcats filter=1 %} либо так {% getcats 2 %}.
Теперь включающий тег:

    @register.inclusion_tag('women/list_categories.html')
    def show_categories(sort=None, cat_selected=0):
        if not sort:
            cats = Category.objects.all()
        else:
            cats = Category.objects.order_by(sort)
     
        return {"cats": cats, "cat_selected": cat_selected}
        
Тут передается 2 параметра, вот так:

    {% show_categories '-name' cat_selected %}

Можно передать только 1 параметр, если передается второй, то дано указать его имя:

    {% show_categories cat_selected=cat_selected %}
    {% show_categories sort='name' %}
'''