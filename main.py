from tkinter import filedialog
from tkinter import *
from tkinter.ttk import Progressbar
import tkinter as tk
import subprocess as sub
import time

def browse_button():
    filename = filedialog.askdirectory()
    global folder_path 
    folder_path = filename
    T.delete("1.0","end")
    T.insert(tk.END, folder_path) 

def start():
    import index
    txt = "Please Wait..."
    l = Label(frame1, text = txt)
    l.pack
    index.run_index(folder_path,T)
    print("Completed Successfully: Elapsed Time:" )

def close_win():
   root.destroy()

def step():
    for i in range(5):
        root.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)

txt="Instructions"

root = Tk()
root.title("Mp3 Automated Tag Editor - v1.0")
root.geometry("600x340")
root.protocol("WM_DELETE_WINDOW", close_win)

frame1 = LabelFrame(root, padx=10, pady=10)
frame1.grid(row=0, column=0, padx=7.5, pady=10)
  
T = Text(frame1, height = 14, width = 41, font =("Courier", 10), wrap=WORD)
# Create label
l = Label(frame1, text = txt)
l.config(font =("Courier", 14))
Fact = """Welcome to the Mp3 Automated Tag Editor v1.0. Please read the given instructions carefully.
        
*Insert Instructions*
*User Documentation*

Version: 1.0
Authors: Jonathan R Samuel (20BCT0332)
         Shivansh Sahai (20BCT0236)

Course: CSE3001(EPJ) - Dr. Swarnlatha P
"""
pb1 = Progressbar(frame1, orient=HORIZONTAL, length=300, mode='determinate')
pb1["value"]=0

l.pack()
T.pack()
pb1.pack(expand=True, pady=10)

T.insert(tk.END, Fact)

  
# Constructing the frame2
frame2 = LabelFrame(root, padx=10, pady=10)
frame2.grid(row=0, column=1, padx=7.5, pady=10)

C1 = Checkbutton(frame2, text = "High Resolution Image", width=20, anchor="w")
C1.pack(padx=10, pady=5)

C2 = Checkbutton(frame2, text = "Open both Directories", width=20, anchor="w")
C2.pack(padx=10, pady=5)

C3 = Checkbutton(frame2, text = "Extended Metadata", width=20, anchor="w")
C3.pack(padx=10, pady=5)

b1 = Button(frame2, text="Select Directory", command=browse_button)
b1.pack(padx=10, pady=10)
b2 = Button(frame2, text="START", command=start)
b2.pack(padx=10, pady=10)


root.mainloop()



#----------------------------------------------------------------------------------------

