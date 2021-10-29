'''
Подходит для работ с формами:

    class AddPage(CreateView):
        form_class = AddPostForm
        template_name = 'women/addpage.html'

form_class указывает, какую форму брать


После добавления новой записи в модель, этот класс автоматически обратиться к get_absuolute_url и направится на новую
страницу, которая была создана формой. Если этого метод нет, то можно в классе использовать:

    success_url = reverse_lazy('home')



'''