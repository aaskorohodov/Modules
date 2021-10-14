'''
Самый простой способ – создать функцию.


from django.http import HttpResponse

def index(request):
    return HttpResponse("Текст страницы")


index – имя функции, может быть любым.
request – это ссылка на класс HttpResponse, который содержит всю информацию о текущем запросе
return HttpResponse – HttpResponse экземпляр класса,

'''