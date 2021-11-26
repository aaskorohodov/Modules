import tkinter as tk

window = tk.Tk()

label = tk.Label(text="Имя")  # подпись под окном ввода
entry = tk.Entry()  # окно ввода


entry.pack()
label.pack()


window.mainloop()