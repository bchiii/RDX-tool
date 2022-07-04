import os
from os import system, remove
from tkinter import *
from tkinter import messagebox
from time import sleep

pre_installation_ver_root = Tk()
pre_installation_ver_root.iconbitmap("logo\\logo.ico")
pre_installation_ver_root.withdraw()

pre_installation_ver = messagebox.askyesno(title="RDX tool", message="the setup installation will add new libraries and modules to your system .                                                                                do you wish to proceed the installation .")
if pre_installation_ver == 0:
    pre_installation_ver_root.destroy();exit()

elif pre_installation_ver== 1:
        pre_installation_ver_root.destroy()
        system("clear")
        system("bash setup\\setup.sh")



