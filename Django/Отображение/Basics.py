'''
Самый простой способ – создать функцию.


from django.http import HttpResponse

def index(request):
    return HttpResponse("Текст страницы")


index – имя функции, может быть любым.
request – это ссылка на класс HttpResponse, который содержит всю информацию о текущем запросе
return HttpResponse – HttpResponse экземпляр класса,
'''


'''
Работая с шаблонами, функция отображения выглядит так:

def index(request):
    return render(request, '<путь к шаблону>')
    
render отвечает за обработку шаблонов и выдачу их в формате HTTP-ответа
<путь к шаблону> по умолчанию ищется внутри текущего приложения в папке templates, так что ее указывать не надо.
'''