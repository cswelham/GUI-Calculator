
from tkinter import *   #imports

"""
>>> defines text update which occurs when a buttons is pressed.
>>> used for all buttons as well as equals button
"""

def text_update(number):
    if number == "=":
        equationList=text.get()
        equationAns = eval(str(equationList))
        text.delete(0, END)
        text.insert(0, equationAns)        
    elif number == "X":
        number = "*"
        text.insert(len(numList), number)
    elif number == "÷":
        number = "/"
        text.insert(len(numList), number)
    else:
        text.insert(len(numList), number)

root = Tk()
root.title("Calculator")
text = Entry(root, width = 35, justify='center', font='copperplate')    #entry widget
text.grid(row=0, column=0, columnspan=5)

numDict = {}
numCol = 0
numRow = 1
numList = ["7", "8", "9", "X",
        "4", "5", "6", "÷",
        "1", "2", "3", "-",
        "0", "=", "+",
        ".", "AC","C", "Exit",]
colDict = [4, 8, 12]

for number in numList:
    action = lambda x = number: text_update(x)      #loop to create buttons
    numDict[number] = (Button(root, text=number, command=action)).grid(row=numRow, column=numCol, pady=5, padx=5)                         
    numCol +=1
    if numCol in colDict:
        numRow += 1     #sets rows and coloumns as buttons are created
        numCol = 0

root.mainloop()

        
