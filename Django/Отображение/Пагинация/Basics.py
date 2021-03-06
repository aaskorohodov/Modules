'''
Пагинацию можно строить из функции или класса view. Представляет собой класс Django, который может работать со списками.
Строится так:

    from django.core.paginator import Paginator

    women = ['Анджелина Джоли', 'Дженнифер Лоуренс', 'Джулия Робертс', 'Марго Робби', 'Ума Турман', 'Ариана Гранде', 'Бейонсе', 'Кэтти Перри', 'Рианна', 'Шакира']
    p = Paginator(women, 3)

    *3 = 3 штуки на страницу

Есть методы:
    p.count # число элементов в списке
    p.num_pages # число страниц (10:3 = 4 – округление до большего)
    p.page_range # итератор для перебора номеров страниц

И много других

Можно позвать первую страницу, у нее тоже свои методы:
    p1 = p.page(1) # получение первой страницы
    p1.object_list  # список элементов текущей страницы
    p1.has_next() # имеется ли следующая страница
    p1.has_previous() # имеется ли предыдущая страница
    p1.has_other_pages() # имеются ли вообще страницы
    p1.next_page_number() # номер следующей страницы
    p1.previous_page_number() # номер предыдущей страницы

    

'''