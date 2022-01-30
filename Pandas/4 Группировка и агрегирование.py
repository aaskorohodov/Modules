import pandas as pd


titanic_df = pd.read_csv('titanic.csv')
pd.set_option('display.max_columns', None)
print(titanic_df)
print()

print(titanic_df.groupby(['Survived', 'Sex'])['PassengerID'].count())
