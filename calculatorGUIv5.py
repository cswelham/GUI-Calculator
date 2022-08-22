            
from tkinter import *   #imports
from tkinter.ttk import *

class Calculator:   #sets class as calculator

    """
    >>> initialise with self and parent
    """
    
    def __init__(self, parent):

        parent.title("Calculator")
        self.text = Entry(parent, width = 35, justify='right', font='copperplate')
        self.text.grid(row=0, column=0, columnspan=5)
        parent.bind("<Key>", self.keyPress)
 
        self.numDict = {}
        self.numCol = 0
        self.numRow = 1
        self.numList = ["Exit", "AC", "⌫", "+",
                        "7", "8", "9", "-",
                        "4", "5", "6", "×",
                        "1", "2", "3", "÷",
                        "0", ".", "=",]
        self.colDict = [4, 8, 12]
        for number in self.numList: #loop for buttons creations
            action = lambda x = number: self.textUpdate(x)  #sets action to update text
            if number == "0":
                self.numDict[number] = (Button(parent, text=number, command=action, width=25)).grid(row=self.numRow, column=self.numCol, pady=5, padx=5, columnspan=2)                         
                self.numCol += 1
            else:
                self.numDict[number] = (Button(parent, text=number, command=action)).grid(row=self.numRow, column=self.numCol, pady=5, padx=5)                         
            self.numCol +=1
            if self.numCol in self.colDict:
                self.numRow += 1    #rows and columns for button layout
                self.numCol = 0
                
        
class Logic(Calculator):    #class logic with calculator in it

    """
    >>> defines module for updating text that includes buttons AC, Exit, =, C
    """
       
    def textUpdate(self, number):
        if number == "AC":
            self.clearNumber()
        elif number == "Exit":
            self.exitCalc()
        elif number == "⌫":
            self.cancelNumber()
        elif number == "=":
            try: 
                self.equationList=text.get()    #gets text from entry widget
                self.equationList = self.equationList.replace("×"," * ").replace("÷"," / ").replace("+", " + ").replace("-", " - ")
                self.equationList = str(''.join(self.equationList))
                self.equationAns = eval(' '.join(str(int(x)) if x.isdigit() else x for x in self.equationList.split())) #removes leading zeroes
                self.text.delete(0, END)
                self.text.insert(0, equationAns)
            except Exception:   #except for all errors
                self.text.delete(0, END)
                self.error() 
        else:
            self.text.insert((len(self.numList)*100), number)


    """
    >>> key binding all keys
    """
        
    def keyPress(self, event):
        self.possibleKeys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                        'Return', 'plus', 'minus', 'slash', 'asterisk',
                        'period', 'BackSpace']
        if event.keysym in self.possibleKeys:
            self.textUpdate(event.keysym.replace('Return', '=').replace('plus', '+').replace('minus', '-')
                                   .replace('slash', '/').replace('asterisk', '*').replace('period', '.')
                                   .replace('BackSpace', '⌫'))


    """
    >>> defines cancel number to remove one number from calculation
    """

    def cancelNumber(self):
        self.equationList=self.text.get()
        self.equationList2=list(self.equationList)[:-1]
        self.equationList3=''.join(self.equationList2)
        self.text.delete(0, END)
        self.text.insert(0, self.equationList3)

    """
    >>> defines clearing all the numbers in the entry widget
    """

    def clearNumber(self):
        self.text.delete(0, END)

    """
    >>> defines an error message that pops up when an error occurs
    """

    def error(self):
        tkinter.messagebox.showerror("Error", "Error")

    """
    >>> defines closes window
    """
        
    def exitCalc(self):
        parent.destroy()

"""
>>> runs the GUI
"""

if __name__ == "__main__":
    root = Tk()
    test = Logic(root)
        
