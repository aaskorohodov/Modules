'''
Для функции нужно все делать руками:


    contact_list = Women.objects.all()          читаем
    paginator = Paginator(contact_list, 3)      передаем что прочитали в пагинатор, указываем сколько выводить записей

    page_number = request.GET.get('page')       берем из запроса номер страницы
    page_obj = paginator.get_page(page_number)  передаем номер страницы пагинатору

    return render(request, 'шаблон', {'page_obj': page_obj, ...}        передаем все в шаблон


В шаблоне остается только перебрать эту коллекцию:

    {% for el in page_obj %}

        <p>{{ el }}</p>

    {% endfor %}


И показать кнопки пагинации:

<nav>
    <ul>
        {% for p in page_obj.paginator.page_range %}
        <li>
            <a href="?page={{ p }}">{{ p }}</a>
        </li>
        {% endfor %}
    </ul>
</nav>


Тут page_obj это то, что мы передали в шаблон, у него есть page_range, который вернет номера страниц. В ссылке мы их
указываем как /?page=12345/

'''