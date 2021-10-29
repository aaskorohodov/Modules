'''
Если шаблон может обрабатывать переменные, то их можно передать прямо из отображения:

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    return render(request, 'women/index.html', {'menu': menu, 'title': 'Главная страница'})


Переменные передаются словарем, тут мы передаем список (menu) в качестве значения, а ключ придумываем сами.
Шаблон возьмет значение, если указать ему ключ:

!DOCTYPE html>
<html>
<head>
         <title>{{ title }}</title>

Тут он распакует title и возьмет значение ('Главная страница'). Вот посложнее:

<ul>
{% for m in menu %}
<li>{{m}}</li>
{% endfor %}
</ul>

Тут мы переберем список и сделаем из него html список. Вот еще:

def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

Берем все записи из базы по конкретной модели, и передаем это в шаблон:

<ul>
         {% for p in posts %}
         <li>
                   <h2>{{p.title}}</h2>
                   {{p.content}}</p>
                   <hr>
         </li>
         {% endfor %}
</ul>
'''



# context
'''
Чтобы не перегружать строчку (render), можно предварительно подготовить словарь с переменными, а затем передать его 
в специальную переменную context:

def index(request):
    posts = Women.objects.all()
    some_name = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'women/index.html', context=some_name)
'''