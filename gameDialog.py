import json
import sys
import time
from combatEngine import game_Complete_Reset 
from moveScript import play


a = 2
b = 0.2
c = 0.08
d = 3

def increaseLevelData(CurrentLevel): #Updates current level to itself +1
    newCurrentLevel = CurrentLevel +1
    data = {"CurrentLevel" : newCurrentLevel}

    with open("CurrentLevel.json", "w") as levelData: #opens "CurrenLevel" in write mode...
        json.dump(data, levelData)
        levelData.close()
    return

def resetAllData(): #resets all level and player data....
    data = {"CurrentLevel" : 1}

    with open("CurrentLevel.json", "w") as levelData:
        json.dump(data, levelData)
        levelData.close()

    game_Complete_Reset()
    return

def slowText(dialog):
    for character in dialog:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(1.0)
    return


def dialogDisplay(CurrentLevel): #prints the dialog depending if level is 1 or 2

    print('-----------------------------------------------------------------------------------')
    print('-----------------------------------------------------------------------------------')
    
   

    if CurrentLevel == 1:
        newLevelDialog = '*****BOOOOOOOOM******\n.....You wake up from the sound of a lightning Bolt ....  strikring down behind you...'
        slowText(newLevelDialog)
        print('-----------------------------------------------------------------------------------')
        dialogForrest = 'It´s night, you wake up in a dark forrest and you hear a sound behind you and you decide to run.....'
        print('-----------------------------------------------------------------------------------')

        slowText(dialogForrest)

    elif CurrentLevel == 2:
        
        print('-----------------------------------------------------------------------------------')
        dialogCity = ('You have defeated one of the Zombie bosses, \nand you decide to head into the city to face the final Zombie Boss and its zombie servants......')
        print('-----------------------------------------------------------------------------------')
    
        slowText(dialogCity)
        
    return


def setUpMovementFunction(): #set-up for the movement script where the scirpt gets the current level as an int 
    while True:

        with open("CurrentLevel.json") as levelInfo: #opens the json file "CurrenLevel" and loads its data called "Currenlevel"
            levelDatabase = json.load(levelInfo) #loads in all data from "currentlevel"
            currentLevelData = levelDatabase["CurrentLevel"]
            levelInfo.close()  

        dialogDisplay(currentLevelData)

        if currentLevelData == 1:
            increaseLevelData(currentLevelData)
            play(currentLevelData)
            
        elif currentLevelData == 2:
            play(currentLevelData)

    
    

def gameIntro():
    print("")
    print('In 1990 some Nackademin polytechnic scientists discovered a virus in the north that reacted in different ways when it came into contact with mammals.')
    print('especially humans and transformed them into ZOMBIES!')
    print('one of the scientists returns to Stockholm with the virus.')
    print("")
    time.sleep(a)
    print('when he got home he turned into a Zombie')
    time.sleep(a)
    print('he contaminated all the people around him')
    print('except his little son Jonathan')
    time.sleep(a)
    print('he was the only one who escaped')
    time.sleep(a)
    print('little jonathan ran until he passed out')
    time.sleep(a)
    print('Now he started to wake up')
    print("")
    question = 'where am i? where should i go?'
    slowText(question)
    return

def startUpText():
    print("")
    print("")
    print("     ######################")
    print("     |                    |")
    print("     |       Zombierpg    |")
    print("     |                    |")
    print("     ######################")
    print("")
    print("")
    time.sleep(a)
    print('!!!WARNING!!!')
    print("")
    time.sleep(d)
    print('This game contains EXPLICIT language and violence that some viewers might find upsetting.')
    time.sleep(d)
    print('RESTRICTED under 18 REQUIRES accompanying parent or adult guardian')
    time.sleep(a)
    print()
    print()          
    return


def startGame():

    startUpText()
    userInputCheck = input('Do you dare to play?\n1.Yes\n2.No\n: ')

    resetAllData() #resets all data on start-up
    
    while True:        

        if userInputCheck.isdigit(): #checks if the user put a digit in...
            userInput = int(userInputCheck) #sets userinput to an int if its an int

            if userInput == 1:
                gameIntro()
                setUpMovementFunction()

            elif userInput == 2:
                quit()
        else:
            print('Thats not an int')

