# from tkinter import *
import tkinter

def click():
    my_label.configure(text="خداحافظ همگی")
    
window = tkinter.Tk()
window.title("my app")
window.configure(bg="black")
window.geometry("300x320")

my_label = tkinter.Label(window, text="سلام به همه",bg="black",fg="white", font=("arial", 22))
my_label.pack()

button_frame = tkinter.Frame(window, bg="black")
button_frame.pack(pady=50)

tkinter.Button(button_frame, text="تایید", command=click).pack(pady=10, padx=10, side="left")
tkinter.Button(button_frame, text="خروج", command=window.destroy).pack(pady=10, side="right", padx=10)

username_entry = tkinter.Entry(window)
username_entry.pack()

window.mainloop()