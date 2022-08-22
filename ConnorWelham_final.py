
#=======================================Imports==========================================#
            
from tkinter import *   #imports tkinter for GUI
import tkinter.messagebox
import tutorialBox, informationBox, creationBox   #imports other module 

#=======================================Calculator Class=================================#

class Calculator(): #sets class as calculator

#=======================================Initialse Calculator GUI=========================#

    """
    >>> initialise with self and parent
    """
    
    def __init__(self,parent):  #defines initialise class with self and parent
    
        entryFont = ('Comic Sans MS',22, 'bold')
        self.labelFont = ('Comic Sans MS',10, 'bold')   #creating global variable fonts
        buttonFont = ('Comic Sans MS', 18)
        
        parent.title("Calculator")  #sets title of window
        self.text = Entry(parent, width = 24, justify='right', font=entryFont, bd=5)    #creates global entry widget
        self.text.configure(state="disabled")
        self.text.grid(row=0, column=0, columnspan=4)   #creates a global grid for the buttons
        parent.resizable(0,0)   #makes it so the calculator can't be resized
        
        parent.bind("<Key>", self.keyPress) #key binding a key to the module keyPress
        self.replacingKey = {'Return':'=', 'plus':'+', 'minus':'-', 'slash':'÷', 'asterisk':'×', 'period':'.',
                     'BackSpace':'⌫', 'Delete':'AC', 'Escape':'EXIT', 'equal':'='}
        self.possibleKeys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                        'Return', 'plus', 'minus', 'slash', 'asterisk',         #list of global keys to be binded
                        'period', 'BackSpace', 'Delete', 'Escape', 'equal']
        self.replacingCommon = {'×':' * ', '÷':' / ', '+':' + ', '-':' - '}
        
        status = Label(parent, text="Four Function Calculator", relief=SUNKEN, anchor=E, width=56,    #creates a local status bar
                       font=self.labelFont, bg="grey").grid(row=10, column=0, columnspan=4)

        menu = Menu(parent)
        parent.config(menu=menu)
        subMenu = Menu(menu)
        menu.add_cascade(label="Help", menu=subMenu)
        subMenu.add_command(label="Tutorial", command=self.tutorial)    #creates a first local toolbar
        subMenu.add_command(label="Information", command=self.information)
        subMenu.add_command(label="Creation", command=self.creation)
        subMenu.add_separator()
        subMenu.add_command(label="Exit", command=self.exitCalc)
        editMenu = Menu(menu)
        menu.add_cascade(label="Edit", menu=editMenu)
        editMenu.add_command(label="Delete", command=self.cancelNumber) #creates a second local toolbar 
        editMenu.add_command(label="Clear", command=self.clearNumber)

        numDict = {}        
        numCol = 0
        numRow = 1
        self.numList = ["EXIT", "AC", "⌫", "+",
                        "7", "8", "9", "-",
                        "4", "5", "6", "×",     #list of global buttons to be created
                        "1", "2", "3", "÷",
                        "0", ".", "=",]
        
        for number in self.numList: #for each local number in the list of global buttons
            if numCol == 4: 
                numRow += 1     #add one to existing number
                numCol = 0
            action = lambda x = number: self.buttonPress(x) #when action called go to global buttonPress
            operatorButtons = ["+", "-", "×", "÷"]
            topButtons = ["EXIT", "AC", "⌫"]
            if number == "=":
                numDict[number] = (Button(parent, text=number, font=buttonFont, command=action, bg="yellow2",       #creates button for = 
                                          fg="black", bd=6).grid(row=numRow, column=numCol, columnspan=2, sticky=NSEW))
                numCol += 1
            elif number in operatorButtons:
                numDict[number] = (Button(parent, text=number, font=buttonFont, command=action, bg="yellow2",   #creates button for the operators, 6699ff
                                          fg="black", bd=6).grid(row=numRow, column=numCol, sticky=NSEW))
                numCol += 1
            else:
                numDict[number] = (Button(parent, text=number, font=buttonFont, command=action, bg="gray12",      #creates buttons for any other numbers/symbols
                                          fg="white", bd=6).grid(row=numRow, column=numCol, sticky=NSEW))
                numCol +=1

#=======================================Button Pressed===================================#

    """
    >>> defines module for special buttons and which module to go to
    """
    
    def buttonPress(self, number):
        self.text.configure(state="normal")
        if number == "AC":
            self.clearNumber()      #if AC is clicked go to the global clear number module
        elif number == "EXIT":
            self.exitCalc()         #if EXIT is clicked go to global exit calc module
        elif number == "⌫":
            self.cancelNumber()     #if delete button is clicked go to global cancel number module
        elif number == "=":
            self.textUpdate()
        else:
            self.text.insert((len(self.numList)*100), number)       #insert text of button into the global entry widget
            self.text.configure(state="disabled")

#=======================================Message Boxes====================================#

    """
    >>> defines message boxes for taskbar
    """

    def tutorial(self):
        tutorialBox.tutorialBox()   #go to imported module tutorial box

    def information(self):
        informationBox.informationBox() #go to imported module history box

    def creation(self):
        creationBox.creationBox() #go to imported module inofrmation box

#=======================================Exit=============================================#

    """
    >>> defines exiting calculator
    """
       
    def exitCalc(self):
        self.text.configure(state="normal")
        root.destroy()      #exit out of the application

#=======================================Logic Class======================================#
        
class Logic(Calculator):        #class of logic called in calculator

#=======================================Calculating Answer===============================#

    """
    >>> defines module for updating text that includes buttons AC, Exit, =, C
    """
    
    def textUpdate(self):
        self.equationList=self.text.get()   #get text in global entry widget
        self.text.configure(state="disabled")
        if len(self.equationList) > 0:
            try:
                self.text.configure(state="normal")
                for key, replacement in self.replacingCommon.items(): #for local key,replacement in global replacing
                    self.equationList = self.equationList.replace(key, replacement)   #replace the key,replacement in local pressKey
                self.equationList = str(''.join(self.equationList))     #join it together in a string
                self.equationAns = eval(' '.join(str(int(x)) if x.isdigit() else x for x in self.equationList.split())) #remove or leading zeroes and calculate answer
                self.equationAns = round(self.equationAns, 2)   #rounds answer to 2 decimal places
                self.text.delete(0, END)    #delete text in global entry widget
                self.text.insert(0, self.equationAns)   #insert global answer
                self.text.configure(state="disabled")
            except Exception:   #don't do the above if there is an error
                self.text.delete(0, END)    #delete text in global entry widget
                self.error()    #go to global error module

#=======================================Key Binding======================================#


    """
    >>> key binding all keys
    """

    def keyPress(self, event):
        if event.keysym in self.possibleKeys:   #if key pressed is in global list of keys
            pressKey = event.keysym 
            for key, replacement in self.replacingKey.items(): #for local key,replacement in global replacing
                pressKey = pressKey.replace(key, replacement)   #replace the key,replacement in local pressKey
            self.buttonPress(pressKey)  #go to global buttonPress with local pressKey

#=======================================Cancel Number====================================#

    """
    >>> defines cancel number to remove one number from calculation
    """

    def cancelNumber(self):
        self.text.configure(state="normal")
        self.equationList=self.text.get()   #get text in global entry widget
        self.equationList2=list(self.equationList)[:-1] #delete last number of list
        self.equationList3=''.join(self.equationList2)  #join it together in a string
        self.text.delete(0, END)    #delete text in global entry widget
        self.text.insert(0, self.equationList3) #insert new text
        self.text.configure(state="disabled")

#=======================================Clear Number=====================================#

    """
    >>> defines clearing all the numbers in the entry widget
    """

    def clearNumber(self):
        self.text.configure(state="normal")
        self.text.delete(0, END)    #delete text in global entry widget
        self.text.configure(state="disabled")

#=======================================Error============================================#

    """
    >>> defines an error message that pops up when an error occurs
    """

    def error(self):
        self.text.configure(state="disabled")
        tkinter.messagebox.showerror("Error", "Error")  #pop up error message
        
        
#=======================================Main Routine=====================================#

    """
    >>> runs the GUI
    """

if __name__ == "__main__":
    root = Tk()
    test = Logic(root)  

#=======================================End==============================================#
        
