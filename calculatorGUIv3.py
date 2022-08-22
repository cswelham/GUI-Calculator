
#=======================================Imports==========================================#
            
from tkinter import *
from tkinter.ttk import *       #imports
import tutorialBox, informationBox, creationBox

#=======================================Text Update======================================#

"""
>>> defines module for updating text that includes buttons AC, Exit, =, C
"""

def text_update(number):
    status = Label(root, text=" Calculating ...", relief=SUNKEN, anchor=W, width=55).grid(row=10, column=0, columnspan=4)
    if number == "AC":
        clearNumber()   #go to clearNumber 
    elif number == "Exit":
        exitCalc()  #go to exitCalc
    elif number == "=":
        try:
            equationList=text.get() #get text from entry widget
            equationList = equationList.replace("×","*").replace("÷","/")
            equationList = str(''.join(equationList))
            equationAns = eval(str(equationList))   #evaluate text
            text.delete(0, END)
            text.insert(0, equationAns)
            status = Label(root, text=" Answer!", relief=SUNKEN, anchor=W, width=55).grid(row=10, column=0, columnspan=4)
        except Exception:   #except for all errors
            text.delete(0, END)
            error()
    elif number == "C":
        cancelNumber()  #go to cancel number
    else:
        total.append(number)
        text.insert((len(numList)*100), number)
        
#=======================================Delete Number====================================#

"""
>>> defines cancel number to remove one number from calculation
"""

def cancelNumber():
    equationList=text.get() #get text from entry widget
    equationList2=list(equationList)[:-1]   #remove last thing from entry widget
    equationList3=''.join(equationList2)
    text.delete(0, END)
    text.insert(0, equationList3)

#=======================================Clear Number=====================================#

"""
>>> defines clearing all the numbers in the entry widget
"""

def clearNumber():
    text.delete(0, END)
    status = Label(root, text=" Clear", relief=SUNKEN, anchor=W, width=55).grid(row=10, column=0, columnspan=4)

#=======================================Error============================================#

"""
>>> defines an error message that pops up when an error occurs
"""

def error():
    status = Label(root, text=" Error :(", relief=SUNKEN, anchor=W, width=55).grid(row=10, column=0, columnspan=4)
    tkinter.messagebox.showerror("Error", "Error")        

#=======================================Exit GUI=========================================#

"""
>>> defines closes window
"""

def exitCalc():
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
editMenu.add_command(label="Undo", command=cancelNumber)
editMenu.add_command(label="Clear", command=clearNumber)

#=======================================Status Bar=======================================#

status = Label(root, text=" Welcome. No need to think. Use the calculator.", relief=SUNKEN, anchor=W, width=55).grid(row=10, column=0, columnspan=4)

#=======================================Buttons==========================================#

numDict = {}

total = []

numCol = 0
numRow = 1
numList = ["Exit", "AC","C", "+",
        "7", "8", "9", "-",
        "4", "5", "6", "×",
        "1", "2", "3", "÷",
        "0", ".", "=",]
colDict = [4, 8, 12]

for number in numList:      #loop for buttons created
    action = lambda x = number: text_update(x)
    if number == "0":
        numDict[number] = (Button(root, text=number, command=action, width=25)).grid(row=numRow, column=numCol, pady=5, padx=5, columnspan=2)                         
        numCol += 1
    else:
        numDict[number] = (Button(root, text=number, command=action)).grid(row=numRow, column=numCol, pady=5, padx=5)                         
    numCol +=1
    if numCol in colDict:
        numRow += 1     #defines rows and columns for buttons
        numCol = 0

#=======================================Mainloop=========================================#

root.mainloop()

#=======================================End==============================================#
        
