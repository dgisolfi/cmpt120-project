#Into to programing
#Author: Daniel Gisolfi
#Date: 12/14/16
#TextGameGui.py
#Version 1.0
from tkinter import *
from sys import *
# GUI for game
def gameGui():
    global outText, outputText, Frame, cmdInput, cmdButton, root

    #Make a window, named "root"
    root = Tk()
    #root attributes
    #root.geometry("550x350+500+300")
    root.title("Text Game")
    #root.option_add("*background", "black")

    #Frame
    Frame = Frame(root)
    Frame.pack(side = TOP)
        #outputText = Label(bottomFrame, text = outText).pack()
    #Widgets for Frame
        #listbox
    scrollbar = Scrollbar(Frame)
    outputText = Listbox(Frame, yscrollcommand=scrollbar.set, width = 40)
    scrollbar.config(command=outputText.yview)
        #Other widgets
    instructLabel = Label(Frame, text = "Enter a Command:")
    cmdInput = Entry(Frame)
    cmdButton = Button(Frame, text = "Enter",fg = "blue", command = playerCustom)
    quitButton = Button(Frame, text = "Quit", command = ending)
    startButton = Button(Frame, text = "Start", command = titleScreen)
    
    #outputText = Label(bottomFrame, text = outText)
    

    #Pack widgets
    scrollbar.pack(side=LEFT, fill=Y)
    outputText.pack(side=LEFT, fill=BOTH)
    instructLabel.pack(side = TOP)
    cmdInput.pack(side = TOP)
    quitButton.pack(side = RIGHT)
    cmdButton.pack(side = LEFT)
    startButton.pack(side = LEFT)
    outputText.insert(END, "Press Start")
    #outputText.pack()
    root.mainloop()