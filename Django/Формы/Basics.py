'''
Формы размещаются в своем файле forms.py в каталоге приложения. Форма = класс, наследуемый от form.Form, это надо
импортировать (from django import forms).

Пример формы, для записи в имеющуюся модель:

    class AddPostForm(forms.Form):  # произвольное название, наследуется от forms.Form
        title = forms.CharField(max_length=255)
        slug = forms.SlugField(max_length=255)
        content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
        is_published = forms.BooleanField()
        cat = forms.ModelChoiceField(queryset=Category.objects.all())

Не все поля = полям модели, некоторых нет, потому что они заполняются автоматически. Из интересного:
cat читает модель queryset=Category.objects.all(), и делает на ее основе список ModelChoiceField

Для красивого отображения есть label:
    title = forms.CharField(max_length=255, label='Заголовок')

Чтобы сделать поле необязательным (required=False):
    is_published = forms.BooleanField(label="Публикация", required=False)

Начальная надпись в выпадающем меню:
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категории", empty_label="Категория не выбрана")

По умолчанию будет отмечено (initial=True):
    is_published = forms.BooleanField(label="Публикация", required=False, initial=True)

Затем класс передается в отображение, например так:

    def addpage(request):
        form = AddPostForm()
        return render(request, 'women/addpage.html', {'menu': menu, 'title': 'Добавление статьи', 'form': form})

Тут form ссылается на созданный класс AddPostForm, во views его надо импортировать (from .forms import *   сразу все)
Затем form передается в рендер ('form': form)
Затем создается шаблон для форма, например такой:

    {% extends 'women/base.html' %}

    {% block content %}
    <h1>{{title}}</h1>


    <!-- action сообщает, куда отправить форму, когда она готова и куда отправится (переадресация) -->
    <form action="{% url 'add_page' %}" method="post">
        <!-- csrf_token встроенная защита от копирования формы на другой ресурс -->
        {% csrf_token %}
        <!-- as_p = как параграф, т.е. отображать поля как параграфы -->
        {{ form.as_p }}
        <button type="submit">Добавить</button>
    </form>

    {% endblock %}


Пример с перебором циклом:

    {% for f in form %}
        <p><label class="form-label" for="{{ f.id_for_label }}">{{f.label}}: </label>{{ f }}</p>
        <div class="form-error">{{ f.errors }}</div>
    {% endfor %}


Более подходящее отображение для формы:

    def addpage(request):
        if request.method == 'POST':  # если request стал POST (форма была отправлена)
            form = AddPostForm(request.POST)  # формируем форму на основе словаря POST, где лежат заполненные данные
            if form.is_valid():  # если все норм, то написать очищенные данные в консоли
                try:
                    Women.objects.create(**form.cleaned_data)  # распаковываем словарь **
                    return redirect('home')
                except:
                    form.add_error(None, 'Ошибка добавления поста')
        else:
            form = AddPostForm()
        return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})
'''