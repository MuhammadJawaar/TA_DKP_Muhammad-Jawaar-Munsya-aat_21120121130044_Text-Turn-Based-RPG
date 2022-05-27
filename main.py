# Import the required library
from tkinter import *
from tkinter import ttk
import tkinter as tk
from gamedata import game


class main:
    def __init__(self):
        self.inputnama = None
        
    def main(self):
        self.inputnama = tk.Tk()
        self.inputnama.geometry('300x200')
        ttk.Label(self.inputnama, text="Your Name").pack()
        text=Text(self.inputnama, width=40, height=1)
        text.insert(END, "")
        text.pack()
        B=ttk.Button(self.inputnama, text="Submit" ,command=lambda:self.retrieve_input(text)).pack()
        self.inputnama.mainloop()
    
    def retrieve_input(self,input1):
        input = input1.get("1.0",'end-1c')
        self.masukgame(input)

    def masukgame(self,name):
        temp = Tk()
        temp.withdraw()
        program = game(name)
        self.inputnama.destroy()
        temp.destroy()
        program.window.mainloop()      

          
xyz = main()
xyz.main()