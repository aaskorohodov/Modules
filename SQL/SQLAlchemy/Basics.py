from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker


engine = create_engine('sqlite:///test.db', echo=True)  # echo печатает обращения к базе, для наглядности
base = declarative_base()


'''
Сама Alchemy дает возможность маппинга объектов (например классов) в базу. Основных метода 2:
    Декларативный – создается базовый класс, от которого наследуются классы с данными
    Классический – элементы таблицы вручную связываются с атрибутами/значениями
'''

class User(base):
    '''
    Это пример декларативного маппинга – наследуем User от base (declarative_base). Теперь User будет тем классом,
    чьи данные будет зранить база. Все остальное случится под капотом Алхимии.
    '''
    __tablename__ = 'users'  # задает имя таблицы
    id = Column(Integer, primary_key=True)  # id связывает объект питона с "объектом" базы. По нему Алхимия их различает
    name = Column(String)  # Column, String являются объектами Алхимии, их надо импортировать
    fullname = Column(String)


def write_to_base():
    '''Это создание таблицы'''
    base.metadata.create_all(engine)
    '''Это создание сессии'''
    session = sessionmaker(bind=engine)()
    '''Это создание юзера, объекта, который будет занесен в базу'''
    user_ivan = User(name = 'Ivan', fullname = 'Ivan Ivanov')
    '''Это добавление объекта в сессию. При этом запись в базу пока не происходит'''
    session.add(user_ivan)
    '''А это запись в базу. Теперь объект записан.'''
    session.commit()
    print(user_ivan.id)

# write_to_base()


def read_from_base():
    '''При чтении также нужна сессия'''
    session = sessionmaker(bind=engine)()
    '''Обращаемся к сессии, делаем запрос (query) через engine (он (engine) знает, где искать файл таблицы), указываем
    в какой класс сделать маппинг (User), фильтруем по имени. Фильтрация на стороне питона, этого не будет видно
     в запросе к базе'''
    q = session.query(User).filter_by(name='Ivan')
    '''Берем оттуда первого Ивана. При этом в питоне формируется объект класса User'''
    some_ivan = q.first()
    '''Теперь из этого объекта можно прочитать атрибуты'''
    print(some_ivan)

# read_from_base()


def add_to_sql():
    session = sessionmaker(bind=engine)()  # я хз почему тут двойные скобки, но без них ничего не работает
    session.add_all([ User(name='Petr', fullname='Petr Petrov')])
    session.commit()

# add_to_sql()


def rewrite_to_base():
    session = sessionmaker(bind=engine)()

    q = session.query(User).filter_by(name='Ivan')
    some_ivan = q.first()

    '''Выше прошло чтение, создался питоновый объект, у него переписали fullname и закоммитили'''
    some_ivan.fullname = 'Ivan Sidorenko'
    session.commit()


# rewrite_to_base()


def asd():
    session = sessionmaker(bind=engine)()
    s = session.execute('select * from Users')
    some_ivan = s.first()
    print(some_ivan)
    print(type(some_ivan))
    print(some_ivan[1])


# asd()


def delete():
    '''Удаление объекта. Создаем сессию, указываем класс для маппинга (User), фильтруем, выбираем (q.first), удаляем'''
    session = sessionmaker(bind=engine)()
    q = session.query(User).filter_by(name='Petr')
    petr = q.first()
    session.delete(petr)
    session.commit()


delete()