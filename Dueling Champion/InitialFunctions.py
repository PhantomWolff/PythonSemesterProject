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

#
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
    heroLevel = input("What is your starting level? ")
    heroTotalHealth = input("What is your starting health? ")
    heroStrength = input("What is your starting strength? ")
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

def start_battle (hero, enemy):
    #Incomplete
    #Battle Initiation
    pass


##################MAIN#######################
    
enemyDict = create_enemy_dictionary()
hero = create_hero()
print(hero.getHeroStats())
hero.damage(3)
print(hero.getHealth())

print(enemyDict["enemy0"].getName() + " will be your first enemy.")

print(enemyDict["enemy0"].getEnemyStats())
    
displayAll(enemyDict["enemy0"])
