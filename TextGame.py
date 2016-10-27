#Into to programing
#Author: Daniel Gisolfi
#Date: 9/22/16
#TextGame.py
#Version 0.3

def game():
    #Start Game
    
    ##Game Locations 
    allLoc = ["labentrance","servicedesk", "powercenter","Storage room", "computerlab", "datacenter","Testing Room"] 
    
    ###Location Descriptions
    locDetails = [
        #Lab Entrance
        ("You come to the entrance where a large metal door used to stand protecting the lab and the nerds inside from the"
        +" wilderness. There is now just a large opening leading into the dark lab. Head inside to further explore the lab")
        #servicedesk
        (" Entering the lab there is a service desk waiting dead ahead dimly lit only by the flickering CRT monitors left"
        +" behind. there seems to be nothing here but unless computers from the 90s and lots of crumpled papers.")
        #powercenter
        ("Huge generators fill the room, they are all shutdown as the main power switch is turned off,"
        +" the backup battery seems to be charged and is the only source of power for the lab currently")
        #Storage room
        ("Behind the door to the storage room lies shelves upon shelves of prtotypes of jetpacks, flying cars and hoverboards")
        #Computerlab
        ("In the computer lab there is little walking space as the room was stuffed to the max with as many cubicles that"
        +" would fit. There is a lone ceiling fan missing half its blades with plenty of trashed computers, paper and floppy"
        +" disks scattered across the room.")
        #datacenter
        ("Large mainframes hold mass amounts of data collected by the lab while it was operational,"
        +" including all reports of experiments and tests")
        #Testing Room
        ("In this room lies the finished technologies of the lab that where left, you see dozons of itmes that untill now only"
        +" seemed science fiction, including a small mech suit which you can use to get back to civilization.")
        ] 


    def playercustom():
        global playername, score
        playername = input("Enter the name of your player: ")
        score = int(0)
    playercustom()
    def titleScreen():
        title = "The Abandoned Lab:"
        print(title)
    titleScreen()
    def gameintro(): 
        global playerlocation 
        backstory = playername + (", you are lost in the woods and searching for any relief from civilization"
                            +" you come across what used to be a scientific laboratory researching new technologies"
                            +" in the side of a mountain. The lab appears abandoned but could hold the key to surviving" 
                            +" nature…New technology!!! Explore inside to find some. \n")
        playerlocation = allLoc[0]
        print()
        print(backstory)
        print()
        print(playerlocation)
    gameintro()
    
    

    
    

    

    ####Locations Visited

    locVisit = []

    '''Map
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

    '''
    

    #Game loop

  
    def cmd():
        while True:
            cmd = input("Which direction would you like to go?: \n")
            cmd = userinput.lower()

            if userinput == "north":
                if playerlocation == labentrance:
                    playerlocation = servicedesk
                    if servicedeskVisted == False:
                        score = score + 5
                        servicedeskVisted = True

                elif playerlocation == servicedesk:
                    print("there is a wall there")

                elif playerlocation == powercenter:
                    print("there is a wall there")

                elif playerlocation == computerlab:
                    playerlocation = datacenter
                    if datacenterVisted == False:
                        score = score + 5
                        datacenterVisted = True
                    break
                elif playerlocation == datacenter:
                    print("there is a wall there")
            
            elif userinput == "south":
                
                if playerlocation == labentrance:
                    print("there is a wall there")

                elif playerlocation == servicedesk:
                    playerlocation = labentrance
                    if labentranceVisited == False:
                        score = score + 5
                        labentranceVisited = True

                elif playerlocation == powercenter:
                    print("there is a wall there")
                    
                elif playerlocation == computerlab:
                    print("there is a wall there")
    	
                elif playerlocation == datacenter:
                    playerlocation = computerlab
                    if computerlabVisted == False:
                        score = score + 5
                        computerlabVisted = True

            elif userinput == "east":

                if playerlocation == labentrance:
                    print("there is a wall there")
                    
                elif playerlocation == servicedesk:
                    playerlocation = computerlab
                    if computerlabVisted == False:
                        score = score + 5
                        computerlabVisted = True

                elif playerlocation == powercenter:
                    playerlocation = servicedesk
                    if servicedeskVisted == False:
                        score = score + 5
                        servicedeskVisted = True

                elif playerlocation == computerlab:
                    print("there is a wall there")
                
                elif playerlocation == datacenter:
                    print("there is a wall there")
                    
            elif userinput == "west":

                if playerlocation == labentrance:
                    print("there is a wall there")
                    
                elif playerlocation == servicedesk:
                    playerlocation = powercenter
                    if powercenterVisited == False:
                        score = score + 5
                        powercenterVisited = True

                elif playerlocation == powercenter:
                    print("there is a wall there")
                    
                elif playerlocation == computerlab:
                    print("there is a wall there")
                
                elif playerlocation == datacenter:
                    print("there is a wall there")

            elif userinput == "help":
                print("This is a list of vaid commands:"
                      "\nnorth"
                      "\nsouth"
                      "\neast"
                      "\nwest"
                      "\nhelp"
                      "\nquit\n")
            
            elif userinput == "quit":
                break
            else:
                print("that is not a valid command")
                
            print()
            print(playerlocation)
            print("score = ",score)
    cmd()
        
    #End Game
    def ending():
        conclusion = "Congratulations " + playername + ", you found the data center and new technology inside"
        copyright = "Copyright (c) 2016 Daniel Gisolfi, Daniel.Gisolfi1@marist.edu"
        print()
        print(conclusion)
        print(copyright)
    ending()

game()








# def main():
#   x = 0
#   addToX()
#   print(x)

# def addToX():
#   x = x+10

# main()
def game():
    #Start Game
    
    ##Game Locations 
    allLoc = ["labentrance","servicedesk", "powercenter","Storage room", "computerlab", "datacenter","Testing Room"] 
    
    visited = []
    def playercustom():
        global playername, score
        playername = input("Enter the name of your player: ")
        score = int(0)
    playercustom()
    def titleScreen():
        title = "The Abandoned Lab:"
        print(title)
    titleScreen()
    def gameintro(): 
        global playerlocation 
        backstory = playername + (", you are lost in the woods and searching for any relief from civilization"
                            +" you come across what used to be a scientific laboratory researching new technologies"
                            +" in the side of a mountain. The lab appears abandoned but could hold the key to surviving" 
                            +" nature…New technology!!! Explore inside to find some. \n")
        playerlocation = allLoc[0]
        print()
        print(backstory)
        print()
        print(playerlocation)
    gameintro()

    def move(dest):
            global score, visited, currLoc
            currLoc = dest
            if not visited[dest]:
                visited[dest] = true
                score += 5


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
                    move(6)
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
                print()
            
            elif cmd == "quit":
                break
            
            elif cmd == "points":
                print(score) 

            elif cmd == "map":
                print()             


    userinput()
game()

