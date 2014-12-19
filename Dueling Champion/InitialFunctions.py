#Dueling Champion
#Created by David Schmitt

from ClassCharacter import Enemy
from ClassCharacter import Hero
import random
import sys

#####################Before game starts#############################
#Takes the file of enemies and creates a nested list of enemies and stats
def get_stat_list () -> list:
    #Complete
    statFile = open("StatList.txt", "r")
    allStatList = []
    for line in statFile:
        line = str(line)
        statList = line.split(",")
        allStatList.append(statList[:])
    allStatList.remove(allStatList[0])
    for line in allStatList:
        line[-1] = line[-1].rstrip()
    statFile.close()
    return allStatList

#takes the list of lists and saves each enemy as its own object in class enemy.
#Currently not planning on using this function, but might change my mind.
def create_enemies (allStatList: list) -> list:
    #Complete
    enemyList = []
    i = 0
    for line in allStatList:
        enemyName = line[0]
        enemy1 = Enemy(line)
        enemyList.append(enemyName)
        i += 1
    return enemyList

#gets the list of stats and creates each enemy inside of a dictionary. 
#To use the enemy0 object, type >>> enemyDict["enemy0"].method()
def create_enemy_dictionary () -> dict:
    #Complete
    allStatList = get_stat_list()
    enemyDict = {}
    i = 0
    for line in allStatList:
        enemyName = line[0]
        enemyID = line[1]
        enemyDict["enemy" + str(i)] = Enemy(line)
        i += 1
    return enemyDict
####################################################################


##########Functions to call for any point in the game###############
def goto_main_menu ():
    menuOptions = ["quit", "stats", "back", "shop", "fight"]
    #Quick for loop to decide the max length of the column
    maxLength = len(menuOptions[0])
    for option in menuOptions:
        if maxLength < len(option):
            maxLength = len(option)
    print("{:*<{}s}".format("", 13))
    print("|{:^11s}|".format("Main Menu"))
    print("{:*<{}s}".format("", 13))
    for option in menuOptions:
        print ("|{:^{}s}|".format(option, 11))
    print("{:*<{}s}".format("", 13))
    
    selection = input("Type your selection: ")
    #Something in here is bad and evil
    while True:
        if selection == "quit":
            print ("quit")
            break
        elif selection == "stats":
            print ("stats")
            break
        elif selection == "back":
            print ("back")
            break
        elif selection == "shop":
            print ("shop")
            break
        elif selection == "fight":
            print ("fight")
            break
        else:
            print ("Not a valid option. Returning to game.")
            break
        
def check_keywords (userInput: str):
    if userInput.lower() == "exit":
        confirm = input("Are you sure you want to exit? (yes/no): ").lower()
        while True:
            if confirm == "yes":
                print("Thanks for playing!")
                sys.exit()
            elif confirm == "no":
                break
            else:
                confirm = input("Please type 'yes' or 'no'")
                
    else:
        pass
        
        
def display_all (enemy):
    print()
    print("*" * 26)
    enemy.displayName()
    enemy.displayLevel()
    enemy.displayHealth()
    enemy.displayTotalHealth()
    enemy.displayStrength()
    enemy.displayExpValue()
    enemy.displayGoldValue()

def start_battle (hero, opponent):
    display_battle_table (hero, opponent)
        
def display_battle_table (hero, opponent):
    #Working, but additions will be made.
    print("*" * 38)
    print("|{:<8s}{:>8s} | {:<8s}{:>8s} |".format("Name:", hero.getName(), "Name:", opponent.getName()))
    print("|{:<8s}{:>8s} | {:<8s}{:>8s} |".format("Level:", hero.getLevel(), "Level:", opponent.getLevel()))
    print("|{:<8s}{:>8s} | {:<8s}{:>8s} |".format("Health:", hero.getHealthFraction(), "Health:", opponent.getHealthFraction()))
    print("*" * 38)
    print("\n")
####################################################################


########Functions for a specific time/single use in the game########

#Creates the hero object. Should be one of the first things the user sees.
def create_hero () -> object:
    #Incomplete but working
    heroName = input("Greetings, adventurer! What is your name? ")
    #heroLevel = input("What is your starting level? ")
    heroLevel = "1"
    #heroTotalHealth = input("What is your starting health? ")
    heroTotalHealth = "15"
    #heroStrength = input("What is your starting strength? ")
    heroStrength = "4"
    heroInitList = [heroName, heroLevel, heroTotalHealth, heroStrength]
    hero = Hero(heroInitList)
    print("It is a pleasure to meet you, " + hero.getName())
    return hero

####################################################################


##################MAIN#####################
#Instantiate characters    
enemyDict = create_enemy_dictionary()
hero = create_hero()
print("\n\n")

enemyNumber = 0

#Changes an enemy number to the current opponent
opponent = enemyDict["enemy" + str(enemyNumber)]

print(opponent.getName() + " will be your first enemy.")
userInput = input("(Press Enter)")
check_keywords(userInput)
goto_main_menu()
start_battle(hero, opponent)