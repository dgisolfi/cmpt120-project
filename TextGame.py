#Into to programing
#Author: Daniel Gisolfi
#Date: 11/21/16
#TextGame.py
#Version 0.9


class Player
    
    maxItems = 5
    #constructor
    def __init__(self,name):
        self.name = name    #atrributes of player
        self.location = 0
        self.score = 0
        self.inventory = []
        self.moveCount = 0

    #method - an operation we an preform on a player
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

class Locale

    def __init__(self)
        self.locations = []
        self.






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
[-1,4,7 ,-1]]


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
    moveCount = int(14)
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
    


def updateGame():
    print()
    print("You are at the",allLoc[currLoc])
    print("score = ",score)
    print()
    print('you have', 15- moveCount, "moves left")
    print(locDetails[currLoc])
    print()
    
    
def  loop():
    while True:
        global cmd
        cmd = input("what would you like to do?: \n")
        cmd = cmd.lower()

        if cmd == "north":
            direct = 0
        elif cmd == "south":
            direct = 1
        elif cmd == "east":
            direct = 2
        elif cmd == "west":
            direct = 3  

        elif cmd == "examine":
            examine()
            continue

        elif cmd == "take":
            take()
            continue
        elif cmd == "help":
            cmdList = ["North", "South", "East", "West", "Help", "Quit", "Map", "Points"]
            print(cmdList)
            continue
        
        elif cmd == "quit":
            break
        
        elif cmd == "points":
            print(score)
            continue 

        elif cmd == "map":
            if "map" in inventory:
                print('''Map


            Manufacuring Lab(8) Testing Room(7)
                     |              |
                     |              |
Network Room--Storage Room(4)-----Datacenter(6)
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
    playercustom()
    titleScreen()
    gameintro()
    userinput()
main()


