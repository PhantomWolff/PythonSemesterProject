#Dueling Champion
#Created by David Schmitt

from ClassCharacter import Enemy
from ClassCharacter import Hero
import random

#Takes the file of enemies and creates a nested list of enemies and stats
def getStatList () -> list:
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
    allStatList = getStatList()
    enemyDict = {}
    i = 0
    for line in allStatList:
        enemyName = line[0]
        enemyID = line[1]
        enemyDict["enemy" + str(i)] = Enemy(line)
        i += 1
    return enemyDict

#Creates the hero object. Should be one of the first things the user sees.
def create_hero () -> object:
    #Incomplete but working
    heroName = input("Hello adventurer! What is your name? ")
    #heroLevel = input("What is your starting level? ")
    heroLevel = "1"
    #heroTotalHealth = input("What is your starting health? ")
    heroTotalHealth = "10"
    #heroStrength = input("What is your starting strength? ")
    heroStrength = "3"
    heroInitList = [heroName, heroLevel, heroTotalHealth, heroStrength]
    hero = Hero(heroInitList)
    return hero

def displayAll (enemy):
    print()
    print("***************************")
    enemy.displayName()
    enemy.displayLevel()
    enemy.displayHealth()
    enemy.displayTotalHealth()
    enemy.displayStrength()
    enemy.displayExpValue()
    enemy.displayGoldValue()

def start_battle (hero, opponent):
    #Incomplete
    #Battle Initiation
    print("*" * 38)
    print("|{:<8s}{:>8s} | {:<8s}{:>8s} |".format("Name:", hero.getName(), "Name:", opponent.getName()))
    print("|{:<8s}{:>8s} | {:<8s}{:>8s} |".format("Level:", hero.getLevel(), "Level:", opponent.getLevel()))
    print("|{:<8s}{:>8s} | {:<8s}{:>8s} |".format("Health:", hero.getHealthFraction(), "Health:", opponent.getHealthFraction()))
    
    print("*" * 38)
    print("\n")

##################MAIN#####################

#Instantiate characters    
enemyDict = create_enemy_dictionary()
hero = create_hero()
print("\n\n")

print(hero.getHeroStats())

enemyNumber = 0

#
opponent = enemyDict["enemy" + str(enemyNumber)]

print(opponent.getName() + " will be your first enemy.")
input()
start_battle(hero, opponent)
