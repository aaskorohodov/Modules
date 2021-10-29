'''
CBV – Class-Based Views

Пример:

    class WomenHome(ListView):
        model = Women  # указываем модель

Такое отображение по умолчанию будет искать шаблон тут: <имя приложения>/<имя модели>_list.html
Чтобы указать другое имя, используется такое:

    template_name = 'women/index.html'

В urls.py вызывается так:

    path('', WomenHome.as_view(), name='home')

WomenHome = имя класса
.as_view() = функция именно вызывается, со скобками ()

По умолчанию, Джанго передаст в шаблон данные в коллекции с именем object_list, ее можно перебирать циклом, аналогично
коллекциям из функция.
Коллекции можно задать другое имя:

    context_object_name = 'posts'

Если список пуст, нет такой страницы, то можно сгенерировать 404:

    allow_empty = False

Передать дополнительные параметры шаблону можно так:

    extra_context = {'title': 'Главная страница'}

Либо так:

    class WomenHome(ListView):
    ...
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

Что тут происходит:
get_context_data вызывается автоматически, нигде прописывать вызов не надо
context = в классу super, то есть ListView, берем уже имеющиеся там данные (автоматически сделанные из модели),
и распаковываем в словарь (**kwargs)
Затем добавляем в этот словарь любые другие данные, context['title'] = 'Главная страница'

Из модели также можно добыть только часть данных:

        def get_queryset(self):
            return Women.objects.filter(is_published=True)

Или так:

        def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        Ниже обращаемся к коллекции данных из модели, берем первую запись, оттуда берем cat = название категории

        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context
'''