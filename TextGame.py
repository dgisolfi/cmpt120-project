#Into to programing
#Author: Daniel Gisolfi
#Date: 9/22/16
#TextGame.py
#Version 0.3

def game():
    
    
    #Game Locations 
    allLoc = ["labentrance","servicedesk", "powercenter","Storage room", "computerlab", "datacenter","Testing Room"] 
    visited = [False,False,False,False,False,False,False]
    llocDetails = [
        #Lab Entrance
        "You come to the entrance where a large metal door used to stand protecting the lab and the nerds inside from the"
        +" wilderness. There is now just a large opening leading into the dark lab. Head inside to further explore the lab"
        #servicedesk
        " Entering the lab there is a service desk waiting dead ahead dimly lit only by the flickering CRT monitors left"
        +" behind. there seems to be nothing here but unless computers from the 90s and lots of crumpled papers."
        #powercenter
        "Huge generators fill the room, they are all shutdown as the main power switch is turned off,"
        +" the backup battery seems to be charged and is the only source of power for the lab currently"
        #Storage room
        "Behind the door to the storage room lies shelves upon shelves of prtotypes of jetpacks, flying cars and hoverboards"
        #Computerlab
        "In the computer lab there is little walking space as the room was stuffed to the max with as many cubicles that"
        +" would fit. There is a lone ceiling fan missing half its blades with plenty of trashed computers, paper and floppy"
        +" disks scattered across the room."
        #datacenter
        "Large mainframes hold mass amounts of data collected by the lab while it was operational,"
        +" including all reports of experiments and tests"
        #Testing Room
        "In this room lies the finished technologies of the lab that where left, you see dozons of itmes that untill now only"
        +" seemed science fiction, including a small mech suit which you can use to get back to civilization."]
        
    #Start Game
    def playercustom():
        global playername
        playername = input("Enter the name of your player: ")
    playercustom()
    
    def titleScreen():
        title = "The Abandoned Lab:"
        print(title)
    titleScreen()
    
    def gameintro(): 
        global currLoc, score
        backstory = playername + (", you are lost in the woods and searching for any relief from civilization"
                            +" you come across what used to be a scientific laboratory researching new technologies"
                            +" in the side of a mountain. The lab appears abandoned but could hold the key to surviving" 
                            +" nature…New technology!!! Explore inside to find some. \n")
        currLoc = 0
        score = int(0)
        
        print()
        print(backstory)
        print()
        print(allLoc[currLoc])
        print(locDetails[currLoc])
    gameintro()

    def move(dest):
        global currLoc, score
        currLoc = dest
        if visited[dest] == False:
            score += 5
            visited[dest] = True
        updateGame()

    def updateGame():
        print()
        print("you are at the",allLoc[currLoc])
        print("score = ",score)
        
    def userinput():
        while True:
            cmd = input("Which direction would you like to go?: \n")
            cmd = cmd.lower()
            destError = "You cannot go that way"

            

            if cmd == "north":
                if currLoc == 0:
                    move(1)
                elif currLoc == 1:
                     move(3)
                elif currLoc == 4:
                     move(5)
                elif currLoc == 5:
                     ending()
                else:
                    print(destError)

            elif cmd == "south":
                if currLoc == 1:
                    move(0)
                elif currLoc == 3:
                    move(1)
                elif currLoc == 5:
                    move(4)
                elif currLoc == 6:
                    move(5)
                else:
                    print(destError)

            elif cmd == "east":
                if currLoc == 1:
                    move(4)
                elif currLoc == 2:
                    move(1)
                else:
                    print(destError)

            elif cmd == "west":
                if currLoc == 4:
                    move(1)
                elif currLoc == 1:
                    move(2) 
                else:
                    print(destError)

            elif cmd == "help":
                cmdList = ["North", "South", "East", "West", "Help", "Quit", "Map", "Points"]
                print(cmdList)
            
            elif cmd == "quit":
                break
            
            elif cmd == "points":
                print(score) 

            elif cmd == "map":
                print()             
#End Game
    def ending():
        conclusion = "Congratulations " + playername + ", you found the Testing room and technology inside, to help you get home safe"
        copyright = "Copyright (c) 2016 Daniel Gisolfi, Daniel.Gisolfi1@marist.edu"
        print() 
        print(conclusion)
        print() 
        print(copyright)
    userinput()
game()
