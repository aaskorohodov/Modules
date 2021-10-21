'''
К статическим файлам относятся CSS, картинки и JS. В режиме отладки Джанго берет их их папки приложения, в боевом режиме из корневой
папки. При раскатке на сервер выполняется команда python manage.py collectstatic, она собирает все статические файлы и
перекладывает их в корневую папку.

В настройках проекта есть:

STATIC_URL – префикс URL-адреса для статических файлов;
STATIC_ROOT – путь к общей статической папке, используемой реальным веб-сервером;
STATICFILES_DIRS – список дополнительных (нестандартных) путей к статическим файлам, используемых для сбора и для режима отладки.

Для работы со статическими файлами, в шаблоне, в самом верху, нужно загрузить статический файлы:

{% load static %}

Затем их можно использовать (подключаем стили):

<link type="text/css" href="{% static 'women/css/styles.css' %}" rel="stylesheet" />

Тут статический файл загружается в качестве ссылки на стиль. Путь указывается относительный, до папки static внутри
приложения Джанго дойдет сам, дальше надо показать.

'''