'''
Created on April 14, 2016
@author: Anthony Frazier 
'''

import tkinter;

#Declaring tkinter object and String Variable constructor for tkinter object 
gui = tkinter.Tk();
gui.title("Calculator")
entry = ""
entry = tkinter.StringVar()

#Creating the tkinter frame with a grey background and packing it into the tkinter object panel 
topframe = tkinter.Frame(gui,  background = "Grey")
topframe.pack()

#Creating the calculator's textbox 
numberentry = tkinter.Entry(topframe, textvariable = entry, bd = 20)
numberentry.pack(side = "top")
numberentry.focus()

#The clear function clears the entry box of any existing string characters 
def clear():
    numberentry.delete(first = 0, last = "end");
    return

#Adds the corresponding string depending on the button pressed. Must be passed character to print. 
def addNumber(number):
    newentry = ""
    newentry = entry.get() + number
    entry.set(newentry)
    return

#Evaluates the given string in the entry box. Question: Does Java have an eval function? 
def equal():
    result = ""
    result = eval(entry.get())
    entry.set(result)
    return 


#Creates another frame, consisting of the 1, 2, 3, and + buttons. 
frame1 = tkinter.Frame(gui)
frame1.pack()
button1 = tkinter.Button(frame1, padx = 20, pady = 20, text = "1", fg ="Black", bg = "Grey", bd= 10, 
                         command = lambda : addNumber("1"))
button1.pack(side = "left")
button2 = tkinter.Button(frame1, text = "2", padx = 20, pady = 20,fg ="Black", bg = "Grey", bd= 10, 
                         command = lambda : addNumber("2"))
button2.pack(side = "left")
button3 = tkinter.Button(frame1, text = "3", padx = 20, pady = 20, fg ="Black", bg = "Grey", bd= 10, 
                        command = lambda : addNumber("3"))
button3.pack(side = "left")
buttonplus = tkinter.Button(frame1, text = "+", padx = 20, pady = 20, fg ="Black", bg = "Grey", bd= 10, command = lambda : addNumber("+"))
buttonplus.pack(side = "left")

#Creates another frame, consisting of the 4, 5, 6, and - buttons. 
frame2 = tkinter.Frame(gui)
frame2.pack()
button4 = tkinter.Button(frame2, text = "4", padx = 20, pady = 20, fg ="Black", bg = "Grey", bd= 10, 
                         command = lambda : addNumber("4"))
button4.pack(side = "left")
button5 = tkinter.Button(frame2, text = "5", padx = 20, pady = 20,  fg ="Black", bg = "Grey", bd= 10, 
                         command = lambda : addNumber("5"))
button5.pack(side = "left")
button6 = tkinter.Button(frame2, text = "6", padx = 20, pady = 20,  fg ="Black", bg = "Grey", bd= 10, 
                         command = lambda : addNumber("6"))
button6.pack(side = "left")
buttonminus = tkinter.Button(frame2, text = "-", padx = 20, pady = 20, fg ="Black", bg = "Grey", bd= 10, command = lambda : addNumber("-"))
buttonminus.pack(side = "left")


#Creates another frame, consisting of the 7, 8, 9, and * buttons. 
frame3 = tkinter.Frame(gui)
frame3.pack()
button7 = tkinter.Button(frame3, text = "7", padx = 20, pady = 20,  fg ="Black", bg = "Grey", bd= 10, 
                         command = lambda : addNumber("7"))
button7.pack(side = "left")
button8 = tkinter.Button(frame3, text = "8", padx = 20, pady = 20, fg ="Black", bg = "Grey", bd= 10, 
                         command = lambda : addNumber("8"))
button8.pack(side = "left")
button9 = tkinter.Button(frame3, text = "9", padx = 20, pady = 20,  fg ="Black", bg = "Grey", bd= 10, 
                         command = lambda : addNumber("9"))
button9.pack(side = "left")
buttonstar = tkinter.Button(frame3, text = "*", padx = 20, pady = 20, fg ="Black", bg = "Grey", bd= 10, command = lambda : addNumber("*"))
buttonstar.pack(side = "left")

#Creates another frame, consisting of the ., 0, C, and / buttons. 
frame4 = tkinter.Frame(gui, background = "Grey")
frame4.pack()
buttondot = tkinter.Button(frame4, text = ".", padx = 20, pady = 20,  fg ="Black", bg = "Grey", bd= 10, 
                         command = lambda : addNumber("."))
buttondot.pack(side = "left")
button0 = tkinter.Button(frame4, text = "0", padx = 20, pady = 20,  fg ="Black", bg = "Grey", bd= 10, 
                         command = lambda : addNumber("0"))
button0.pack(side = "left")
button0 = tkinter.Button(frame4, text = "C", padx = 20, pady = 20,  fg ="Black", bg = "Grey", bd= 10, 
                         command = clear)
button0.pack(side = "left")
buttondivide = tkinter.Button(frame4, text = "/", padx = 20, pady = 20, fg ="Black", bg = "Grey", bd= 10, command = lambda : addNumber("/"))
buttondivide.pack(side = "left")

#Creates another frame, consisting of the = button. 
frame5 = tkinter.Frame(gui, background = "Grey")
frame5.pack()
buttonequals = tkinter.Button(frame5, text = "=", padx = 80, pady = 20, fg ="Black", bg = "Grey", bd= 10, command = lambda : equal())
buttonequals.pack(side = "left")

#Command loops the panel and frames until the panel is closed. Cannot be used on Linux machines. 
gui.mainloop();
