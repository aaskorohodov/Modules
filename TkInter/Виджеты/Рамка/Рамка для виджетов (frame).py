'''
По умолчанию виджеты кладутся в окно, но их можно положить в рамку, указав master = наша_рамка.
'''

import tkinter as tk

window = tk.Tk()

frame_a = tk.Frame()  # рамка 1
frame_b = tk.Frame()  # рамка 2

label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

frame_a.pack()
frame_b.pack()

window.mainloop()