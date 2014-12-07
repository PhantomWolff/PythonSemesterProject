from ClassCharacter import Character
import random

def getStatList () -> list:
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

#takes the list of lists and saves each enemy as its own object in class enemy
def create_enemies (allStatList: list) -> list:
    enemyList = []
    i = 0
    for line in allStatList:
        enemyName = line[0]
        enemy1 = Character(line)
        enemyList.append(enemyName)
        i += 1
    return enemyList

def create_enemy_dictionary (allStatList: list) -> dict:
    enemyDict = {}
    i = 0
    for line in allStatList:
        enemyName = line[0]
        enemyID = line[1]
        enemyDict[str(i)] = Character(line)
        i += 1
    return enemyDict
#MAIN
allStatList = getStatList()
enemy1 = create_enemy_dictionary(allStatList)
print(enemy)
enemy1.getLevel())
#print(enemy[1].getLevel())
#allStatList[i][0] = str("enemy" + str(i))
#apple = str("enemy" + str(i))
#print(apple)