from exm import Room
from combatEngine import zombieBattleSetup 
import json

def createForrest():
    forest = Room("****** YOU ARE IN THE DARK FORREST ******")
    forest1 = Room("You take a step North into the Dark Forrest")
    forest2 = Room("You take a step South into the Dark Forrest")
    forest3 = Room("You take a step East into the Dark Forrest")
    forest4 = Room("You take a step West into the Dark Forrest")
    forest5 = Room("You take a step NorthEast into the Dark Forrest")
    forest6 = Room("You take a step NorthWest into the Dark Forrest")
    forest7 = Room("You take a step SouthEasst into the Dark Forrest")
    forest8 = Room("You take a step SouthWest into the Dark Forrest")

    forest.setRoomToTheNorth(forest1) # plains is north of forest
    forest1.setRoomToTheSouth(forest)
    forest.setRoomToTheSouth(forest2)
    forest2.setRoomToTheNorth(forest)
    forest.setRoomToTheEast(forest3)
    forest3.setRoomToTheWest(forest)
    forest.setRoomToTheWest(forest4)
    forest4.setRoomToTheEast(forest)
    forest.setRoomToTheNorthEast(forest5)
    forest5.setRoomToTheSouthWest(forest)
    forest.setRoomToTheNorthWest(forest6)
    forest6.setRoomToTheSouthEast(forest)
    forest.setRoomToTheSouthEast(forest7)
    forest7.setRoomToTheNorthWest(forest)
    forest.setRoomToTheSouthWest(forest8)
    forest8.setRoomToTheNorthEast(forest)

    return forest # return the starting location
 

def createCity():
    city = Room("****** YOU ARE IN THE CITY ******")
    city1 = Room("You take a step North into the City")
    city2 = Room("You take a step South into the City")
    city3 = Room("You take a step East into the City")
    city4 = Room("You take a step West into the City")
    city5 = Room("You take a step NorthEast into the City")
    city6 = Room("You take a step NorthWest into the City")
    city7 = Room("You take a step SouthEasst into the City")
    city8 = Room("You take a step SouthWest into the City")

    city.setRoomToTheNorth(city1) # plains is north of forest
    city1.setRoomToTheSouth(city)
    city.setRoomToTheSouth(city2)
    city2.setRoomToTheNorth(city)
    city.setRoomToTheEast(city3)
    city3.setRoomToTheWest(city)
    city.setRoomToTheWest(city4)
    city4.setRoomToTheEast(city)
    city.setRoomToTheNorthEast(city5)
    city5.setRoomToTheSouthWest(city)
    city.setRoomToTheNorthWest(city6)
    city6.setRoomToTheSouthEast(city)
    city.setRoomToTheSouthEast(city7)
    city7.setRoomToTheNorthWest(city)
    city.setRoomToTheSouthWest(city8)
    city8.setRoomToTheNorthEast(city)

    
    return city # return the starting location


def printPlayerState(currentRoom: Room):
    print("-----------------------------------------------------------------------------------") # a separator line between player turns
    print("Location: " + currentRoom.getName())
 
def getRoomInDirection(currentRoom: Room, direction):
    if direction == "1" : # the player wants to move north
        return currentRoom.getRoomToTheNorth() 
    elif direction == "2" : # the player wants to move south
        return currentRoom.getRoomToTheSouth() 
    elif direction == "3": # the player wants to move west
        return currentRoom.getRoomToTheWest() 
    elif direction == "4" : # the player wants to move east
        return currentRoom.getRoomToTheEast() 
    elif direction == "5" : # the player wants to move northeast
        return currentRoom.getRoomToTheNorthWest()
    elif direction == "6" : # the player wants to move northwest
        return currentRoom.getRoomToTheNorthEast()
    elif direction == "7" : # the player wants to move southeast
        return currentRoom.getRoomToTheSouthWast()
    elif direction == "8" : # the player wants to move southwest
        return currentRoom.getRoomToTheSouthEast()


def setUpRoom(currentRoom):
    while True:
        printPlayerState(currentRoom)
        print("\n1 = North, 2 = South, 3 = West, 4 = South\n") 
        print("5 = NorthWest, 6 = NorthEast, 7 = SouthWest, 8 = SouthEast\n")
        commandInput = input("What do you wish to do?")
        command = ("go " + commandInput)
        subcommands = command.split(" ") # split “go” and “north”

        if subcommands[0] == "go" : # the player wants to move
            newRoom = getRoomInDirection(currentRoom, subcommands[1])
            if newRoom == None :
                print("You are unable to move further " + subcommands[1])
            else :
                currentRoom = newRoom # perform the actual move

        printPlayerState(currentRoom)
        print("\nOh?.... what is that sound?\n.... Oh no its a Zombie get ready to fight...\n")
        return
 
def play (currenLevel) :
    KeepPlaying = True

    while KeepPlaying  :        
        with open("GameInfo.json") as gameInfo: #reads gameinfo for zombiedeathcount and takes its varible (int) 
            gameInfoDatabase = json.load(gameInfo)
            zombieDeathCount = gameInfoDatabase["ZombieDeathCount"]
            gameInfo.close()

        if currenLevel == 1:
            #User is in the forrest
            currentRoom = createForrest()


        elif currenLevel == 2:
            #User is in the city
            currentRoom = createCity()

        setUpRoom(currentRoom) 
        

        zombieBattleSetup()

        if zombieDeathCount == 5:
            break

