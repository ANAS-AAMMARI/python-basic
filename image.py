from tkinter import *


def empty():
    e.delete(0, END)


def write(d):
    current = e.get()
    empty()
    e.insert(0, str(current) + str(d))


def operation(d):
    # global num1
    # num1 = float(e.get())
    global x
    x = d
    write(d)


def result():
    # num2 = float(e.get())
    num = str(e.get()).split(x)
    # print(num)
    num1 = float(num[0])
    num2 = float(num[1])
    # empty()
    if x == "+":
        st = "= %d" % (num1 + num2)
        write(st)
    elif x == "*":
        st = f"= {num1 * num2}"
        write(st)
    elif x == "-":
        st = f"= {num1 - num2}"
        write(st)
    elif x == "/":
        st = f"= {num1 / num2}"
        write(st)


root = Tk()
height = 400
width = 300
canvas = Canvas(root, height=height, width=width)
canvas.pack()

frame = Frame(root, bg='#80c1ff')
frame.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.95, anchor='n')

e = Entry(frame, font=60)
e.place(relx=0.5, rely=0.1, anchor='n', relheight=0.8, relwidth=0.969)

frame1 = Frame(root, bg='#80c1ff')
frame1.place(relx=0.5, rely=0.22, relheight=0.7, relwidth=0.95, anchor='n')

btn7 = Button(frame1, text="7", bg="#faf4f4", borderwidth=0, font=40, command=lambda: write(7))
btn7.place(relx=0.15, rely=0.05, relheight=0.15, relwidth=0.2, anchor='n')

btn8 = Button(frame1, text="8", bg="#faf4f4", borderwidth=0, font=40, command=lambda: write(8))
btn8.place(relx=0.38, rely=0.05, relheight=0.15, relwidth=0.2, anchor='n')

btn9 = Button(frame1, text="9", bg="#faf4f4", borderwidth=0, font=40, command=lambda: write(9))
btn9.place(relx=0.61, rely=0.05, relheight=0.15, relwidth=0.2, anchor='n')

btn_dev = Button(frame1, text="/", bg="black", fg="white", borderwidth=0, font=40, command=lambda: operation("/"))
btn_dev.place(relx=0.84, rely=0.05, relheight=0.15, relwidth=0.2, anchor='n')

btn4 = Button(frame1, text="4", bg="#faf4f4", borderwidth=0, font=40, command=lambda: write(4))
btn4.place(relx=0.15, rely=0.25, relheight=0.15, relwidth=0.2, anchor='n')

btn5 = Button(frame1, text="5", bg="#faf4f4", borderwidth=0, font=40, command=lambda: write(5))
btn5.place(relx=0.38, rely=0.25, relheight=0.15, relwidth=0.2, anchor='n')

btn6 = Button(frame1, text="6", bg="#faf4f4", borderwidth=0, font=40, command=lambda: write(6))
btn6.place(relx=0.61, rely=0.25, relheight=0.15, relwidth=0.2, anchor='n')

btn_mul = Button(frame1, text="*", bg="black", fg="white", borderwidth=0, font=40, command=lambda: operation("*"))
btn_mul.place(relx=0.84, rely=0.25, relheight=0.15, relwidth=0.2, anchor='n')

btn1 = Button(frame1, text="1", bg="#faf4f4", borderwidth=0, font=40, command=lambda: write(1))
btn1.place(relx=0.15, rely=0.45, relheight=0.15, relwidth=0.2, anchor='n')

btn2 = Button(frame1, text="2", bg="#faf4f4", borderwidth=0, font=40, command=lambda: write(2))
btn2.place(relx=0.38, rely=0.45, relheight=0.15, relwidth=0.2, anchor='n')

btn3 = Button(frame1, text="3", bg="#faf4f4", borderwidth=0, font=40, command=lambda: write(3))
btn3.place(relx=0.61, rely=0.45, relheight=0.15, relwidth=0.2, anchor='n')

btn_sub = Button(frame1, text="-", bg="black", fg="white", borderwidth=0, font=40, command=lambda: operation("-"))
btn_sub.place(relx=0.84, rely=0.45, relheight=0.15, relwidth=0.2, anchor='n')

btn0 = Button(frame1, text="0", bg="#faf4f4", borderwidth=0, font=40, command=lambda: write(0))
btn0.place(relx=0.15, rely=0.65, relheight=0.15, relwidth=0.2, anchor='n')

btn_pnt = Button(frame1, text=".", bg="#faf4f4", borderwidth=0, font=("calibre", 20), command=lambda: write("."))
btn_pnt.place(relx=0.38, rely=0.65, relheight=0.15, relwidth=0.2, anchor='n')

btn_equal = Button(frame1, text="=", bg="#faf4f4", borderwidth=0, font=40, command=result)
btn_equal.place(relx=0.61, rely=0.65, relheight=0.15, relwidth=0.2, anchor='n')

btn_add = Button(frame1, text="+", bg="black", fg="white", borderwidth=0, font=40, command=lambda: operation("+"))
btn_add.place(relx=0.84, rely=0.65, relheight=0.15, relwidth=0.2, anchor='n')

lbl = Label(frame1, text="Created By ANAS AAMMARI", font=("Kristen ITC", 12), fg="black", bg="#80c1ff")
lbl.place(relx=0.5, rely=0.85, anchor='n')
root.mainloop()
