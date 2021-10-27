'''
При первом входе в админку надо создать супер-пользователя: python manage.py createsuperuser

Удаление пользователя:
    > python manage.py shell
    $ from django.contrib.auth.models import User
    $ User.objects.get(username="joebloggs", is_superuser=True).delete()

Смена пароля: python manage.py changepassword <user_name>


Чтобы работаьт в админке с приложениями, их надо регистрировать. Регистрация проходит в файле admin.py в каталоге
приложения. Сначала надо импортировать нужную модель или все
    from .models import *
затем зарегистрировать
admin.site.register(Имя модели)

'''