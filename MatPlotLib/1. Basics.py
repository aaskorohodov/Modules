"""
pip install matplotlib

С ним устанавливается:
    NumPy (>= 1.15)
    setuptools
    cycler (>= 0.10.0)
    dateutil (>= 2.1)
    kiwisolver (>= 1.0.0)
    Pillow (>= 6.2)
    pyparsing (>=2.0.3)

А для визуальной отрисовки используется TkInter, но он должен быть в стандартном пакете Питона
"""

import matplotlib

print(matplotlib.get_backend())  # Выводит используемый модуль для графической отрисовки

'''
Qt5Agg = Рендеринг графики в Qt5 (требуется PyQt5). В IPython активируется командой %matplotlib qt5
ipympl = Рендеринг графики в виджете Jupyter (требуется ipympl). В IPython активируется командой %matplotlib ipympl
GTK3Agg = Рендеринг графики в GTK 3.x (требуется PyGObject и pycairo или cairocffi). В IPython активируется командой %matplotlib gtk3
macosx = Рендеринг графики в Cocoa. В IPython активируется командой %matplotlib osx
TkAgg = Рендеринг графики в Tk (требуется TkInter). В IPython активируется командой %matplotlib tk
nbAgg = Рендеринг графики в Jupyter notebook. В Jupyter активируется командой %matplotlib notebook
WebAgg = Для использования с торнадо-сервером.
GTK3Cairo = Cairo рендеринг графики в GTK 3.x x (требуется PyGObject и pycairo или cairocffi).
Qt4Agg = Рендеринг графики в Qt4 (требуется PyQt4 или pyside). В IPython активируется командой %matplotlib qt4
wxAgg = Рендеринг графики в wxWidgets (требуется wxPython 4). В IPython активируется командой %matplotlib wx
'''

matplotlib.use('TkAgg')  # Выбор графического бекэнда

'''Но этот выбор надо каждый раз прописывать в коде'''

import matplotlib.pyplot as plt  # Импорт модуля
plt.plot([1, 2, -6, 0, 4])       # Рисуем график
plt.show()                       # Держим окно с графиком открытым


'''В основе окна лежит Фигура (Figure), на ней рисуется график (Axes). Графиков в окне может быть несколько
со своими координатами.
На графике есть 2 или 3 координатные оси (Axis), сетку, метки (ticks), легенду и произвольное число графиков.
Объект Artist отвечает за размещение и оформление отображаемых данных на рисунке (Figure) и взаимодействует
непосредственно с объектом Canvas – подложки для рисования на холсте (рисунке).
'''
