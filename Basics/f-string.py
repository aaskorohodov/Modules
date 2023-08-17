import datetime

num = 123
some_str = 'hello'
print(f'{num=}')        # Will print literally 'num=123'. Not '123'm but 'num=123'
print(f'{num / 2 = }')  # Operations can be executed inside f-string
print(f'{some_str!r}')  # Formal representation of an object (call to __repr__() is happening)


more_num = 123.456
now = datetime.datetime.utcnow()
print(f'{more_num:.2f}')  # Rounding
print(f"{now:%Y %m %d}")  # Formatting
