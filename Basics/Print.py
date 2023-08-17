"""
print(objects, sep=' ', end='\n', file=sys.stdout, flush=False)

– objects – the object to be displayed (or several objects separated by commas)
– sep – separates objects. Default value: ' ';
– end – placed after all objects;
     *that is, this separator is set 1 time at the end of the print execution. If you remove it, then two prints will
     come out in 1 line
– file – an object with a write (string) method is expected. If not set, the sys.stdout file is used to output objects;
     *file write (the value passed to print) to a file. If the file does not exist, then it will be created.
     It is also better to close the file after such a recording method.
– flush – if set to True, the stream is forcibly flushed to a file. Default value: False.
"""
