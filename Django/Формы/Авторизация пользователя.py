'''
Не совсем форма, но и форма тоже. Сначала view, все наглядно и очевидно:

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm  # связанный класс формы
    template_name = 'women/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


Сама форма еще проще:

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


Шаблон формы:

form method="post">
    {% csrf_token %}

    <!-- Вывод общих ошибок формы, например неверный логин или пароль -->
    <div class="form-error">{{ form.non_field_errors }}</div>

        {% for f in form %}
        <p><label class="form-label" for="{{ f.id_for_label }}">{{f.label}}: </label>{{ f }}</p>

        <!-- f.errors выводит стандартное сообщение об ошибке, если что-то заполнено неверно -->
        <div class="form-error">{{ f.errors }}</div>

        {% endfor %}
    <button type="submit">Войти</button>
</form>


Чтобы проверять пользователя на авторизацию (залогинился ли он):

    {% if request.user.is_authenticated %}
    ...


Чтобы выводить имя пользователя в шаблоне:

    ...{{user.username}}...



Чтобы сделать logout достаточно простой функций view:

    def logout_user(request):
        logout(request)
        return redirect('login')


Чтобы при регистрации нового пользователя сразу его авторизовать, в классе view:

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
'''