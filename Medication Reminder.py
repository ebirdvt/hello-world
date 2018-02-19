# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 16:29:53 2018

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
T.insert (END, "    Did you take your medicine?")
T.insert (END, "    1= Yes")
T.insert (END, "    2= No")

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
        T.insert (END, "    Good Job! Text 0 to end conversation")
        send.config (command = answer2)
        root.bind ("<Return>", lambda event: answer2 ())

    elif answer1=="2":
        T.insert (END, "Support:")
        T.insert (END, "    1= Did you forget?")
        T.insert (END, "    2= Did you run out of medicine?")
        T.insert (END, "    3= Did it have bad side effects?")
        send.config (command = answer2)
        root.bind ("<Return>", lambda event: answer2 ())

    else:
        T.insert (END, "Support:")
        T.insert (END, "    I did not understand your response.")

    return answer1

#Make a Send button to send the answer from the entry box to the definition of answer1 
send = Button(f, text="Send", command=answer1)
send.grid(row = 1, column = 1, columnspan = 2)

#This is the second question

#Make an entry box to answer the question in

def answer2():
    """ What to do with the answer in the entry box"""
    answer2 = e.get()
    T.insert (END, "Patient: " + answer2)
    e.delete (0, END)
    #This is the response to the second entry box
    if answer2=="0":
        T.insert (END, "Support:")
        T.insert (END, "    Have a good day.")
        send.config (text = "OK", command = root.destroy)
        root.bind ("<Return>", lambda event: root.destroy ())
        e.pack_forget ()

    elif answer2=="1":
        T.insert (END, "Support:")
        T.insert (END, "    Take it as your earliest convience.")
        T.insert (END, "    Do Not Take two doses at once!")
        root.bind ("<Return>", lambda event: root.destroy ())
        send.config (text = "OK", command = root.destroy)
        e.pack_forget ()

    elif answer2=="2":
        T.insert (END, "Support:")
        T.insert (END, "    Please contact your doctor or")
        T.insert (END, "    pharmacy for refills.\n")
        root.bind ("<Return>", lambda event: root.destroy ())
        send.config (text = "OK", command = root.destroy)
        e.pack_forget ()

    elif answer2=="3":
        T.insert (END, "Support:")
        T.insert (END, "    Please contact your doctor about")
        T.insert (END, "    changing your medications or")
        T.insert (END, "    dealing with your symptoms.")
        root.bind ("<Return>", lambda event: root.destroy ())
        send.config (text = "OK", command = root.destroy)
        e.pack_forget ()

    else:
        T.insert (END, "Support:")
        T.insert (END, "    I did not understand your response.")

    return answer2

root.mainloop()
