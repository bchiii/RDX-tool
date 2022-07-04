import os
from os import system, remove
from tkinter import *
from tkinter import messagebox
from time import sleep

installation_done_root = Tk()
installation_done_root.iconbitmap("logo\\logo.ico")
installation_done_root.withdraw()
installation_done = messagebox.askokcancel("RDX tool", "installation finished.")

if installation_done == 1:
    installation_done_root.destroy()
    system("clear")
    system("bash run.sh")
else: 
    installation_done_root.destroy()
    system("clear")
    system("bash run.py")
                
    
