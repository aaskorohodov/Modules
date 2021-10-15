'''
Пример запроса:
127.0.0.1:8000/cats/music/?name=Gagarina&type=pop

Django отловит параметры запроса (?name=Gagarina&type=pop) и запакует в словарь, который доступен тут: request.GET.
Его можно получить и посмотреть в отображении, куда он передается вместе с request. Например:

def categories(request, cat):
    print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1>{cat}</p>")

'''