import pandas as pd
import matplotlib.pyplot as plt




weight = pd.read_csv(r'C:\Users\Аркадий\PycharmProjects\Modules\Pandas\weight.csv', delimiter=';')

weight_only = weight['Вес']

weight_only.plot()

plt.show()