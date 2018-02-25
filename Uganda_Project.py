# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 17:40:07 2018

@author: Beth
"""


from tkinter import *
import datetime

# Medication
tk = Tk ()
f1 = Frame(tk, bg='blue')
f1.grid (sticky = "nsew")
Grid.columnconfigure (tk, 0, weight = 1)
Grid.rowconfigure (tk, 0, weight = 1)
tk.title("Uganda Project")


def medication():
    """This will run the Medication Reminder Program"""
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

    def save ():
        with open ("Log - %s.txt" % str (datetime.datetime.now ()).replace (":", "."), "w") as f: f.write ("\n".join (T.get (0, END)))
    
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
            save ()
            e.pack_forget ()

        elif answer2=="1":
            T.insert (END, "Support:")
            T.insert (END, "    Take it as your earliest convience.")
            T.insert (END, "    Do Not Take two doses at once!")
            root.bind ("<Return>", lambda event: root.destroy ())
            send.config (text = "OK", command = root.destroy)
            save ()
            e.pack_forget ()

        elif answer2=="2":
            T.insert (END, "Support:")
            T.insert (END, "    Please contact your doctor or")
            T.insert (END, "    pharmacy for refills.\n")
            root.bind ("<Return>", lambda event: root.destroy ())
            send.config (text = "OK", command = root.destroy)
            save ()
            e.pack_forget ()

        elif answer2=="3":
            T.insert (END, "Support:")
            T.insert (END, "    Please contact your doctor about")
            T.insert (END, "    changing your medications or")
            T.insert (END, "    dealing with your symptoms.")
            root.bind ("<Return>", lambda event: root.destroy ())
            send.config (text = "OK", command = root.destroy)
            save ()
            e.pack_forget ()

        else:
            T.insert (END, "Support:")
            T.insert (END, "    I did not understand your response.")

        return answer2

        root.mainloop()
    return medication

button1 = Button(f1, text="Medication", command=medication)
button1.grid(row = 1, column = 1, columnspan = 2)

# Appoinment

def appointment():
    """This will run the Appointment Reminder Program"""
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
    T.insert (END, "    Remember your appointment is on")
    T.insert (END, "    6/5/18 at 10:30am at location A.")
    T.insert (END, "    1= Confirm appointment")
    T.insert (END, "    2= Reschedule")

    #Make an entry box to answer the question in
    e = Entry(f, fg='black', bg='lightgray')
    e.focus_force ()
    e.grid (row = 1, column = 0, sticky = "ew")

    def save ():
        with open ("Log - %s.txt" % str (datetime.datetime.now ()).replace (":", "."), "w") as f: f.write ("\n".join (T.get (0, END)))

    def answer1():
        """ What to do with the answer in the entry box"""
        answer1 = e.get()
        T.insert (END, "Patient: " + answer1)
        e.delete (0, END)
        if answer1=="1":       
            T.insert (END, "Support:")
            T.insert (END, "    Thank you. See you then.")
            send.config (text = "OK", command = root.destroy)
            root.bind ("<Return>", lambda event: root.destroy ())
            save ()
            e.pack_forget ()

        elif answer1=="2":
            T.insert (END, "Support:")
            T.insert (END, "    The Nurse will contact you to reschedule.")
            root.bind ("<Return>", lambda event: root.destroy ())
            send.config (text = "OK", command = root.destroy)
            save ()
            e.pack_forget ()

        else:
            T.insert (END, "Support:")
            T.insert (END, "    I did not understand your response.")

        return answer1

    #Make a Send button to send the answer from the entry box to the definition of answer1 
    send = Button(f, text="Send", command=answer1)
    send.grid(row = 1, column = 1, columnspan = 2)

    root.mainloop()
    return appointment

button2 = Button(f1, text="Appointment", command=appointment)
button2.grid(row = 2, column = 1, columnspan = 2)

# Prescription
def prescription():
    """This will run the Prescription is Ready for Pick-Up Remider Program"""
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

    def save ():
        with open ("Log - %s.txt" % str (datetime.datetime.now ()).replace (":", "."), "w") as f: f.write ("\n".join (T.get (0, END)))

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
            save ()
            e.pack_forget ()
            
        elif answer1=="2":
           T.insert (END, "Support:")
           T.insert (END, "    Sorry for the error.")
           root.bind ("<Return>", lambda event: root.destroy ())
           send.config (text = "OK", command = root.destroy)
           save ()
           e.pack_forget ()

        else:
            T.insert (END, "Support:")
            T.insert (END, "    I did not understand your response.")

        return answer1

    #Make a Send button to send the answer from the entry box to the definition of answer1 
    send = Button(f, text="Send", command=answer1)
    send.grid(row = 1, column = 1, columnspan = 2)

    root.mainloop()

    return prescription
    
button3 = Button(f1, text="Prescription", command=prescription)
button3.grid(row = 3, column = 1, columnspan = 2)

# Side Effects
def side_effects():
    """This will run the Side Effects Program"""
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
    T.insert (END, "    Are you having bad side effects from your medicine?")
    T.insert (END, "    1= Yes")
    T.insert (END, "    2= No")

    #Make an entry box to answer the question in
    e = Entry(f, fg='black', bg='lightgray')
    e.focus_force ()
    e.grid (row = 1, column = 0, sticky = "ew")

    def save ():
        with open ("Log - %s.txt" % str (datetime.datetime.now ()).replace (":", "."), "w") as f: f.write ("\n".join (T.get (0, END)))

    def answer1():
        """ What to do with the answer in the entry box"""
        answer1 = e.get()
        T.insert (END, "Patient: " + answer1)
        e.delete (0, END)
        if answer1=="1":       
            T.insert (END, "Support:")
            T.insert (END, "    The Nurse will contact you.")
            send.config (text = "OK", command = root.destroy)
            root.bind ("<Return>", lambda event: root.destroy ())
            save ()
            e.pack_forget ()
            
        elif answer1=="2":
            T.insert (END, "Support:")
            T.insert (END, "    I'm glad to hear you aren't having bad side effects.")
            root.bind ("<Return>", lambda event: root.destroy ())
            send.config (text = "OK", command = root.destroy)
            save()
            e.pack_forget ()

        else:
            T.insert (END, "Support:")
            T.insert (END, "    I did not understand your response.")
        
        return answer1

    #Make a Send button to send the answer from the entry box to the definition of answer1 
    send = Button(f, text="Send", command=answer1)
    send.grid(row = 1, column = 1, columnspan = 2)

    root.mainloop()

    return side_effects

button4 = Button(f1, text="Side Effects", command=side_effects)
button4.grid(row = 4, column = 1, columnspan = 2)

# Patient Initiated
def patient_initiated():
    """This will run the Patient Initiated Conversation Program"""
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

    def save ():
        with open ("Log - %s.txt" % str (datetime.datetime.now ()).replace (":", "."), "w") as f: f.write ("\n".join (T.get (0, END)))
    
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
            save ()
            e.pack_forget ()

        elif answer2=="2":
            T.insert (END, "Support:")
            T.insert (END, "    The Nurse will contact you.")
            root.bind ("<Return>", lambda event: root.destroy ())
            send.config (text = "OK", command = root.destroy)
            save ()
            e.pack_forget ()

        elif answer2=="3":
            T.insert (END, "Support:")
            T.insert (END, "    The Nurse will contact you.")
            root.bind ("<Return>", lambda event: root.destroy ())
            send.config (text = "OK", command = root.destroy)
            save ()
            e.pack_forget ()

        else:
            T.insert (END, "Support:")
            T.insert (END, "    I did not understand your response.")

        return answer2

    root.mainloop()
    
    return patient_initiated

button5 = Button(f1, text="Patient Initiated", command=patient_initiated)
button5.grid(row = 5, column = 1, columnspan = 2)

tk.mainloop()
