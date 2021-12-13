'''
У Django уже есть встроенная модель для пользователя, со своей таблицей в базе. Пользуясь ей, сначала нужен класс view:


    class RegisterUser(DataMixin, CreateView):
        form_class = UserCreationForm
        template_name = 'women/register.html'
        success_url = reverse_lazy('login')

        def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            c_def = self.get_user_context(title="Регистрация")
            return dict(list(context.items()) + list(c_def.items()))


Тут класс наследуется от Миксина и CreateView, который как раз создан для работы с формами.
Указывается имя формы form_class = UserCreationForm, это стандартная форма Django, она сама сделает поля формы
Указывается, куда пойти в случае успеха success_url = reverse_lazy('login')
Затем добываем данные контекста и пакуем в словарь, словарь объединяем с дефолтным.


Можно переделать форму, изменить ее вид и добавить полей. Для этого нужен свой класс формы:

    class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }

RegisterUserForm = произвольное имя, чтобы view стал звать эту форму, нужно у него переписать стандартный
UserCreationForm на RegisterUserForm (form_class = RegisterUserForm)
Наследуется от UserCreationForm
fields = имена полей, которые отображать. Это стандартные поля, их имена фиксированы, их надо смотреть в коде страницы
(именно для регистрации, потому что Django уже делает ее в админке, та их и можно посмотреть, а еще в документации)
widgets = стили полей. Но в таком виде они тут не работают, надо в таком (вне Meta, выше, просто в классе):

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

Можно добавить еще полей:

    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))

Их нужно передать в списке:

    fields = ('username', 'email', 'password1', 'password2')

'''