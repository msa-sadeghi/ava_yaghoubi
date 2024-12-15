from tkinter import *
def enter_func(e):
    exit_button.config({
        "bg":"red",
        'fg' : 'white',
        'padx':20,
        'pady':5,
        'font':15
    })
def leave_func(e):
    exit_button.config({
        "bg":"white",
        'fg' : 'black',
        'padx': 0,
        'pady':0,
        'font':10
    })


window = Tk()
window.geometry("300x360")
window.config(bg="black")
user_frame = Frame(window, bg="black")
user_frame.pack(anchor="w", fill="x", padx=30, pady=15)

Label(user_frame, text="username", fg="white", bg="black").pack(side="left")
user_entry = Entry(user_frame, width=20, bg="gray")
user_entry.pack(side="right")

pass_frame = Frame(window, bg="black")
pass_frame.pack(anchor="w", fill="x", padx=30, pady=15)

Label(pass_frame, text="password", fg="white", bg="black").pack(side="left")
pass_entry = Entry(pass_frame, width=20, bg="gray")
pass_entry.pack(side="right")

exit_button = Button(window, text="exit", fg="red", bg="black", activebackground="green")
exit_button.pack()
exit_button.bind("<Enter>", enter_func)
exit_button.bind("<Leave>", leave_func)



window.mainloop()