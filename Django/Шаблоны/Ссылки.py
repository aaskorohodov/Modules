'''
Есть конструкция, которая делает ссылки в шаблонах:
href="{% url 'home' %}"

home = имя маршрута из urls.py:  path('', index, name='home')
'''



# динамические ссылки

'''
Прописываем в модели функцию, которая сделает url на эту модель (например на статью про экземпляр модели):

def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

reverse требует:
post = имя маршрута из urls.py
post_id = то, что будет поставлено в урле, согласно правилу в urls.py:
    
    path('post/<int:post_id>/', show_post, name='post')

path ждет какую-то цифру, мы ее как раз передадим, взяв из модели self.pk – это идентификатор.


Теперь можно в шаблоне вызвать метод класса Модели:  href="{{ p.get_absolute_url }}
'''