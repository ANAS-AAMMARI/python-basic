from tkinter import *

root = Tk()
root.title("Hello")

e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def btn_click(num):
    current = e.get()
    btn_empty()
    e.insert(0, str(current) + str(num))


def btn_empty():
    e.delete(0, END)


def btn_operator(d):
    global num1
    global op

    op = d
    num1 = int(e.get())
    btn_empty()


def btn_result():
    num2 = int(e.get())
    btn_empty()
    if op == "+":
        e.insert(0, num1 + num2)
    elif op == "*":
        e.insert(0, num1 * num2)
    elif op == "/":
        e.insert(0, num1 / num2)
    elif op == "-":
        e.insert(0, num1 - num2)


btn_1 = Button(root, text="1", padx=40, pady=20, command=lambda: btn_click(1))
btn_2 = Button(root, text="2", padx=40, pady=20, command=lambda: btn_click(2))
btn_3 = Button(root, text="3", padx=40, pady=20, command=lambda: btn_click(3))

btn_4 = Button(root, text="4", padx=40, pady=20, command=lambda: btn_click(4))
btn_5 = Button(root, text="5", padx=40, pady=20, command=lambda: btn_click(5))
btn_6 = Button(root, text="6", padx=40, pady=20, command=lambda: btn_click(6))

btn_7 = Button(root, text="7", padx=40, pady=20, command=lambda: btn_click(7))
btn_8 = Button(root, text="8", padx=40, pady=20, command=lambda: btn_click(8))
btn_9 = Button(root, text="9", padx=40, pady=20, command=lambda: btn_click(9))

btn_0 = Button(root, text="0", padx=40, pady=20, command=lambda: btn_click(0))
btn_clear = Button(root, text="clear", padx=30, pady=20, command=lambda: btn_empty())
btn_equal = Button(root, text="=", padx=40, pady=20, command=btn_result)

btn_add = Button(root, text="+", padx=40, pady=20, command=lambda: btn_operator("+"))
btn_sub = Button(root, text="-", padx=40, pady=20, command=lambda: btn_operator("-"))
btn_mul = Button(root, text="*", padx=40, pady=20, command=lambda: btn_operator("*"))
btn_div = Button(root, text="/", padx=40, pady=20, command=lambda: btn_operator("/"))

btn_1.grid(row=4, column=0)
btn_2.grid(row=4, column=1)
btn_3.grid(row=4, column=2)

btn_4.grid(row=3, column=0)
btn_5.grid(row=3, column=1)
btn_6.grid(row=3, column=2)

btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)

btn_0.grid(row=5, column=0)
btn_add.grid(row=6, column=0)
btn_clear.grid(row=1, column=2)

btn_equal.grid(row=6, column=2)
btn_mul.grid(row=5, column=1)
btn_sub.grid(row=6, column=1)
btn_div.grid(row=5, column=2)

mainloop()
