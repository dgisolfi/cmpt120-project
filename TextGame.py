#Into to programing
#Author: Daniel Gisolfi
#Date: 11/21/16
#TextGame.py
#Version 1.0

from TextGameGui import *
from TextGameClass import *

#Start Game
def press():
    global cmd
    cmd = cmdInput.get()
    outputText.insert(END,cmd)
    cmd = cmd.lower()
    loop()
    outputText.insert(END,"")
    outputText.insert(END,"Enter a Command:")


def titleScreen():
    outputText.insert(END, "The Abandoned Lab:")
    outputText.insert(END, "Enter the name of your player and press enter: ")

def playerCustom():     
    player.name = cmdInput.get()
    cmdButton.config(command = press)
    gameintro()


def gameintro():
    global backstory
    backstory = player.name + (", you are lost in the woods and searching for any relief from civilization\n"
                            +" you come across what used to be a scientific laboratory researching new technologies\n"
                            +"in the side of a mountain. The lab appears abandoned but could hold the key to surviving\n"
                            +"Find all items to win")
    player.location = 0
    player.score = 0
    player.moveCount = 0
    player.inventory = ""
    outputText.insert(END,"")
    outputText.insert(END,backstory)
    outputText.insert(END,"")
    outputText.insert(END,("You are at the "+locations[player.location].name))
    outputText.insert(END,(locations[player.location].descrip))
    outputText.insert(END,"")
    outputText.insert(END,"Enter a Command:")
    


def move(dest):
    player.location = dest
    if locations[dest].visited == False:
        player.score += 5
        player.moveCount += 1
        locations[dest].visited = True
    if player.moveCount >= 15:
        ending()
    updateGame()

def getDestination(startloc,direct):
    dest = gameMatrix[player.location][direct]
    if dest == nowhere:
            outputText.insert(END,("you cannot go "+cmd+" from"+locations[player.location]+"."))
            dest = startloc
            return dest
    move(dest)


def updateGame():
    #outputText.insert(END,"")
    outputText.insert(END,("You are at the "+locations[player.location].name))
    outputText.insert(END,("score = ",str(player.score)))
    #outputText.insert(END,'you have', 15- player.moveCount, "moves left")
    if locations[player.location].visited != True:
        outputText.insert(END,(locations[player.location].descrip))
    
    
def  loop():
    global cmd
    
    if cmd == "north" or "n":
        direct = 0
    elif cmd == "south" or "s":
        direct = 1
    elif cmd == "east" or "e":
        direct = 2
    elif cmd == "west" or "w":
        direct = 3  

    elif cmd == "examine" or "x":
        [cmd,item] = examine(str,input("Enter the command and what item you would like to affect").split(" "))
        

    elif cmd == "take" or "t":
        [cmd,item] = take(str,input("Enter the command and what item you would like to affect").split(" "))
        

    elif cmd == "drop" or "d":
        [cmd,item] = drop(str,input("Enter the command and what item you would like to affect").split(" "))
        

    elif cmd == "help" or "h":
        cmdList = ["North", "South", "East", "West", "Help", "Quit", "Map", "Points"]
        outputText.insert(END,cmdList)
        
    
    elif cmd == "points" or "p":
        outputText.insert(END,player.score)

    elif cmd == "inventory" or "i":
        outputText.insert(END, player.inventory)
         

    elif cmd == "map" or "m":
        if "map" in player.inventory:
            outputText.insert(END,'''Map


        Manufacturing Lab(9) Testing Room(7)-------aiFacility(10)
                 |              |
                 |              |
Network Room(8)--Storage Room(4)--Datacenter(6)
  |              |              |
  |              |              |
  |              |              |
Powercenter(2)-----Servicedesk(1)---Computer lab(5)--breakRoom(11)
  |              |   
  |              |
  |              |
Side Entrance(3)---Lab Entrance(0)

''')
        else:
            outputText.insert(END,"you have not found the map yet")

    else:
        outputText.insert(END,"that is not a valid command")      
    
    getDestination(player.location,direct)

#End Game
def ending():
    if player.moveCount == 15:
        outputText.insert(END,"you ran out of moves")
        outputText.insert(END,"")
        outputText.insert(END,"Game Over")
        outputText.insert(END,"")
    elif player.inventory == 5:
        conclusion = "Congratulations " + player.name + ", you found the Testing room and technology inside, to help you get home safe"
        outputText.insert(END,conclusion)
        outputText.insert(END,"") 
    copyright = "Copyright (c) 2016 Daniel Gisolfi, Daniel.Gisolfi1@marist.edu"
    outputText.insert(END,copyright)
    while True:
        outputText.insert(END,"do you want to play again? Y or N")
        txt = cmdInput.get()
        outputText.insert(END,cmd)
        txt = txt.lower()
        if "Y" in txt:
            continue
        else:
            root.quit()

gameGui()


