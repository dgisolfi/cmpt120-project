#Into to programing
#Author: Daniel Gisolfi
#Date: 9/22/16
#TextGame.py

def game():
    #Start Game
    ##Game Settings
    title = "The Abandoned Lab:" 
    playername = ''
    backstory =  ("You have arrived at a large metal door leading to an abandoned" 
                  " Computer labratory, explore inside to discover new technology")
    score = int(0)
    ##Game Locations   
    
    labentrance = "You are at the Lab entrance"
    computerlab = "You are in the Computer Lab"
    datacenter =  "You are in the Data Center"
    servicedesk =  "You are at the Service Desk"

    ###Locations Visited
    labentranceVisited = True
    computerlabVisted = False
    datacenterVisted = False
    servicedeskVisted = False
    
    #Game Start
    playerlocation = labentrance
    
    print(title)
    print(backstory)
    print(playerlocation)
    input("Press Enter to continue")

    #Game loop
    while True:
        userinput = input("Which direction would you like to go?: ")
        userinput = userinput.lower()

        if userinput == "north":
            if playerlocation == labentrance:
                playerlocation = servicedesk
                servicedeskVisted = True

            elif playerlocation == servicedesk:
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
                

            elif playerlocation == computerlab:
                print("there is a wall there")
	
            elif playerlocation == datacenter:
                playerlocation = computerlab
                computerlabVisted = True

            print(playerlocation)
        
    conclusion = "Congradulations, you found the data center and new technology inside"
    copyright = "Copyright (c) 2016 Daniel Gisolfi, Daniel.Gisolfi1@marist.edu"
    print(conclusion)
    print(copyright)


game()
