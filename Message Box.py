from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("500x500")
def msg():
    messagebox.showwarning("Alert", "OH nooo! VIRUS has been FOUND. AKRAMAND!!!!")
button=Button(root, text="OH no please don't scan the virus. PLEASE DON'T!!!", width=50, command=msg)
button.place(x=40, y=80)

root.mainloop()