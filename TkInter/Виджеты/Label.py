import tkinter as tk

window = tk.Tk()

label = tk.Label(
    text="Привет, Tkinter!",
    fg="white",
    bg="black",
    width=20,
    height=20
)
# несмотря на заданную высоту, окно будет не квадратным, тк это "текстовые юниты"

label.pack()
window.mainloop()