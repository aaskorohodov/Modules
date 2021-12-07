import time
from tkinter import *
import threading


class Timer():
    def ml(self):
        self.window.mainloop()

    def start(self):
        self.timer_number = 0
        self.window = Tk()
        self.window.title("Добро пожаловать в приложение!")

        self.lbl = Label(self.window, text="О чем напомнить?", font=("Arial Bold", 50))
        self.lbl.pack(expand=1, padx=10)
        self.txt = Entry(self.window, font=("Arial Bold", 20))
        self.txt.pack(fill=BOTH, pady=15, padx=10, expand=1)
        self.btn = Button(self.window, text="Клик!", command=self.clicked, font=("Arial Bold", 20))
        self.btn.pack(pady=15, expand=1)

    def clicked(self):
        self.lbl.pack_forget()
        self.btn.pack_forget()
        self.txt.pack_forget()

        self.f_top = Frame(self.window)
        self.f_secs = Frame(self.window)
        self.f_mins = Frame(self.window)
        self.f_hrs = Frame(self.window)
        self.f_btn = Frame(self.window)

        self.lbl2 = Label(self.f_top, text='Через сколько?', font=("Arial Bold", 50)).pack()

        self.secslbl = Label(self.f_secs, text='Сек:').pack(side=LEFT)
        self.secsinpt = Entry(self.f_secs)
        self.secsinpt.pack(side=LEFT)

        self.minslbl = Label(self.f_mins, text='Мин:').pack(side=LEFT)
        self.minsinpt = Entry(self.f_mins).pack(side=LEFT)

        self.hrslbl = Label(self.f_hrs, text='Час:').pack(side=LEFT)
        self.hrsinpt = Entry(self.f_hrs).pack(side=LEFT)

        self.btnstart = Button(self.f_btn, text='Старт', command=self.timer_start, font=('Arial Bold', 15)).pack()

        self.f_top.pack()
        self.f_secs.pack()
        self.f_mins.pack()
        self.f_hrs.pack()
        self.f_btn.pack()

    def timer_start(self):
        self.f_timer = Frame(self.window)

        self.timer_info = Label(self.f_timer, text=self.secsinpt.get(), bd=5)
        self.timer_info.pack(side=RIGHT)

        self.timer_number += 1
        self.timer_number_lbl = Label(self.f_timer, text=(f'Таймер {self.timer_number} '))
        self.timer_number_lbl.pack(side=RIGHT)

        self.f_timer.pack()
        self.secs = int(self.secsinpt.get())
        self.window.after(1000)
        self.go()

    # def threading_timer(self):
    #     x = threading.Thread(target=self.go)
    #     x.start()

    def go(self):
        self.secs -= 1
        if self.secs == 0:
            self.timer_info.configure(text=self.txt.get())
        else:
            self.timer_info.configure(text=self.secs)
            self.window.after(1000, self.go)


if __name__ == '__main__':
    timer = Timer()
    timer.start()
    timer.ml()