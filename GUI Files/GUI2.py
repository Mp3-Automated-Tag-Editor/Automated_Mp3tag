from tkinter import *
import tkinter.font as tkFont
master = Tk()
master.title("AUTOMATED MP3 TAG EDITOR ")


def var_states():
    print("SELECTED  OPTIONS: %d,\nfemale: %d" % (var1.get(), var2.get(),var3.get()))


fontStyle = tkFont.Font(family="Lucida Grande", size=30)
Button(master, text="SELECT DIRECTORY  ", font=fontStyle, borderwidth=3,
       relief='solid').grid(row=0, sticky=W, pady=50, padx=50)

var1 = IntVar()
Checkbutton(master, text="HIGH RESOLUTION IMAGE", variable=var1,
            borderwidth=3, relief='solid').grid(row=1, sticky=W, padx=20, pady=10)
var2 = IntVar()
Checkbutton(master, text="DISPLAY FAILED ATTEMPTS/RESULTS", variable=var2,
            borderwidth=3, relief='solid').grid(row=2, sticky=W, padx=20, pady=10)
var3 = IntVar()
Checkbutton(master, text="ENABLE RANKED BASED MINING OF SONGS", variable=var3,
            borderwidth=3, relief='solid').grid(row=3, sticky=W, padx=20, pady=10)


Button(master, text='START', command=master.quit).grid(
    row=8, column=1, sticky=W, pady=40, padx=30)
Button(master, text='ADVANCED OPTION', command=var_states).grid(
    row=8, column=3, sticky=W, pady=40, padx=30)
mainloop()
