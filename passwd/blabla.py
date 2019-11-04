from tkinter import*
from random import randint

root = Tk()
root.geometry("400x170")
root.title("Password generator!!!")
root.resizable(width=False, height=False)


def pswd_gen():
    tmp = StringVar()
    if pointer.get() == 0:
        tmp.set("12345678901234567890")
    if pointer.get() == 1:
        tmp.set("qwertyuiopasdfghjklzxcvbnm")
    if pointer.get() == 2:
        tmp.set("qwertyuiopasdfghjklzxcvbnm12345678901234567890")
    pwd = ""
    tmp = str(tmp.get())
    ###########################################################
    for i in range(0, pwd_len.get()):
        pwd += tmp[randint(0, len(tmp)-1)]
    vr.set("Password: " + pwd)
###########################################################


vr = StringVar()

lab1 = Label(text="Enter length:")
lab1.pack()
pwd_len = IntVar()
Entry(textvariable=pwd_len).pack()


pointer = IntVar()
rd1 = Radiobutton(variable=pointer, text="Only numbers", value=int(0))
rd1.pack()
rd2 = Radiobutton(variable=pointer, text="Only characters", value=int(1))
rd2.pack()
rd3 = Radiobutton(variable=pointer, text="Numbers and characters", value=int(2))
rd3.pack()

but = Button(text="Generate", command=pswd_gen)
but.pack()


res = Label(textvariable=vr)
res.pack(side=BOTTOM)


root.mainloop()