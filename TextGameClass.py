#Into to programing
#Author: Daniel Gisolfi
#Date: 12/14/16
#TextGameClass.py
#Version 1.0

class Player:
    
    MAX_ITEMS = 5
    
    def __init__(self, name):
        self.name = name    #atrributes of player
        self.location = 0
        self.score = 0
        self.inventory = []
        self.moveCount = 0

    def examine(self):
        if len(self.inventory) < Player.MAX_ITEMS: #checks if the current location matches any locations in the items list:
            outputText.insert(END,"There is a", locations[self.location].item, "in the area" )#reveal
            outputText.insert(END,locations[self.location].descrip)
        else:
            outputText.insert(END,"there is no item in this area")#let the player know there is not a item in this area

    def take(self, item):
        if len(self.inventory) < Player.MAX_ITEMS:
            if item in locations[self.location].item:
                self.inventory.append()
            else:
                outputText.insert(END,"that item is not here")
        else:
            ending()

    def drop(self, item):
        self.inventory.remove(locations[self.location].item)
        locations[self.location].item = item


class Locale:

    def __init__(self, name, descrip, visited, item):
        self.name = name    #attributes of locations
        self.descrip = descrip
        self.visited = False
        self.item = item

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

    Locale("Testing Room","In this room lies the finished technologies of the lab that were left, you see dozons of items that untill now only"
        +" seemed science fiction, including a small mech suit which you can use to get back to civilization.",False, "Power shoes"),

    Locale("Network Room","A small compact room filled with ethernet cables connected to various machines.",False, ""),

    Locale("Manufacturing Lab","An old manufacturing room where assembly lines are set up with products in various stages of completion",False, "Battery"),
    
    Locale("A.I. Facility", "A room filled with computers and hard drives for the purpose of creating a AI", False, ""),

    Locale("Break Room", "room devoted to eating and taking breaks from the high level of stress at work", False, "Crowbar")]

class Item:

    def __init__(self,name,descrip):
        self.name = name
        self.descrip = descrip

items = [
    Item("map","a pecie of paper that shows were locations of the game are"),
    Item("keycard","a Id card that grants accss to rooms"),
    Item("FlashLight","a old fashlight that still needs a battery"),
    Item("Power shoes","shoes that allow the user to move quicker"),
    Item("Battery","a battery that still holds a charge and can power a flashlight"),
    Item("Crowbar", "A ong peice of metal used to pry")]


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
[-1,4,7,-1],
[-1,-1,-1,7],
[-1,-1,-1,5]]



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
NetworkRoom = 8
ManufacturingRoom = 9
aiFacility = 10
breakRoom = 11

# Give the player a placeholder, get the real name later with playerCustom
player = Player("noname")
