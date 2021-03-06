'''
print(objects, sep=' ', end='\n', file=sys.stdout, flush=False)

– objects – объект, который нужно вывести (или несколько объектов через запятую)
– sep – разделяет объекты. Значение по умолчанию: ‘ ‘;
– end – ставится после всех объектов;
    *то есть этот разделитель ставится 1 раз в конце выполнения print. Если убрать, то два print выйдут в 1 строку
– file – ожидается объект с методом write (string). Если значение не задано, для вывода объектов используется файл sys.stdout;
    *file производить запись (переданного в print значения) в файл. Если файл не существует, то он будет создан.
    Файл также лучше закрыть после такого метода записи.
– flush – если задано значение True, поток принудительно сбрасывается в файл. Значение по умолчанию: False.
'''