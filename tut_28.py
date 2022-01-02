from tkinter import *
root = Tk()
root.geometry("644x900")
root.title("Calculator")
# root.wm_iconbitmap("Calculator.ioc")

def click(event):
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        pass
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text )
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=2, padx=5)

f = Frame(root, bg="grey")
f.pack()

b = Button(f, text="9", font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="8", font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="7", font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

f = Frame(root, bg="grey")
f.pack()
b = Button(f, text="6", font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="5", font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="4", font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

f = Frame(root, bg="grey")
f.pack()
b = Button(f, text="3", font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="2", font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="1", font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

f = Frame(root, bg="grey")
f.pack()
b = Button(f, text="0", font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="+", font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="-", font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

f = Frame(root, bg="grey")
f.pack()
b = Button(f, text="/", font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="*", font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="%", font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

f = Frame(root, bg="grey")
f.pack()

b = Button(f, text="C", font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>", click)

root.mainloop()