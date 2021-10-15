'''
301 и 302 (временный и постоянный) редиректы можно звать в конструкторе отображения при каком-то условии, например.

def archive(request, year):
    if(int(year) > 2020):
        return redirect('/')

    return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")

Тут при введенном годе свыше 2020 случится редирект на главную. Но имя главной прописано строго, что плохо. Если задать
в urls какому-то сопоставлению придуманное имя, то можно давать редиректу сразу его:

return redirect('home')

Также можно выбрать перманентное перемещение (302):

return redirect('home', permanent=True)
'''