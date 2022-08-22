from tkinter import *   #imports

"""
>>> defines a place holder that doesn't do anything when button clicked
"""

def refresh():
    text.delete(0,END)
    return

root = Tk()
frame = Frame(root) #creating a frame
frame.pack()

frame2 = Frame(root)
frame2.pack(side=TOP)

text=Entry(frame)
text.pack()

button1 = Button(frame2, padx=10, pady=10, text="1", fg="blue")
button1.pack(side=LEFT)
button2 = Button(frame2, padx=10, pady=10, text="2", fg="blue")     #creating buttons manually
button2.pack(side=LEFT)
button3 = Button(frame2, padx=10, pady=10, text="3", fg="blue")
button3.pack(side=LEFT)
buttonDivide = Button(frame2, padx=10, pady=10, text="/", fg="black")
buttonDivide.pack(side=LEFT)

frame3 = Frame(root)    #packing buttons into frame
frame3.pack(side=TOP)

button4 = Button(frame3, padx=10, pady=10, text="4", fg="blue")
button4.pack(side=LEFT)
button5 = Button(frame3, padx=10, pady=10, text="5", fg="blue")
button5.pack(side=LEFT)
button6 = Button(frame3, padx=10, pady=10, text="6", fg="blue")
button6.pack(side=LEFT)
buttonMultiply = Button(frame3, padx=10, pady=10, text="*", fg="black")
buttonMultiply.pack(side=LEFT)

frame4 = Frame(root)
frame4.pack(side=TOP)

button7 = Button(frame4, padx=10, pady=10, text="7", fg="blue")
button7.pack(side=LEFT)
button8 = Button(frame4, padx=10, pady=10, text="8", fg="blue")
button8.pack(side=LEFT)
button9 = Button(frame4, padx=10, pady=10, text="9", fg="blue")
button9.pack(side=LEFT)
buttonMinus = Button(frame4, padx=10, pady=10, text="-", fg="black")
buttonMinus.pack(side=LEFT)

frame5 = Frame(root)
frame5.pack(side=TOP)

button0 = Button(frame5, padx=10, pady=10, text="0", fg="blue")
button0.pack(side=LEFT)
buttonAC = Button(frame5, padx=10, pady=10, text="AC", fg="red", command=refresh)
buttonAC.pack(side=LEFT)
buttonAdd = Button(frame5, padx=10, pady=10, text="+", fg="black")
buttonAdd.pack(side=LEFT)
buttonEqual = Button(frame5, padx=10, pady=10, text="=", fg="black")
buttonEqual.pack(side=LEFT)

root.mainloop()

     
