import pandas as pd


titanic_df = pd.read_csv('titanic.csv')
pd.set_option('display.max_columns', None)
# print(titanic_df)
# print()

"""При группировке, указываются столбцы, по которым надо сделать выборку. В данном случае это пол, затем Выживаемость.
В результирующей таблице будут колонка Sex, затем Survived. После этого указывается, что еще вывести для этих записей,
в примере это PassengerID, просто потому что он заполнен у всех, можно выбрать и другое поле, но например возраст
есть не у каждого пассажира, поэтому он не подойдет. И в конце метод count посчитает, сколько всего записей."""
print(titanic_df.groupby(['Sex', 'Survived'])['PassengerID'].count())

print(titanic_df.groupby(['PClass', 'Survived'])['PassengerID'].count())
