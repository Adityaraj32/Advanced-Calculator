from tkinter import *
root = Tk()
root.geometry("644x700")
# root.minsize("644x700")
# root.maxsize("644x700")
root.title("Calculator")
root.wm_iconbitmap("Calculator.ico")

def click(event):
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Error!"
                scvalue.set(value)
                screen.update()
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text )
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=4, pady=1, padx=1)

f = Frame(root, bg="grey")
f.pack()

b = Button(f, text="9", font="lucida 35 bold",padx=5,pady=2.5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="8", font="lucida 35 bold",padx=5,pady=2.5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="7", font="lucida 35 bold",padx=5,pady=2.5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

f = Frame(root, bg="grey")
f.pack()
b = Button(f, text="6", font="lucida 35 bold",padx=5,pady=2.5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="5", font="lucida 35 bold",padx=5,pady=2.5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="4", font="lucida 35 bold",padx=5,pady=2.5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

f = Frame(root, bg="grey")
f.pack()
b = Button(f, text="3", font="lucida 35 bold",padx=5,pady=4.5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="2", font="lucida 35 bold",padx=5,pady=4.5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="1", font="lucida 35 bold",padx=5,pady=4.5)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

f = Frame(root, bg="grey")
f.pack()


b = Button(f, text="+", font="lucida 36 bold",padx=5,pady=4.5)
b.pack(side=LEFT,padx=6.49,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="0", font="lucida 35 bold",padx=5,pady=4.5)
b.pack(side=LEFT,padx=6.49,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="-", font="lucida 36 bold",padx=5,pady=4.5)
b.pack(side=LEFT,padx=6.49,pady=5)
b.bind("<Button-1>", click)

f = Frame(root, bg="grey")
f.pack()

b = Button(f, text="/", font="lucida 35 bold",padx=5,pady=1)
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="*", font="lucida 35 bold",padx=5,pady=1)
b.pack(side=LEFT,padx=5.5,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="%", font="lucida 35 bold",padx=5,pady=1)
b.pack(side=LEFT,padx=5.5,pady=5)
b.bind("<Button-1>", click)

f = Frame(root, bg="grey")
f.pack()

b = Button(f, text="=", font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=5,pady=5.5)
b.bind("<Button-1>", click)

b = Button(f, text="C", font="lucida 35 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=5,pady=5.5)
b.bind("<Button-1>", click)

root.mainloop()