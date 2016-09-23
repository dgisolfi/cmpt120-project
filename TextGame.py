#Into to programing
#Author: Daniel Gisolfi
#Date: 9/22/16
#TextGame.py

def game():
    #Start Game
    ##Game Settings
    title = "The Abandoned Lab:"
    print(title)
    playername = input("Enter the name of your player: ")

    backstory =  playername,(" has arrived at a large metal door\n"
                             "leading to an abandoned Computer labratory,explore"
                             "\ninside to discover new technology")
    score = int(0)
    ##Game Locations   
    
    labentrance = "You are at the Lab entrance"
    servicedesk =  "You are at the Service Desk"
    powercenter = "You are at the Power Center"
    computerlab = "You are in the Computer Lab"
    datacenter =  "You are in the Data Center"
    

    ###Locations Visited
    labentranceVisited = True
    servicedeskVisted = False
    computerlabVisted = False
    datacenterVisted = False
    powercenterVisited = False
        
    #Game Start
    playerlocation = labentrance
    
    
    print()
    print(backstory)
    print(playerlocation)

    #Game loop
    while True:
        userinput = input("Which direction would you like to go?: \n")
        userinput = userinput.lower()

        if userinput == "north":
            if playerlocation == labentrance:
                playerlocation = servicedesk
                servicedeskVisted = True

            elif playerlocation == servicedesk:
                print("there is a wall there")

            elif playerlocation == powercenter:
                print("there is a wall there")

            elif playerlocation == computerlab:
                playerlocation = datacenter
                datacenterVisted = True
	
            elif playerlocation == datacenter:
                print("there is a wall there")
        elif userinput == "south":
            
            if playerlocation == labentrance:
                print("there is a wall there")

            elif playerlocation == servicedesk:
                playerlocation = labentrance

            elif playerlocation == powercenter:
                print("there is a wall there")
                
            elif playerlocation == computerlab:
                print("there is a wall there")
	
            elif playerlocation == datacenter:
                playerlocation = computerlab
                

        elif userinput == "east":

            if playerlocation == labentrance:
                print("there is a wall there")
                
            elif playerlocation == servicedesk:
                playerlocation = computerlab
                computerlabVisted = True

            elif playerlocation == powercenter:
                playerlocation = servicedesk
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
       
        print(playerlocation)           

    conclusion = "Congratulations, you found the data center and new technology inside"
    copyright = "Copyright (c) 2016 Daniel Gisolfi, Daniel.Gisolfi1@marist.edu"
    print(conclusion)
    print(copyright)


game()
