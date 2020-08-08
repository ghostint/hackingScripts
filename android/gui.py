from tkinter import *
from functools import partial


root = Tk()
# def fun():
# 	messagebox.showinfo("Hello", "Button clicked")
# redButton = Button(root, text="Red", fg="red", activeforeground="green", activebackground="black", command=fun)
# redButton.pack(side=LEFT)


# blueButton = Button(root, text="Blue", fg="blue")
# blueButton.pack(side=RIGHT)


# greenButton = Button(root, text="Green", fg="green")
# greenButton.pack(side=TOP)


# blackButton = Button(root, text="Black", fg="black")
# blackButton.pack(side=BOTTOM)


# name = Label(root, text="Name:").grid(row=0,column=0)
# e1 = Entry(root).grid(row=0, column=1)




# passw = Label(root, text="Password:").grid(row=1,column=0)
# e1 = Entry(root).grid(row=1, column=1)
# submit = Button(root, text="Submit").grid(row=4, column=0)

# python = IntVar()
# Javascript = IntVar()
# golang = IntVar()
# cpp = IntVar()
# php = IntVar()


# lang1 = Checkbutton(root, text="Python", variable=python,bg="black", fg="green")
# lang1.grid(row=0, column=0)

# lang2 = Checkbutton(root, text="Javascript", variable=Javascript,bg="black", fg="green")
# lang2.grid(row=1, column=0)

# lang4 = Checkbutton(root, text="Golang", variable=golang ,bg="black", fg="green")
# lang4.grid(row=2, column=0)

# lang3 = Checkbutton(root, text="C++", bg="black", variable=cpp ,fg="green")
# lang3.grid(row=3, column=0)

# lang5 = Checkbutton(root, text="PHP", variable=php ,bg="black", fg="green")
# lang5.grid(row=4, column=0)



# ======================= Simple Calculator ==========================


# def Calc(resultLabel, inp1, inp2):

# 	x = int(inp1.get())
# 	y = int(inp2.get())
# 	res = x+y

# 	resultLabel.config(text="Result is: %d"%res)
# 	return 


# x = StringVar()
# y = StringVar()

# label1 = Label(root,text="First Number: ").grid(row=0, column=0)
# val1 = Entry(root, textvariable=x).grid(row=0, column=1)

# label2 = Label(root,text="Second Number: ").grid(row=1, column=0)
# val2 = Entry(root, textvariable=y).grid(row=1, column=1)

# resultLabel = Label(root)
# resultLabel.grid(row=4, column=0)

# Calc = partial(Calc, resultLabel, x, y)

# calc = Button(root, command=Calc, text="Calculate").grid(row=3, column=0)


# ===================== TODO LIST =====================================

index = StringVar()
item = StringVar()

def add(box, index, item):
	index = int(index.get())
	item = str(item.get())
	box.insert(index, item)

	return

lable1 = Label(root, text="Enter the Index: ").grid(row=0, column=0)
ent1 = Entry(root, textvariable=index).grid(row=0, column=1)

lable2 = Label(root, text="Item to insert: ").grid(row=1, column=0)
ent2 = Entry(root, textvariable=item).grid(row=1, column=1)



label = Label(root, text="A list box Practice.")
box = Listbox(root)
box.grid(row=5, column=0)
box.insert(1, "Python")
box.insert(2, "Golang")
box.insert(3, "Javascript")

add = partial(add, box, index, item)

btn = Button(root, text="Add", command=add)
btn.grid(row=2, column=0)

btnRem = Button(root, text="Remove", command=lambda box=box:box.delete(ANCHOR))
btnRem.grid(row=2, column=1)



root.mainloop()
