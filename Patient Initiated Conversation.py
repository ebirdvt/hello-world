# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 13:43:16 2018

@author: Beth
"""

from tkinter import *

root = Tk ()
root.bind ("<Return>", lambda event: start_convo ())
f = Frame(root, bg='lightgray')
f.grid (sticky = "nsew")
Grid.columnconfigure (root, 0, weight = 1)
Grid.rowconfigure (root, 0, weight = 1)
root.title("Uganda Project")

#This is the beginning of the conversation
Bar = Scrollbar (f)
T = Listbox (f, fg='white', bg='blue', yscrollcommand = Bar.set, width = 50, height = 20)
Bar.config (command = T.yview)
T.grid (row = 0, column = 0, columnspan = 2, sticky = "nsew")
Bar.grid (row = 0, column = 2, sticky = "ns")
Grid.columnconfigure (f, 0, weight = 1)
Grid.rowconfigure (f, 0, weight = 1)

#Make an entry box to answer the question in
e = Entry(f, fg='black', bg='lightgray')
e.focus_force ()
e.grid (row = 1, column = 0, sticky = "ew")

def start_convo():
    """ What to do with the answer in the entry box"""
    start_convo = e.get()
    T.insert (END, "Patient: " + start_convo)
    e.delete (0, END)
    if start_convo=="77":       
        T.insert (END, "Support:")
        T.insert (END, "    1= Need to talk to the Nurse.")
        T.insert (END, "    2= Need to reschedule an appoinment.")
        T.insert (END, "    3= Need a medication refill.")
        send.config (command = answer2)
        root.bind ("<Return>", lambda event: answer2 ())

    else:
        T.insert (END, "Support:")
        T.insert (END, "    I did not understand your response.")

    return start_convo

#Make a Send button to send the answer from the entry box to the definition of answer1 
send = Button(f, text="Send", command=start_convo)
send.grid(row = 1, column = 1, columnspan = 2)

#This is the second question

#Make an entry box to answer the question in

def answer2():
    """ What to do with the answer in the entry box"""
    answer2 = e.get()
    T.insert (END, "Patient: " + answer2)
    e.delete (0, END)
    #This is the response to the second entry box
    if answer2=="1":
        T.insert (END, "Support:")
        T.insert (END, "    The Nurse will contact you.")
        send.config (text = "OK", command = root.destroy)
        root.bind ("<Return>", lambda event: root.destroy ())
        e.pack_forget ()

    elif answer2=="2":
        T.insert (END, "Support:")
        T.insert (END, "    The Nurse will contact you.")
        root.bind ("<Return>", lambda event: root.destroy ())
        send.config (text = "OK", command = root.destroy)
        e.pack_forget ()

    elif answer2=="3":
        T.insert (END, "Support:")
        T.insert (END, "    The Nurse will contact you.")
        root.bind ("<Return>", lambda event: root.destroy ())
        send.config (text = "OK", command = root.destroy)
        e.pack_forget ()

    else:
        T.insert (END, "Support:")
        T.insert (END, "    I did not understand your response.")

    return answer2

root.mainloop()

