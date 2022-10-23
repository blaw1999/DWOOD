#import cgitb cgitb.enable()
#attempt to embed into an html using cgit

import json

from tkinter import *

if __name__ == '__main__':
    window = Tk()
    window.title(" TestingApp ")

    s1 = StringVar(window);s2 = StringVar(window);s3 = StringVar(window)
    s4 = StringVar(window);s5 = StringVar(window);s6 = StringVar(window)
    s7 = StringVar(window);s8 = StringVar(window);s9 = StringVar(window)
    s10 =StringVar(window);s11 = StringVar(window);s12 = StringVar(window)

    L1 = Label(window, text="Event Date*").grid(column = 0, row = 0)
    E1 = Entry(window, textvariable = s1, bd =5).grid(column = 1, row = 0)

    L2 = Label(window, text="Start Time*").grid(column = 0, row = 1)
    E2 = Entry(window, textvariable = s2, bd =5).grid(column = 1, row = 1)

    L3 = Label(window, text="End Time*").grid(column = 0, row = 2)
    E3 = Entry(window, textvariable = s3, bd =5).grid(column = 1, row = 2)
    
    L4 = Label(window, text="Location of Event*").grid(column = 0, row = 3)
    E4 = Entry(window, textvariable = s4, bd =5).grid(column = 1, row = 3)

    L5 = Label(window, text="Event Title/Name*").grid(column = 0, row = 4)
    E5 = Entry(window, textvariable = s5, bd =5).grid(column = 1, row = 4)

    L6 = Label(window, text="Client Name*").grid(column = 0, row = 5)
    E6 = Entry(window, textvariable = s6, bd =5).grid(column = 1, row = 5)

    L7 = Label(window, text="Client Email*").grid(column = 0, row = 6)
    E7 = Entry(window, textvariable = s7, bd =5).grid(column = 1, row = 6)

    L8 = Label(window, text="Client Phone Number*").grid(column = 0, row = 7)
    E8 = Entry(window, textvariable = s8, bd =5).grid(column = 1, row = 7)

    L9 = Label(window, text="Company/Business Name (if applicable)").grid(column = 0, row = 8)
    E9 = Entry(window, textvariable = s9, bd =5).grid(column = 1, row = 8)

    L10 = Label(window, text="Day-of Point of Contact (Name, phone & email if not same as client above)").grid(column = 0, row = 9)
    E10 = Entry(window,textvariable = s10, bd =5).grid(column = 1, row = 9)

    L11 = Label(window, text="Nature of Appearance:").grid(column = 0, row = 10)

    var = IntVar()
    R1 = Radiobutton(window, text="Private/Corporate", variable=var, value=1,
                  command=SEL).grid(column = 1, row = 10)


    R2 = Radiobutton(window, text="Department/Office", variable=var, value=2,
                  command=SEL).grid(column = 1, row = 11)


    R3 = Radiobutton(window, text="Student Organization", variable=var, value=3,
                  command=SEL).grid(column = 1, row = 12)
    
    R4 = Radiobutton(window, text="Non-Profit", variable=var, value=4,
                  command=SEL).grid(column = 1, row = 13)
    R5 = Radiobutton(window, text="Other", variable=var, value=5,
                  command=SEL).grid(column = 1, row = 14)

    L12 = Label(window, text="Physical Billing Address").grid(column = 0, row = 15)
    E12 = Entry(window, textvariable = s11, bd =5).grid(column = 1, row = 15)

    L13 = Label(window, text="Mascot Preference (Note: If mascot requested is unavailable, you will be offered the other mascot before scheduling the event.").grid(column = 0, row = 16)

    var2 = IntVar()
    R6 = Radiobutton(window, text="Mascot 1", variable=var2, value=1,
                  command=SEL).grid(column = 1, row = 16)

    R7 = Radiobutton(window, text="Mascot 2", variable=var2, value=2,
                  command=SEL).grid(column = 1, row = 17)

    R8 = Radiobutton(window, text="First Availible", variable=var2, value=3,
                  command=SEL).grid(column = 1, row = 18)
    
    R9 = Radiobutton(window, text="Both (2x rate)", variable=var2, value=4,
                  command=SEL).grid(column = 1, row = 19)


    L14 = Label(window, text="What Do You Request of the Mascot(s) (ie. special instructions").grid(column = 0, row = 20)
    E14 = Entry(window, textvariable = s12, bd =5).grid(column = 1, row = 20)

    var3 = IntVar()
    L15 = Label(window, text="Have you read our appearance terms and conditions listed above on this page?").grid(column = 0, row = 21)
    R10 = Radiobutton(window, text="No", variable=var3, value=1,
                  command=SEL).grid(column = 1, row = 21)
    
    R11 = Radiobutton(window, text="Yes", variable=var3, value=2,
                  command=SEL).grid(column = 2, row = 21)

    def createJSON(a,b,c,d,e,f,g,h,i,j,k,l,m,o,p):
        x = {
            "date" : a.get(),
            "start" : b.get(),
            "end" : c.get(),
            "location" : d.get(),
            "Title" : e.get(),
            "Client" : f.get(),
            "Email" : g.get(),
            "Number" : h.get(),
            "Business" : i.get(),
            "DOPOC" : j.get(),
            "Nature" : k.get(),
            "BillingAdd" : l.get(),
            "Mascot" : m.get(),
            "Special" : o.get(),
            "TOC" : p.get()
            }
        y = json.dumps(x)
        print(y)
    
    enterbutton = Button(window, text = "Submit", command = lambda: createJSON(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10, var, s11, var2, s12, var3)).grid(row = 22, column = 2)
