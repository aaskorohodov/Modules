import matplotlib.pyplot as plt
import pandas as pd


# читаем и в качестве индекса берем дату
df = pd.read_csv('apple.csv', index_col='Date', parse_dates=True)

# сортируем по индексу, т.е. по дате (там неверная сортировка изначально)
df = df.sort_index()

# берем с 2012-Feb по 2017-Feb и только колонку Close
df = df.loc['2012-Feb':'2017-Feb', ['Close']]
print(df)

# рисуем
df.plot()
plt.show()