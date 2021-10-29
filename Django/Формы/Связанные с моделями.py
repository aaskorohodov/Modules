'''
Класс выглядит так:

    class AddPostForm(forms.ModelForm):
        class Meta:
            model = Women  # указывает, с какой моделью установить связь
            fields = '__all__'  # указывает, какие поля брать (__all__ берет все, кроме заполняемых автоматически)

Наследуется уже от forms.ModelForm, в отличие от формы, несвязанной с моделью.
Можно указать, какие поля брать:

    fields = ['title', 'slug', 'content', 'is_published', 'cat']

Можно задать свой стиль оформления для полей:

    widgets = {
                'title': forms.TextInput(attrs={'class': 'form-input'}),
                'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            }

form-input = стиль из css

Для выпадающего списка можно переписать начальное значение:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

Метод прописывается в самое начала класса формы. Он вызывает init для super, там прописывает параметр пустого поля.


Чтобы отправлять файлы через форму, нужно в отображении не только указать связь форма-модель, но и передать файл:

    form = AddPostForm(request.POST, request.FILES)

А в шаблоне нужно заставить форму не кодировать данные, при передаче на сервер:

    <form action="{% url 'add_page' %}" method="post" enctype="multipart/form-data">

<!-- action сообщает, куда отправить форму, когда она готова и куда отправится (переадресация)
enctype="multipart/form-data" заставляет не кодировать данные формы, нужно для отправки файлов -->
'''