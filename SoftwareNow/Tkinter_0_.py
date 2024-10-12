from tkinter import *
root=Tk()
thelabel=Label(root, text='Hello World!')
thelabel.pack()

topFrame=Frame(root)
topFrame.pack()

one=Label(root, text="ONE", bg="red", fg="white")
one.pack()
two=Label(root, text="TWO", bg="green", fg="black")
two.pack(fill=X)

bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)
three=Label(root, text="THREE", bg="blue", fg="white")
three.pack(side=RIGHT, fill=BOTH)

button1= Button(topFrame, text="Button 1", fg="red")
button2= Button(topFrame, text="Button 2", fg="green")
button3= Button(topFrame, text="Button 3", fg="blue")
button4= Button (bottomFrame, text="Button 4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()