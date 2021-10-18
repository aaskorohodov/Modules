'''
Модели создаются в соответствующем файле внутри своего приложения. Django все равно, с какой базой данных
(из совместимых) он будет работать, алгоритм создания модели одинаковый, отличается только настройка (выбор БД).

Для создания модели объявляется новый класс, его имя будет = имени таблицы. Новый класс наследуется от models.Model:

class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

*тут нет primarykey, потому что он генерируется автоматически
*последовательность полей по умолчанию будет аналогичной объявленному классу

Поля таблицы (на стороне Django) являются разными классами (models.CharField, models.TextField...). Эти классы
представляют разные типы полей в БД, все просто и почти всегда наглядно.

'''