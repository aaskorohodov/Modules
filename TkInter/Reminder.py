import time
from tkinter import *


window = Tk()
window.title("Добро пожаловать в приложение!")
# window.geometry('700x500')




def start():
    def clicked():
        def timer_start():
            tinfo = secsinpt.get()
            print(tinfo)
            # timer_info = Label(window, text=)

        lbl.pack_forget()
        btn.pack_forget()
        txt.pack_forget()

        f_top = Frame(window)
        f_secs = Frame(window)
        f_mins = Frame(window)
        f_hrs = Frame(window)
        f_btn = Frame(window)

        lbl2 = Label(f_top, text='Через сколько?', font=("Arial Bold", 50)).pack()

        secslbl = Label(f_secs, text='Сек:').pack(side=LEFT)
        secsinpt = Entry(f_secs).pack(side=LEFT)

        minslbl = Label(f_mins, text='Мин:').pack(side=LEFT)
        minsinpt = Entry(f_mins).pack(side=LEFT)

        hrslbl = Label(f_hrs, text='Час:').pack(side=LEFT)
        hrsinpt = Entry(f_hrs).pack(side=LEFT)

        btnstart = Button(f_btn, text='Старт', command=timer_start, font=('Arial Bold', 15)).pack()

        f_top.pack()
        f_secs.pack()
        f_mins.pack()
        f_hrs.pack()
        f_btn.pack()

    lbl = Label(window, text="О чем напомнить?", font=("Arial Bold", 50))
    lbl.pack(expand=1, padx=10)
    txt = Entry(window, font=("Arial Bold", 20))
    txt.pack(fill=BOTH, pady=15, padx=10, expand=1)
    btn = Button(window, text="Клик!", command=clicked, font=("Arial Bold", 20))
    btn.pack(pady=15, expand=1)


if __name__ == '__main__':
    start()
    window.mainloop()