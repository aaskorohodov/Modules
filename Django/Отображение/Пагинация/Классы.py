'''
Некоторые классы view уже имеют встроенную пагинацию, нужно только указать атрибут в классе:

    class MyView(models.Model):
        paginate_by = N
        ...


С этим view уже отрисует по 3 записи на страницу, а переходить можно руками, вбивая урл. Если есть Миксин, который
работает с несколькими классами, то paginate_by = N можно передать ему, чтобы не прописывать это в каждом отдельном
классе view.

Также теперь в шаблон автоматически передаются объекты paginator и page_obj. Их можно использовать, чтобы вывести
нумерацию страниц снизу:

    <nav class="list-pages">
    <ul>
        {% for p in paginator.page_range %}

        <li class="page-num">

            <a href="?page={{ p }}">{{ p }}</a>

        </li>
        {% endfor %}
    </ul>
</nav>

paginator.page_range возвращает все номера страниц, номер используется чтобы по шаблону (?page=) сделать ссылку и
нарисовать номер.

'''