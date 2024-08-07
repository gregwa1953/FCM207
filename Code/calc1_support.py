#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
# ======================================================
#     calc1_support.py
#  ------------------------------------------------------
# Created for Full Circle Magazine Issue #207
# Written by G.D. Walters
# Copyright © 2023, 2024 by G.D. Walters
# This source code is released under the MIT License
# ======================================================
# Support module generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#    Jul 07, 2024 04:39:31 AM CDT  platform: Linux

import sys

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter.font import Font
import calc1

_debug = False  # False to eliminate debug printing from callback functions.
divsym = "÷"

def main(*args):
    """Main entry point for the application."""
    global root
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = calc1.Toplevel1(_top1)
    startup()
    root.mainloop()

def startup():
    # Clear the display label widget
    _w1.Display.set("")
    global dbuf
    dbuf = ""
    set_button_fonts()
    _top1.title("Simple Calculator")

def set_button_fonts():
    """
    This function will set all TButtons in the project to a font size of bold 18 point.
    """
    sty = ttk.Style()
    # Create the font definition
    myFont = Font(family="DejaVu Sans", size=18, weight="bold", slant="roman")
    # Apply the new font to all the TButtons along with a different background colour
    sty.configure("TButton", font=myFont, background="cornsilk4")
    # Update the entire Toplevel (just in case)
    _top1.update()

def on_numKey(*args):
    """
    This is the callback function for all of the number keys.
    The value for that key is passed in as arg[0].
    number keys include {1,2,3,4,5,6,7,8,9,0,.}
    """
    if _debug:
        print("calc1_support.on_numKey")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()
    global dbuf
    dbuf = dbuf + str(args[0])
    _w1.Display.set(dbuf)

def on_funcKey(*args):
    """
    This is the callback function for all of the 'function' keys.
    The function 'name' for that key is passed in as arg[0].
    """
    if _debug:
        print("calc1_support.on_funcKey")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()
    global dbuf
    which = args[0]
    match which:
        case "Add":
            dbuf = f"{dbuf}+"
            _w1.Display.set(dbuf)
        case "Sub":
            dbuf = f"{dbuf}-"
            _w1.Display.set(dbuf)
        case "Mult":
            dbuf = f"{dbuf}*"
            _w1.Display.set(dbuf)
        case "Divide":
            dbuf = f"{dbuf}/"
            _w1.Display.set(dbuf)
        case "Clear":
            _w1.Display.set("")
            dbuf = ""
        case "Equal":
            result = str(eval(dbuf))
            _w1.Display.set(result)
            _top1.update()
            dbuf = ""

if __name__ == "__main__":
    calc1.start_up()




