#Into to programing
#Author: Daniel Gisolfi
#Date: 9/22/16
#TextGame.py
#Version 0.3

def game():
    
    
    #Game Locations 
    allLoc = ["labentrance","servicedesk", "powercenter","Storage room", "computerlab", "datacenter","Testing Room"] 
    visited = [False,False,False,False,False,False,False]
    locDetails = ['1','2']
                        
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
                print('''Map
                                    Testing Room
                                        |
                                        |
                                    Datacenter
                    Storage Room        |
                         |              |
                         |              |
     Powercenter-----Servicedesk----Computer lab
                         |   
                         |
                         |
                    Lab Entrance

''')             
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
