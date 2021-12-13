'''
Если все записи влезли на 1 страницу, и пагинировать некуда, то отображать внизу номер страниц может быть лишним. Убрать
можно в шаблоне, проверяя, есть ли другие страницы, кроме показанной:

    {% if page_obj.has_other_pages %}
        <nav class="list-pages">
            ...  тут наша пагинация ...
        </nav>
    {% endif %}
'''

'''
Можно не давать ссылку на текущую страницу (или делать у нее другой эффект):

    <nav class="list-pages">
    <ul>
    
        {% for p in paginator.page_range %}
        
                   {% if page_obj.number == p %}
        <li class="page-num page-num-selected">{{ p }}</li>
        
                   {% else %}
        <li class="page-num">
            <a href="?page={{ p }}">{{ p }}</a>
        </li>
        
                   {% endif %}
        {% endfor %}
    </ul>
</nav>

Тут главное, что если проверка проходит, то мы просто не делаем ссылку.
'''

'''
Можно отображать не все доступные номера страниц, а только какую-то часть. Делая это в шаблоне, можно использовать его
встроенный фильтр |add и условие if, чтобы выводить, например, 2 страницы до текущей и 2 после:

        {% for p in paginator.page_range %}
                   {% if page_obj.number == p %}
        <li class="page-num page-num-selected">{{ p }}</li>
                   {% elif p >= page_obj.number|add:-2 and p <= page_obj.number|add:2  %}
        <li class="page-num">
            <a href="?page={{ p }}">{{ p }}</a>
        </li>
                   {% endif %}
        {% endfor %}
'''

'''
Отображение следующая/предыдущая страница делается до и после цикла for:

    {% if page_obj.has_previous %}
    <li class="page-num">
             <a href="?page={{ page_obj.previous_page_number }}">&lt;</a>
    </li>
    {% endif %}
    
    ...
    
    {% if page_obj.has_next %}
    <li class="page-num">
         <a href="?page={{ page_obj.next_page_number }}">&gt;</a>
    </li>
    {% endif %}

Тут проверяется, нужно ли показывать след/пред страницу, если нужно, то выводим ссылку. &lt; и &gt; это экранированные
значки <>.
'''