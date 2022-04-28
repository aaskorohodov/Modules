import numpy as np
import matplotlib.pyplot as plt
import matplotlib


matplotlib.use('TkAgg')

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

'''Если сделать такой график, то на нем будут мелкие колебания, которые не будет видно'''

x = np.arange(-10 * np.pi, 10 * np.pi, 0.5)
ax.plot(x, np.sinc(x) * np.exp(-np.abs(x / 10)))

'''Вот так его можно сделать логарифмическим'''

ax.semilogy(x, np.sinc(x) * np.exp( -np.abs(x/10)) )
ax.grid()
plt.show()

'''
semilogy() - по У
semilogx() - по Х
'''

'''
Аналог:
    ax.set_yscale('log')
    ax.set_xscale('log')
    
Значения:
    'linear' – линейный масштаб (используется по умолчанию);
    'log' – логарифмический масштаб;
    'symlog' – вблизи нуля (в указанных пределах) масштаб линейный, а в остальной области – логарифмический.
'''