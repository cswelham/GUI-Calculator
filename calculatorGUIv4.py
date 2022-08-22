
#=======================================Imports==========================================#
            
from tkinter import *
from tkinter.ttk import *   #imports
import tutorialBox, informationBox, creationBox

#=======================================Text Update======================================#

"""
>>> defines module for updating text that includes buttons AC, Exit, =, C
"""

def textUpdate(number):
    global equationList
    text.configure(state="normal")
    status = Label(root, text=" Inputing ...", relief=SUNKEN, anchor=W, width=55).grid(row=10, column=0, columnspan=4)
    if number == "AC":
        clearNumber()   #go to clearNumber
    elif number == "Exit":
        exitCalc()  #go to exitCalc
    elif number == "⌫":
        cancelNumber()  #go to cancel Number
    elif number == "=":
        try: 
            equationList=text.get() #get text from entry widget
            equationList = equationList.replace("×"," * ").replace("÷"," / ").replace("+", " + ").replace("-", " - ")
            equationList = str(''.join(equationList))
            equationAns = eval(' '.join(str(int(x)) if x.isdigit() else x for x in equationList.split()))   #strips of leading zeroes
            text.delete(0, END)
            text.insert(0, equationAns)
            status = Label(root, text=" Answer!", relief=SUNKEN, anchor=W, width=55).grid(row=10, column=0, columnspan=4)
            text.configure(state="disabled")
        except Exception:   #except for all errors
            text.delete(0, END)
            error() 
    else:
        text.insert((len(numList)*100), number)
        text.configure(state="disabled")

#=======================================Key Press========================================#

"""
>>> key binding all keys
"""

def keyPress(event):
    possibleKeys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                    'Return', 'plus', 'minus', 'slash', 'asterisk',
                    'period', 'BackSpace']
    if event.keysym in possibleKeys:
        textUpdate(event.keysym.replace('Return', '=').replace('plus', '+').replace('minus', '-')
                               .replace('slash', '/').replace('asterisk', '*').replace('period', '.')
                               .replace('BackSpace', '⌫'))

#=======================================Cancel Number====================================#

"""
>>> defines cancel number to remove one number from calculation
"""


def cancelNumber():
    global equationList
    equationList=text.get() #get text from entry widget
    equationList2=list(equationList)[:-1]   #remove last thing from entry widget
    equationList3=''.join(equationList2)
    text.delete(0, END)
    text.insert(0, equationList3)
    text.configure(state="disabled")

#=======================================Clear Number=====================================#

"""
>>> defines clearing all the numbers in the entry widget
"""


def clearNumber():
    text.delete(0, END)
    status = Label(root, text=" Clear", relief=SUNKEN, anchor=W, width=55).grid(row=10, column=0, columnspan=4)
    text.configure(state="disabled")

#=======================================Error Box========================================#

"""
>>> defines an error message that pops up when an error occurs
"""

def error():
    status = Label(root, text=" Error :(", relief=SUNKEN, anchor=W, width=55).grid(row=10, column=0, columnspan=4)
    tkinter.messagebox.showerror("Error", "Error")
    text.configure(state="disabled")

#=======================================Exit GUI=========================================#

"""
>>> defines closes window
"""


def exitCalc():
    text.configure(state="normal")
    root.destroy()

#=======================================Message Boxes====================================#

"""
>>> defines the taskbar message boxes
"""


def tutorial():    
    status = Label(root, text=" Message Box ...", relief=SUNKEN, anchor=W, width=55).grid(row=10, column=0, columnspan=4)
    tutorialBox.tutorialBox()

def information():
    status = Label(root, text=" Message Box ...", relief=SUNKEN, anchor=W, width=55).grid(row=10, column=0, columnspan=4)
    informationBox.informationBox()

def creation():
    status = Label(root, text=" Message Box ...", relief=SUNKEN, anchor=W, width=55).grid(row=10, column=0, columnspan=4)
    creationBox.creationBox()

#=======================================Title and Entry==================================#

root = Tk()
root.title("Calculator")
text = Entry(root, width = 35, justify='right', font='copperplate')
text.configure(state="disabled")
text.grid(row=0, column=0, columnspan=5)

#=======================================Tool Bar=========================================#

"""
>>> defines the taskbar being added
"""
    
menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="Tutorial", command=tutorial)
subMenu.add_command(label="Information", command=information)
subMenu.add_command(label="Creation", command=creation)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=exitCalc)
editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Delete", command=cancelNumber)
editMenu.add_command(label="Clear", command=clearNumber)

#=======================================Status Bar=======================================#

status = Label(root, text=" Welcome. No need to think. Use the four function calculator.", relief=SUNKEN, anchor=W, width=55).grid(row=10, column=0, columnspan=4)

#=======================================Key Binding======================================#

root.bind("<Key>", keyPress)
 
#=======================================Buttons==========================================#

numDict = {}

numCol = 0
numRow = 1
numList = ["Exit", "AC", "⌫", "+",
            "7", "8", "9", "-",
            "4", "5", "6", "×",
            "1", "2", "3", "÷",
            "0", ".", "=",]
colDict = [4, 8, 12]

for number in numList:  #loop for buttons created
    action = lambda x = number: textUpdate(x)   #sets action to update text
    if number == "0":
        numDict[number] = (Button(root, text=number, command=action, width=25)).grid(row=numRow, column=numCol, pady=5, padx=5, columnspan=2)                         
        numCol += 1
    else:
        numDict[number] = (Button(root, text=number, command=action)).grid(row=numRow, column=numCol, pady=5, padx=5)                         
    numCol +=1
    if numCol in colDict:
        numRow += 1     #rows and columns for button layout
        numCol = 0

#=======================================Mainloop=========================================#

root.mainloop()

#=======================================End==============================================#
        
