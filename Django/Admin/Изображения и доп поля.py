'''
Чтобы отображать в админке картинки, а не просто имя пути, требуется добавить в класс модели Админки метод:

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

if object.photo: = проверяем, есть ли картинка (если нет, то вернется None, и Джанго нарисует прочерк). Или можно:
    else:
        return "Нет фото"

object = ссылка на текущую запись (на текущий пост)
mark_safe = воспринимать теги как теги (не экранировать)
src='{object.photo.url}' = получает путь к картинке
width=50 = максимальная ширина (нужна миниатюра)

Теперь этот метод можно передать в качестве поля:

    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published')

Чтобы изменить имя столбца (там сейчас было бы get_html_photo), прямо в эту же модель в админки добавить:

    get_html_photo.short_description = "Миниатюра"
'''


'''
Чтобы менять поля внутри карточки чего-то в админке, нужно указать переменную:

    fields = ('title', 'slug', 'cat', 'content', 'photo', 'is_published')

fields = порядок и список !редактируемых! полей. Чтобы показать нередактируемые поля надо добавить:

    readonly_fields = ('time_create', 'time_update')

А в fields добавить эти новые поля:

    fields = ('title', 'slug', 'cat', 'content', 'photo', 'is_published', 'time_create', 'time_update')

Если есть уже метод для вывода картинки, то можно его тоже сюда добавить:

    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')

'''