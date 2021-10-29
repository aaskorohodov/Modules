'''
Делается аналогично ListView:

    class ShowPost(DetailView):
        model = Women
        template_name = 'women/post.html'

По умолчанию ищет в urls.py переменную с именем slug. Если в маршруте отлавливается другое имя, то его можно
переопределить:

    slug_url_kwarg = 'post_slug'

404 на несуществующую страницу тут вызывается автоматически

'''