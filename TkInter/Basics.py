'''
Основным элементом является окно, в него кладутся виджеты
'''
import time
import tkinter as tk

window = tk.Tk()


'''Создаем виджет'''
greeting = tk.Label(text="Привет")
'''Добавляем виджет на окно'''
greeting.pack()


window.mainloop()