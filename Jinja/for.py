from jinja2 import Template


cities = [{'id': 1, 'city': 'Москва'},
          {'id': 5, 'city': 'Тверь'},
          {'id': 7, 'city': 'Минск'},
          {'id': 8, 'city': 'Смоленск'},
          {'id': 11, 'city': 'Калуга'}]

# html тег select создает выпадающий список, или просто список выбора

'''Ниже: перебираем с в cities, для каждого задаем option value (то, что будет элементом списка в html)
* -% в блоке for указывает удалять все переносы и пробелы после блока for и после endfor
**аналогично работает минус в endfor
'''

link = '''<select name="cities">
{% for c in cities -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% endfor -%}
</select>'''

tm = Template(link)
msg = tm.render(cities=cities)

print(msg)