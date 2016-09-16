#Into to programing
#Author: Daniel Gisolfi
#Date: 9/13/16
#CMPT-Version0.1

def main():
#Start Game
    title = "The Abandoned Lab:"
    backstory =  "You have arrived at a large metal door leading to an abandoned computer labratory, explore inside to discover new technology"
    labentrance = "You are at the Lab entrance"
    computerlab = "You are in the Computer Lab"
    datacenter =  "You are in the Data Center"
    servicedesk =  "You are at the Service Desk"
    score = int(0)
    playerlocation = labentrance
    print(title)
    print(backstory)
    print(playerlocation)
    input("Press Enter to continue")

#Game
    x = int(0)
    while x < 3:
        if x == 0:
            playerlocation = computerlab
        elif x == 1:
            playerlocation = servicedesk
        elif x == 2:
            playerlocation = datacenter
            
        score = score + 5
        print(playerlocation,"Your score is",score)
        input("Press Enter to continue")
        x = x + 1

#End Game
    conclusion = "Congradulations, you found the data center and new technology inside"
    copyright = "Name: Daniel Gisolfi Email: Daniel.Gisolfi1@marist.edu"
    print(conclusion)
    print(copyright)

main()

	
