from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1440x1024")
window.configure(bg="#ffffff")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=1024,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

canvas.create_text(
    1123.0, 560.0,
    text="HIGH RESOLUTION IMAGE\n",
    fill="#000000",
    font=("None", int(24.0)))

canvas.create_text(
    1084.5, 647.5,
    text="Display Failed attempts/results",
    fill="#000000",
    font=("None", int(24.0)))

canvas.create_text(
    1085.5, 739.0,
    text="Enable Ranked based Mining of Songs",
    fill="#000000",
    font=("None", int(24.0)))

canvas.create_text(
    931.5, 911.5,
    text="START",
    fill="#000000",
    font=("None", int(24.0)))

canvas.create_text(
    1212.5, 911.5,
    text="ADVANCED OPTION",
    fill="#000000",
    font=("None", int(20.0)))

canvas.create_text(
    1311.5, 311.0,
    text="UPLOAD FILE",
    fill="#000000",
    font=("None", int(24.0)))

canvas.create_text(
    1159.0, 175.5,
    text="MP3 AUTOMATED TAG EDITOR",
    fill="#000000",
    font=("JacquesFrancoisShadow-Regular", int(40.0)))

window.resizable(False, False)
window.mainloop()
