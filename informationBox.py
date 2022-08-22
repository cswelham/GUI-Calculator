from tkinter import *
import tkinter.messagebox

"""
>>> defines information which is message box in taskbar
"""

def informationBox():
    x = tkinter.messagebox.showinfo("Information", "A calculator is a device that performs arithmetic operations on numbers."
                                    "The simplest calculators can do only addition, subtraction, multiplication, and division."
                                    "More sophisticated calculators can handle exponent ial operations, roots, logarithm s, trigonometric functions,"
                                    "and hyperbolic functions. Internally, some calculators actually perform all of these functions by repeated processes of addition.")
