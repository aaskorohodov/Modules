'''
slug = урл из букв.

В urls.py слаги отлавливаются так:

    path('post/<slug:post_slug>/', show_post, name='post'),

Работает аналогично int – ловим буквы, пакуем в переменную (post_slug), передает в отображение.
Чтобы как-то обработать слаг, его можно добавить в модель, там есть специальное поле:

    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
'''