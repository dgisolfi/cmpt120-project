#Into to programing
#Author: Daniel Gisolfi
#Date: 11/21/16
#TextGame.py
#Version 0.9


class Player:
    
    maxItems = 5

    def __init__(self,name):
        self.name = name    #atrributes of player
        self.location = 0
        self.score = 0
        self.inventory = []
        self.moveCount = 0

    def take(self, item):
        inventory.append(itemList[currLoc])
        print("you now have a", itemList[currLoc])
        itemList[currLoc] = "nothing"

        if len(self.inventory) < Player.maxItems:
            self.inventory.append(item)
            return True
        else:
            return False

    def drop(self, item):
        pass

    def Examine(self, item):
        if itemList[currLoc] != "nothing": #checks if the current location matches any locations in the items list
            print("There is a", itemList[currLoc], "in the area" )#reveal
        else:
            print("there is no item in this area")#let the player know there is not a item in this area




class Locale:

    def __init__(self, name, descrip, visited, items):
        self.name = name    #attributes of locations
        self.descrip = descrip
        self.visited = visited
        self.items = []

locations = [
    Locale("Lab Entrance","You come to the entrance where a large metal door used to stand protecting the "
         +"lab and the nerds inside from the wilderness. There is now just a large opening leading into the dark lab. "
         +"Head inside to further explore the lab",True,""),
    
    Locale("Service Desk","Entering the lab there is a service desk waiting dead ahead dimly lit only by the "
         +"flickering CRT monitors left behind. there seems to be nothing here but unless computers from the 90s and lots "
         +"of crumpled papers.",False,"Keycard"),
    
    Locale("Powercenter","Huge generators fill the room, they are all shutdown as the main power switch is turned off, "
         +" the backup battery seems to be charged and is the only source of power for the lab currently",False,"Flashlight"),
    
    Locale("Side Entrance","off to the side of the Main entrance lies a hidden door that appers to also lead to the lab",False, ""),
    
    Locale("Storage Room","Behind the door to the storage room lies shelves upon shelves of prtotypes of jetpacks, "
         +"flying cars and hoverboards",False, "Map"),

    Locale("Computer Lab","In the computer lab there is little walking space as the room was stuffed to the max with as many cubicles that"
        +" would fit. There is a lone ceiling fan missing half its blades with plenty of trashed computers, paper and floppy"
        +" disks scattered across the room.",False, ""),

    Locale("Datacenter","Large mainframes hold mass amounts of data collected by the lab while it was operational,"
        +" including all reports of experiments and tests",False, ""),

    Locale("Testing Room","In this room lies the finished technologies of the lab that were left, you see dozons of itmes that untill now only"
        +" seemed science fiction, including a small mech suit which you can use to get back to civilization.",False, "Power shoes"),

    Locale("Network Room","A small compact room filled with ethernet cables connected to various machines.",False, ""),

    Locale("Manufacturing Lab","An old manufacturing room where assembly lines are set up with products in various stages of completion",
        False, "Battery")
    ]






#Game Matrix

gameMatrix =[
[1,-1,-1,3],
[4,0,5,2],
[-1,3,1,-1],
[2,-1,0,-1],
[-1,1,6,-1],
[6,-1,-1,1],
[7,5,-1,4],
[-1,6,-1,-1],
[-1,2,4,-1],
[-1,4,7,-1]]


#item list

itemList = ["nothing","nothing","map","fashlight","nothing","nothing","keycard","nothing"]
inventory = []

#Direction list

directions = [0,1,2,3]#north,south,east,west

nowhere = -1 
labEntrance = 0
serviceDesk = 1
powerCenter = 2
sideEntrance = 3
storageRoom = 4 
computerLab = 5
dataCenter = 6
testingRoom = 7
                    
#Start Game
def playerCustom():
    Player.name = input("Enter the name of your player: ")


def titleScreen():
    title = "The Abandoned Lab:"
    print(title)


def gameintro(): 
    global currLoc, score, moveCount
    backstory = Player.name + (", you are lost in the woods and searching for any relief from civilization"
                        +" you come across what used to be a scientific laboratory researching new technologies"
                        +" in the side of a mountain. The lab appears abandoned but could hold the key to surviving" 
                        +" nature…New technology!!! Explore inside to find some. \n")
    currLoc = 0
    score = int(0)
    moveCount = int(14)
    print()
    print(backstory)
    print()
    #print("You are at the",allLoc[currLoc])
    #print(locDetails[currLoc])
    print()


def move(dest):
    global currLoc, score, moveCount
    currLoc = dest
    if visited[dest] == False:
        score += 5
        moveCount += 1
        visited[dest] = True
    if moveCount >= 15:
        ending()
    if currLoc == 7:
        ending()
    updateGame()

def getDestination(startloc,direct):
    dest = gameMatrix[currLoc][direct]
    print(dest)
    if dest == nowhere:
            print("you cannot go",cmd,"from",allLoc[startloc],".")
            dest = startloc
            return dest
    move(dest)
    

def examine():
    pass


def updateGame():
    print()
    print("You are at the",allLoc[currLoc])
    print("score = ",score)
    print()
    print('you have', 15- moveCount, "moves left")
    #print(locDetails[currLoc])
    print()
    
    
def  loop():
    while True:
        global cmd
        cmd = input("what would you like to do?: \n")
        cmd = cmd.lower()

        if cmd == "north" or "n":
            direct = 0
        elif cmd == "south" or "s":
            direct = 1
        elif cmd == "east" or "e":
            direct = 2
        elif cmd == "west" or "w":
            direct = 3  

        elif cmd == "examine" or "x":
            examine()
            continue

        elif cmd == "take" or "t":
            take()
            continue
        elif cmd == "help" or "h":
            cmdList = ["North", "South", "East", "West", "Help", "Quit", "Map", "Points"]
            print(cmdList)
            continue
        
        elif cmd == "quit" or "q":
            break
        
        elif cmd == "points" or "p":
            print(score)
            continue 

        elif cmd == "map" or "m":
            if "map" in self.inventory:
                print('''Map


            Manufacturing Lab(9) Testing Room(7)
                     |              |
                     |              |
Network Room(8)--Storage Room(4)--Datacenter(6)
      |              |              |
      |              |              |
      |              |              |
Powercenter(2)-----Servicedesk(1)---Computer lab(5)
      |              |   
      |              |
      |              |
Side Entrance(3)---Lab Entrance(0)

''')
            else:
                print("you have not found the map yet")
            continue

        else:
            print("that is not a valid command")
            continue
        
        getDestination(currLoc,direct)







#End Game
def ending():
    if moveCount == 15:
        print("you ran out of moves")
        print()
        print("Game Over")
        print()
    elif currLoc == 7:
        conclusion = "Congratulations " + playername + ", you found the Testing room and technology inside, to help you get home safe"
        print(conclusion)
        print() 
    copyright = "Copyright (c) 2016 Daniel Gisolfi, Daniel.Gisolfi1@marist.edu"
    print(copyright)

def main():
    playerCustom()
    titleScreen()
    gameintro()
    loop()
main()


