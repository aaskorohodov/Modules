'''
Сделаем форму, куда положим капчу. Это форма обратной связи, view:

    class ContactFormView(DataMixin, FormView):
        form_class = ContactForm
        template_name = 'women/contact.html'
        success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


Класс формы:

    class ContactForm(forms.Form):
        name = forms.CharField(label='Имя', max_length=255)
        email = forms.EmailField(label='Email')
        content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))


Шаблон:

    {% extends 'women/base.html' %}

    {% block content %}
    <h1>{{title}}</h1>

    <form method="post">
        {% csrf_token %}

        <div class="form-error">{{ form.non_field_errors }}</div>

    {% for f in form %}
    <p><label class="form-label" for="{{ f.id_for_label }}">{{f.label}}: </label>{{ f }}</p>
    <div class="form-error">{{ f.errors }}</div>
    {% endfor %}

        <button type="submit">Отправить</button>

    </form>

    <p>{% endblock %}


urls.py:

    path('contact/', ContactFormView.as_view(), name='contact'),
'''

'''
Теперь в эту форму положим капчку django-simple-captcha:

    pip install django-simple-captcha
    
INSTALLED_APPS = [
...
    'captcha',
...
]


В КОРНЕВОМ списке маршрутов:
    
urlpatterns = [
...
    path('captcha/', include('captcha.urls')),
...
]


В форме импортируем:

    from captcha.fields import CaptchaField

и просто дописываем еще 1 переменную в форму:

    captcha = CaptchaField()


Делаем миграцию после установки капчи:

    python manage.py migrate
'''