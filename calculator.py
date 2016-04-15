# Calculator
Basic Python implementation of a calculator fit with GUI.


'''
Created on Apr 14, 2016
@author: MorsRegis
'''

import tkinter;

gui = tkinter.Tk();
gui.title("Calculator")
entry = ""
entry = tkinter.StringVar()

topframe = tkinter.Frame(gui,  background = "Grey")
topframe.pack()
numberentry = tkinter.Entry(topframe, textvariable = entry, bd = 20)
numberentry.pack(side = "top")
numberentry.focus()


def clear():
    numberentry.delete(first = 0, last = "end");
    return

#Work on this function
def addNumber(number):
    newentry = entry.get() + number
    entry.set(newentry)
    return

def equal():
    result = ""
    result = eval(entry.get())
    entry = entry.set(result)
    return 


    
frame1 = tkinter.Frame(gui)
frame1.pack()
button1 = tkinter.Button(frame1, padx = 20, pady = 20, text = "1", fg ="Black", bg = "Grey", bd= 10, 
                         command = addNumber("1"))
button1.pack(side = "left")
button2 = tkinter.Button(frame1, text = "2", padx = 20, pady = 20,fg ="Black", bg = "Grey", bd= 10, 
                         command = addNumber("2"))
button2.pack(side = "left")
button3 = tkinter.Button(frame1, text = "3", padx = 20, pady = 20, fg ="Black", bg = "Grey", bd= 10, 
                        command = addNumber("3"))
button3.pack(side = "left")
buttonplus = tkinter.Button(frame1, text = "+", padx = 20, pady = 20, fg ="Black", bg = "Grey", bd= 10)
buttonplus.pack(side = "left")

frame2 = tkinter.Frame(gui)
frame2.pack()
button4 = tkinter.Button(frame2, text = "4", padx = 20, pady = 20, fg ="Black", bg = "Grey", bd= 10, 
                         command = addNumber("4"))
button4.pack(side = "left")
button5 = tkinter.Button(frame2, text = "5", padx = 20, pady = 20,  fg ="Black", bg = "Grey", bd= 10, 
                         command = addNumber("5"))
button5.pack(side = "left")
button6 = tkinter.Button(frame2, text = "6", padx = 20, pady = 20,  fg ="Black", bg = "Grey", bd= 10, 
                         command = addNumber("6"))
button6.pack(side = "left")
buttonminus = tkinter.Button(frame2, text = "-", padx = 20, pady = 20, fg ="Black", bg = "Grey", bd= 10)
buttonminus.pack(side = "left")


frame3 = tkinter.Frame(gui)
frame3.pack()
button7 = tkinter.Button(frame3, text = "7", padx = 20, pady = 20,  fg ="Black", bg = "Grey", bd= 10, 
                         command = addNumber("7"))
button7.pack(side = "left")
button8 = tkinter.Button(frame3, text = "8", padx = 20, pady = 20, fg ="Black", bg = "Grey", bd= 10, 
                         command = addNumber("8"))
button8.pack(side = "left")
button9 = tkinter.Button(frame3, text = "9", padx = 20, pady = 20,  fg ="Black", bg = "Grey", bd= 10, 
                         command = addNumber("9"))
button9.pack(side = "left")
buttonstar = tkinter.Button(frame3, text = "*", padx = 20, pady = 20, fg ="Black", bg = "Grey", bd= 10)
buttonstar.pack(side = "left")

frame4 = tkinter.Frame(gui, background = "Grey")
frame4.pack()
buttondot = tkinter.Button(frame4, text = ".", padx = 20, pady = 20,  fg ="Black", bg = "Grey", bd= 10, 
                         command = addNumber("."))
buttondot.pack(side = "left")
button0 = tkinter.Button(frame4, text = "0", padx = 20, pady = 20,  fg ="Black", bg = "Grey", bd= 10, 
                         command = addNumber("0"))
button0.pack(side = "left")
button0 = tkinter.Button(frame4, text = "C", padx = 20, pady = 20,  fg ="Black", bg = "Grey", bd= 10, 
                         command = clear)
button0.pack(side = "left")
buttondivide = tkinter.Button(frame4, text = "/", padx = 20, pady = 20, fg ="Black", bg = "Grey", bd= 10)
buttondivide.pack(side = "left")

frame5 = tkinter.Frame(gui, background = "Grey")
frame5.pack()
buttonequals = tkinter.Button(frame5, text = "=", padx = 80, pady = 20, fg ="Black", bg = "Grey", bd= 10)
buttonequals.pack(side = "left")


gui.mainloop();
