import pandas as pd


print("dataframe это таблица, где столбцы являются объектами series. dataframe можно сделать из словаря\n")

df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]
})

print(df)
print()

print("Убедимся, что столбцы это series:  df['country']")
print(df['country'])
print()

print("Посмотреть имена колонок  df.columns")
print(df.columns)
print()

print("Посмотреть сколько элементов (строк)  df.index")
print(df.index)
print()

print("Номер строки, то есть индекс, можно задать при создании таблицы")
df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]
}, index=['KZ', 'RU', 'BY', 'UA'])
print(df)
print()

print("Или на уже созданной таблице")
df.index = ['KZ', 'RU', 'BY', 'UA']
df.index.name = 'Country Code'
print(df)
print()

print("При этом объекты series в этом dataframe получили те же имена индексов")
print(df['country'])
print()

print("Доступ к записи, т.е. строке (объекту таблицы), можно получить по имени индекса, который мы задали вручную,"
      "либо по номеру, который задается по дефолту. "
      "Первый называется .loc "
      "второй .iloc")

print(df.loc['KZ'])
print()
print(df.iloc[0])
print()

print("Выборка по строкам и колонкам одновременно  df.loc[['KZ', 'RU'], 'population']")
print(df.loc[['KZ', 'RU'], 'population'])
print()

print("Выборка с... по... Причем как по колонкам, так и по строкам. Можно взять все, ничего не указав (:)")
print(df.loc['KZ':'BY', 'country':'population'])
print()

print("Взять конкретные колонки")
print(df[['country', 'square']])
print()

print("Взять одну колонку можно так или так")
print(
    df.population,
    '\n\n',
    df['population']
)

print("Фильтрация")
print(df[df.population > 10])
print()

print("Сброс индексов")
print(df.reset_index())
print()

print("При операциях над dataframe, возвращается новый объект. Несмотря на сброс индексов, старый массив остался")
print(df)
print()

print("Добавляем новый столбец, беря данные из старых")
df['density'] = df['population'] / df['square'] * 1000000
print(df)

print("Удаляем столбец, при этом возвращается новый объект, в старом ничего не меняется")
print(df.drop(['density'], axis='columns'))
print()

print("А теперь удаляем колонку в старом объекте")
del df['density']
print(df)
print()

print("Переименование имени индексов возможно только после его сброса")
df = df.reset_index()
df = df.rename(columns={'Country Code': 'country_code'})
print(df)