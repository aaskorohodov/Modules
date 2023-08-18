import io

"""
Syntax:
with <Expression>[ as <Variable>]:
     <The block in which we catch exceptions>

'with as' is called a 'context manager'. Its task is to close the file (or something else) even if an error occurs.
It is not necessary to write close() or similar methods in the body of the expression.

With...as is similar to Try...finally, but more concise. If you need to write something in finally, and this can be
executed by the __exit__ method, then you can use with...as
"""


text = "Hello, this is some text."

# Create an in-memory text file-like object (imitating reading an actual file)
with io.StringIO(text) as file:
    contents = file.read()

print(contents)  # Output: Hello, this is some text.
