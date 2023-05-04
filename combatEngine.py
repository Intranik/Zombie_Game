import json
from random import randrange

#-----------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------

def game_Complete_Reset(): #resets the userhealthdata and the gamedata to its original values
    data = {"Health" : 250}

    with open(("UserHealth.json"), "w") as outfile:
        json.dump(data, outfile)
        outfile.close()
        

    data = {"ZombieDeathCount" : 0,"WeaponType" : 0, "FinalLevel" : "No"}

    with open("GameInfo.json", "w") as gameInfo:
        json.dump(data, gameInfo)
        gameInfo.close()


    print("------------------------------------------------\nsaving data....\n------------------------------------------------")   
    return

#-----------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------

def zombieBattleActions(zombieType):
    zombieAction = randrange(0,2)

    if zombieAction == 0:
        print("The ", zombieType, " attacked, but you blocked its attack")

    elif zombieAction == 1:
        print("The ", zombieType, " stalled and you just stood there watching it")

    elif zombieAction == 2:
        print("Well.... thats awkward the ", zombieType, " blocked as well....")

    return

#-----------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------

def userHealthDisplay(userHealth): #displays the Users Health

    data = {"Health" : userHealth}

    with open(("UserHealth.json"), "w") as outfile:
        json.dump(data, outfile)
        outfile.close()

    print("------------------------------------------------")   
    print("You´re current health is: ", userHealth)
    print("------------------------------------------------")    
    return 

#-----------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------

def zombieHealthDisplay(zombieHealth): #displays the Zombies Health
   
    print("------------------------------------------------")  
    print("Zombies current health is: ", zombieHealth)
    print("------------------------------------------------")
    return 

#-----------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------

def saveGameInfo(zombieDeathCountData,weaponIntTypeData, finalLevel): #saves the game info such as zombieDeathCount (zombies killed), currentWeapon aka weaponType and if its the final level or not

    data = {"ZombieDeathCount" : zombieDeathCountData,"WeaponType" : weaponIntTypeData, "FinalLevel" : finalLevel}


    with open("GameInfo.json", "w") as gameInfo:
        json.dump(data, gameInfo)
        gameInfo.close()
    
    print("Data saved....")
    return

#-----------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------

def zombieBattle(zombieDeathCount, weaponTypeInt, finalLevel):

    #-----------------------------------------------------------------------------------------------------------------------------------------

    if zombieDeathCount < 5: # checks if the zombieDeathCount is below 0 and then sets the next enemy to a normal zombie
        zombieTypeInfo = "Zombie"
    elif zombieDeathCount == 5: # checks if the zombieDeathCount is 5 and then sets the next enemy to the Boss Zombie
        zombieTypeInfo = "BossZombie"

    #-----------------------------------------------------------------------------------------------------------------------------------------

    if weaponTypeInt == 0: # checks the users current weapon with the int "weaponTypeInt"
        weaponName = "Hands"
    elif weaponTypeInt == 1:
        weaponName = "Bat"
    elif weaponTypeInt == 2:
        weaponName = "Gun"
   
    #-----------------------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------

    with open("UserHealth.json") as userData: #displays user data, such as health
        userDatabase = json.load(userData)
        userHealth = userDatabase["Health"]
        userData.close()
        print("------------------------------------------------")
        print("Current User health is: ", userHealth)
        print("------------------------------------------------")

    #-----------------------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------

    with open(weaponName + ".json") as weaponData: #displays weapon data, such name and damage
        WeaponDatabase = json.load(weaponData)
        
        userWeaponName = WeaponDatabase["Name"]
        userDamage = WeaponDatabase["Damage"]
        weaponData.close()
        print("Current Weapon Equipped: ",userWeaponName)
        print("Current Weapon Damage is: ",userDamage)
        print("------------------------------------------------")

    #-----------------------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------

    with open(zombieTypeInfo +".json") as zombieData: #displays zombie data, such name, health and damage
        ZombieDatabase = json.load(zombieData)
        
        zombieType = ZombieDatabase["Name"]
        zombieHealth = ZombieDatabase["Health"]
        zombieDamage = ZombieDatabase["Damage"]
        zombieData.close()

        print("Monster Type: ",zombieType)
        print("Monster Health: ",zombieHealth)
        print("Monster Damage: ",zombieDamage)
        print("------------------------------------------------")

    #-----------------------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------
    
    while True:
        
        if (zombieHealth > 0 and userHealth > 0):

            print("------------------------------------------------")
            actionChoiceInputCheck = input("What do you want to do?\n1. Attack\n2. Block\n3. Stall\n:")
            print("------------------------------------------------")

            if actionChoiceInputCheck.isdigit(): #Checks if the user input a digit if it is it sets the "actionChoiceInput" to an int
                actionChoiceInput = int(actionChoiceInputCheck)
            else: #Checks if the user input a digit if not it just continues and the user gets asked again
                print("Thats not a correct input, try again......")
                continue
            

            if actionChoiceInput == 1: #attacks the zombie
                
                zombieAction = randrange(0,2)

                if zombieAction == 0: #You attack the zombie and it also attacked
                    print("You hit the ", zombieType, " for: ", userDamage, " Damage")
                    print("\nThe ", zombieType, " hit you for: ", zombieDamage, " Damage")

                    newZombieHealth = zombieHealth - userDamage
                    zombieHealth = newZombieHealth

                    newUserHealth = userHealth - zombieDamage
                    userHealth = newUserHealth

                    userHealthDisplay(userHealth) #user damage taken calculation
                    zombieHealthDisplay(zombieHealth) #Zombie health calculation   

                elif zombieAction == 1: #The Zombie blocked you´re attack
                    print("The ", zombieType, " blocked you´re attack")

                elif zombieAction == 2: #You attacked the Zombie and it stalled.....
                    print("Thats awkward the ", zombieType, " just stood there and you hit it for: ", userDamage, " Damage")
                    newZombieHealth = zombieHealth - userDamage
                    zombieHealth = newZombieHealth
                    
                    zombieHealthDisplay(zombieHealth)  #Zombie health calculation   
                

            elif actionChoiceInput == 2: #blocks the zombie attack
                
                zombieBattleActions(zombieType) # start the def that chooses one of three random actions for the zombie, since a block. blocks every other attack
                        

            elif actionChoiceInput == 3: #user just stands there and does nothing
                print("You stand there and wonder what the zombie is thinking......\n come on!, get a grip")
                

                zombieAction = randrange(0,2) #gets a random int between 0-2 to make the zombie do one of three moves

                if zombieAction == 0: #You stalled and the Zombie hit you.....
                    print(zombieType, " hit you for: ", zombieDamage, " Damage")
                    newUserHealth = userHealth - zombieDamage
                    userHealth = newUserHealth

                    userHealthDisplay(userHealth) #user damage taken calulation
                    zombieHealthDisplay(zombieHealth) #Zombie health calculation    

                elif zombieAction == 1: #You stalled and the Zombie just  stood there looking.....
                    print("The ", zombieType, " blocked you´re attack")

                elif zombieAction == 2: #You stalled and the Zombie stalled.....
                    print("Thats awkward the you and the ", zombieType, " just stood there and looked at eachother.....")
                    
                    print("You´re current health is: ", userHealth)
                    zombieHealthDisplay(zombieHealth)  #Zombie health calculation 


                userHealthDisplay(userHealth) #move this out, user damage taken calulation        
            
            else:
                pass

            continue

    #-----------------------------------------------------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------

        elif (userHealth > 0 and zombieHealth <= 0): # checks if the userhealth is 0 or above and if the zombie is 0 or below
            print("You defeated the ", zombieType)

            if zombieType == "Boss Zombie": #checks if the zombie you faced was the boss zombie or a normal zombie
                
                if finalLevel == "Yes": #checks if the final level is active if it is the game ends and you win....
                    print("Congratulations You Won The Game!")
                    game_Complete_Reset() #resets all user data and zombie kill count data
                    quit()
                
                elif finalLevel == "No": #checks if the final level is active if it isnt the game knows it can load a new world....
                    print("------------------------------------------------")
                    print("You defeated the Boss Zombie, but its not over yet.....\n")
                    userHeal = userHealth + 100

                    userHealthDisplay(userHeal) #heals the user after killing the zombie

                    finalLevel = "Yes"                  
                print("------------------------------------------------")
                zombieDeathCount = 0
                weaponTypeInt = 0
                saveGameInfo(zombieDeathCount,weaponTypeInt, finalLevel)
                return
            else:
                print("------------------------------------------------")
                print("You gained 30 health from killing the Zombie")
                userHeal = userHealth + 30
                userHealthDisplay(userHeal) #heals the user after killing the zombie


                newDeathCount = zombieDeathCount +1
                zombieDeathCount = newDeathCount
                #print("Zombie Death Count: ",zombieDeathCount) #test function.... ignore....

                print("------------------------------------------------")
                weaponChoiceInput = input("the Zombie dropped a weapon, would you like to pick it up?\n Y/N")
                print("------------------------------------------------")
                
                if weaponChoiceInput == "Y" or "y": #checks if user wants to pick-up a new weapon

                    NewWeaponType = randrange(0,2) #sets a rando int that gives the user a random weapon

                    if NewWeaponType == 0: #user drops its weapon and uses its hands
                        weaponTypeInt = NewWeaponType
                        saveGameInfo(zombieDeathCount,weaponTypeInt, finalLevel)
                        print("You decided to not pick-up the weapon and use you´re hands instead")
                        
                    elif NewWeaponType == 1: #user pick-ups a bat
                        weaponTypeInt = NewWeaponType
                        saveGameInfo(zombieDeathCount,weaponTypeInt, finalLevel)
                        print("You decided to pick-up a Bat from the Zombie")

                    elif NewWeaponType == 2: #user pick-ups a shotgun
                        weaponTypeInt = NewWeaponType
                        saveGameInfo(zombieDeathCount,weaponTypeInt, finalLevel)
                        print("You decided to pick-up a ShotGun from the Zombie")
                
                elif weaponChoiceInput == "n" or "N":
                    print("You decided to not pickup the weapon from the zombie")   
                    saveGameInfo(zombieDeathCount,weaponTypeInt, finalLevel)
                else:
                    print("You decided to not pickup the weapon from the zombie")   
                    saveGameInfo(zombieDeathCount,weaponTypeInt, finalLevel)
                return


        elif userHealth <= 0: #checks if the user got 0 health or below and then resets the games json files to the start value and then quits the game

            game_Complete_Reset() 

            print("-------------------------------------------------")
            print("****GAME OVER****\n****You Died****")
            print("-------------------------------------------------")
            
            quit()

#-----------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------

def zombieBattleSetup(): #gives the "ZombieBattle" def all its nessecary values so it can work without having to be called outside the scirpt

    with open("GameInfo.json") as gameInfo:
        userDatabase = json.load(gameInfo)
        zombieDeathCountData = userDatabase["ZombieDeathCount"]
        weaponTypeData = userDatabase["WeaponType"]
        finalLevel = userDatabase["FinalLevel"]
        gameInfo.close()

    zombieBattle(zombieDeathCountData, weaponTypeData, finalLevel)
    return


#-----------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------

#ZombieBattleSetup() # calls the setup function that starts the game.
