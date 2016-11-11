#Into to programing
#Author: Daniel Gisolfi
#Date: 11/4/16
#TextGame.py
#Version 0.7




#Game Locations 
allLoc = ["labentrance","servicedesk", "powercenter", "sideentrance""Storage room", "computerlab", "datacenter","testingroom"] 
visited = [True,False,False,False,False,False,False, False]
locDetails = [
#Lab Entrance
("You come to the entrance where a large metal door used to stand protecting the lab and the nerds inside from the"
+" wilderness. There is now just a large opening leading into the dark lab. Head inside to further explore the lab"),
#servicedesk
("Entering the lab there is a service desk waiting dead ahead dimly lit only by the flickering CRT monitors left"
+" behind. there seems to be nothing here but unless computers from the 90s and lots of crumpled papers."),
#powercenter
("Huge generators fill the room, they are all shutdown as the main power switch is turned off,"
+" the backup battery seems to be charged and is the only source of power for the lab currently"),
#Storage room
("Behind the door to the storage room lies shelves upon shelves of prtotypes of jetpacks, flying cars and hoverboards"),
#Computerlab
("In the computer lab there is little walking space as the room was stuffed to the max with as many cubicles that"
+" would fit. There is a lone ceiling fan missing half its blades with plenty of trashed computers, paper and floppy"
+" disks scattered across the room."),
#datacenter
("Large mainframes hold mass amounts of data collected by the lab while it was operational,"
+" including all reports of experiments and tests"),
#Testing Room
("In this room lies the finished technologies of the lab that were left, you see dozons of itmes that untill now only"
+" seemed science fiction, including a small mech suit which you can use to get back to civilization.")]

#Game Matrix

gameMatrix =[[1,-1,-1,3],
[4,0,5,2],
[-1,3,1,-1],
[2,-1,0,-1],
[-1,1,6,-1],
[6,-1,-1,1],
[7,5,-1,4],
[-1,6,-1,-1]]


#item list

itemList = ["nothing","nothing","map","fashlight","nothing","nothing","keycard","nothing"]

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
def playercustom():
    global playername
    playername = input("Enter the name of your player: ")


def titleScreen():
    title = "The Abandoned Lab:"
    print(title)


def gameintro(): 
    global currLoc, score, moveCount
    backstory = playername + (", you are lost in the woods and searching for any relief from civilization"
                        +" you come across what used to be a scientific laboratory researching new technologies"
                        +" in the side of a mountain. The lab appears abandoned but could hold the key to surviving" 
                        +" nature…New technology!!! Explore inside to find some. \n")
    currLoc = 0
    score = int(0)
    moveCount = int(0)
    print()
    print(backstory)
    print()
    print("You are at the",allLoc[currLoc])
    print(locDetails[currLoc])
    print()


def move(dest):
    global currLoc, score, moveCount
    currLoc = dest
    if visited[dest] == False:
        score += 5
        moveCount += 1
        visited[dest] = True
    #if moveCount >= 15:
    updateGame()

def getDestination(startloc,direct):
    dest = gameMatrix[currLoc][direct]
    print(dest)
    if dest == nowhere:
            print("you cannot go " + direct + " from " + locationNames[startloc] + ".")
            dest = startloc
            return dest
    move(dest)

def take():
    global inventory
    inventory = []
    inventory.append.itemList[currLoc]
    itemList[currLoc] = "nothing"


def examine():
    if currLoc == itemList[currLoc]: #checks if the current location matches any locations in the items list
        return True
        print("There is a", itemList[currLoc], "in the area" )#reveal
    else:
        return False
        print("there is no item in this area")#let the player know there is not a item in this area


def updateGame():
    print()
    print("You are at the",allLoc[currLoc])
    print("score = ",score)
    print()
    print('you have' + +"moves left")
    print(locDetails[currLoc])
    print()
    
    
def userinput():
    while True:
        cmd = input("Which direction would you like to go?: \n")
        cmd = cmd.lower()
        destError = "You cannot go that way"

        if cmd == "north":
            direct = 0
        elif cmd == "south":
            direct = 0
        elif cmd == "east":
            direct = 0
        elif cmd == "west":
            direct = 0 
        getDestination(currLoc,direct)
        elif cmd == "examine":
            examine()
        elif cmd == "take":
            take()
        elif cmd == "help":
            cmdList = ["North", "South", "East", "West", "Help", "Quit", "Map", "Points"]
            print(cmdList)
        
        elif cmd == "quit":
            break
        
        elif cmd == "points":
            print(score) 

        elif cmd == "map":
            print('''Map
                                Testing Room(7)
                                    |
                                    |
            Storage Room(4)-----Datacenter(6)
                     |              |
                     |              |
                     |              |
Powercenter(2)-----Servicedesk(1)---Computer lab(5)
  |                  |   
  |                  |
  |                  |
Side Entrance(3)---Lab Entrance(0)

''')             
#End Game
def ending():
    conclusion = "Congratulations " + playername + ", you found the Testing room and technology inside, to help you get home safe"
    copyright = "Copyright (c) 2016 Daniel Gisolfi, Daniel.Gisolfi1@marist.edu"
    print() 
    print(conclusion)
    print() 
    print(copyright)






def main():
    playercustom()
    titleScreen()
    gameintro()
    userinput()

main()








paths = [matrix]

