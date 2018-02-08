# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 15:57:18 2018

@author: Beth
"""

import tkinter
from tkinter import *

def text_message(answer1, answer2):
    """This will hopefully show in text boxes text messages back and forth"""
    
    root = Tk()
    frame = Frame(root, bg='white')
    frame.pack(fill='both', expand='yes')
    root.title("Uganda Project")
    T = Text(frame, height=3, width=37)
    T.pack()
    T.insert(END, "Did you take your medicine today?\n 1= Yes\n 2= No\n")
    T.configure(fg='white', bg='blue')
    
    T2 = Text(frame, height=1, width=37)
    T2.pack()
    T2.insert(END, answer1)
    T2.configure(fg='black', bg='lightgray')
    
    if answer1==1:
        
        T3 = Text(frame, height=1, width=37)
        T3.pack()
        T3.insert(END, "Good Job! Text 0 to end conversation")
        T3.configure(fg='white', bg='blue')
        
    else:
        T3 = Text(frame, height=3, width=37)
        T3.pack()
        T3.insert(END, "1= Did you forget?\n2= Did you run out of medicine?\n3= Did it have bad side effects?\n")
        T3.configure(fg='white', bg='blue')

    T4 = Text(frame, height=1, width=37)
    T4.pack()
    T4.insert(END, answer2)
    T4.configure(fg='black', bg='lightgray')
    
    if answer2==0:
        T5 = Text(frame, height=1, width=37)
        T5.pack()
        T5.insert(END, "Have a good day.")
        T5.configure(fg='white', bg='blue')
        
    elif answer2==1:
        T5 = Text(frame, height=2, width=37)
        T5.pack()
        T5.insert(END, "Take it as your earliest convience.\nDo Not Take two doses at once!\n")
        T5.configure(fg='white', bg='blue')
    
    elif answer2==2:
        T5 = Text(frame, height=2, width=37)
        T5.pack()
        T5.insert(END, "Please contact your doctor or\npharmacy for refills.\n")
        T5.configure(fg='white', bg='blue')
        
    else:
        T5 = Text(frame, height=3, width=37)
        T5.pack()
        T5.insert(END, "Please contact your doctor about\nchanging your medications or\ndealing with your symptoms.\n")
        T5.configure(fg='white', bg='blue')
        root.mainloop()
        
text_message(1,0)
text_message(2,1)
text_message(2,2)
text_message(2,3)