from tkinter import *
import tkinter.font as tkFont

master = Tk()
master.title("AUTOMATED MP3 RAG EDITOR -Advanced option")


def var_states():
    print("SELECTED ADVANCED  OPTIONS: %d,\nfemale: %d" % (var1.get(),
          var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get()))


fontStyle = tkFont.Font(family="Lucida Grande", size=30)
Label(master, text="ADVANCED OPTIONS", font=fontStyle, borderwidth=3,
      relief='solid').grid(row=0, sticky=W, pady=50, padx=50)
var1 = IntVar()
Checkbutton(master, text="ADD TITLE", variable=var1).grid(
    row=1, sticky=W, pady=20, padx=20)
var2 = IntVar()
Checkbutton(master, text="ADD ARTIST", variable=var2).grid(
    row=2, sticky=W, pady=10, padx=20)
var3 = IntVar()
Checkbutton(master, text="ADD YEAR", variable=var3).grid(
    row=3, sticky=W, pady=10, padx=20)
var4 = IntVar()
Checkbutton(master, text="ADD TRACK", variable=var4).grid(
    row=4, sticky=W, pady=10, padx=20)
var5 = IntVar()
Checkbutton(master, text="ADD GENRE", variable=var5).grid(
    row=5, sticky=W, pady=10, padx=20)
var6 = IntVar()
Checkbutton(master, text="ADD COMPOSER", variable=var2).grid(
    row=6, sticky=W, pady=10, padx=20)
var7 = IntVar()
Checkbutton(master, text="ADD DISC NUMBER", variable=var2).grid(
    row=7, sticky=W, pady=10, padx=20)
Button(master, text='START', command=master.quit, borderwidth=3,
       relief='solid').grid(row=8, column=0, sticky=W, pady=40)
Button(master, text='BACK', command=var_states, borderwidth=3,
       relief='solid').grid(row=8, column=5, sticky=W, pady=40)
mainloop()
