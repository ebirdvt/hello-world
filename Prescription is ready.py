# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 07:36:26 2018

@author: Beth
"""

from tkinter import *


root = Tk ()
root.bind ("<Return>", lambda event: answer1 ())
f = Frame(root, bg='lightgray')
f.grid (sticky = "nsew")
Grid.columnconfigure (root, 0, weight = 1)
Grid.rowconfigure (root, 0, weight = 1)
root.title("Uganda Project")

#This is the first Question
Bar = Scrollbar (f)
T = Listbox (f, fg='white', bg='blue', yscrollcommand = Bar.set, width = 50, height = 20)
Bar.config (command = T.yview)
T.grid (row = 0, column = 0, columnspan = 2, sticky = "nsew")
Bar.grid (row = 0, column = 2, sticky = "ns")
Grid.columnconfigure (f, 0, weight = 1)
Grid.rowconfigure (f, 0, weight = 1)
T.insert (END, "Support:")
T.insert (END, "    Your prescription is ready for pick-up.")
T.insert (END, "    Please get it at your earliest convience.")
T.insert (END, "    1= Confirm read message.")
T.insert (END, "    2= Didn't need a refill.")

#Make an entry box to answer the question in
e = Entry(f, fg='black', bg='lightgray')
e.focus_force ()
e.grid (row = 1, column = 0, sticky = "ew")

def answer1():
    """ What to do with the answer in the entry box"""
    answer1 = e.get()
    T.insert (END, "Patient: " + answer1)
    e.delete (0, END)
    if answer1=="1":       
        T.insert (END, "Support:")
        T.insert (END, "    Thank you. Have a good day.")
        send.config (text = "OK", command = root.destroy)
        root.bind ("<Return>", lambda event: root.destroy ())
        e.pack_forget ()

    elif answer1=="2":
        T.insert (END, "Support:")
        T.insert (END, "    Sorry for the error.")
        root.bind ("<Return>", lambda event: root.destroy ())
        send.config (text = "OK", command = root.destroy)
        e.pack_forget ()

    else:
        T.insert (END, "Support:")
        T.insert (END, "    I did not understand your response.")

    return answer1

#Make a Send button to send the answer from the entry box to the definition of answer1 
send = Button(f, text="Send", command=answer1)
send.grid(row = 1, column = 1, columnspan = 2)

root.mainloop()
