import random

#HERO CLASS
class Hero(object):
    def __init__ (self, heroInitList):
        #all variables are stored as strings
        self.__name = heroInitList[0]
        self.__level = heroInitList[1]
        self.__health = heroInitList[2]
        self.__totalHealth = heroInitList[2]
        self.__strength = heroInitList[3]
        self.__exp = "0"
        
#Methods to retreive specific class information
    def getName (self):
        return self.__name
    def getLevel (self):
        return self.__level
    def getHealth (self):
        return self.__health
    def getTotalHealth (self):
        return self.__totalHealth
    def getHealthFraction (self):
        return self.__health + "/" + self.__totalHealth    
    def getStrength (self):
        return self.__strength
    def getHeroStats (self):
            heroStats = ["Name:" + self.__name, "Level:" + self.__level, "Health:" + self.__health, "Total Health:" + self.__totalHealth, "Strength:" + self.__strength]
            return heroStats   

#Methods to display specific class information for the user
    def displayName (self):
        print ("Your Name is " + self.__name)
    def displayLevel (self):
        print ("You are level " + self.__level)
    def displayHealth (self):
        print ("You currently have " + self.__health + " out of " + self.__totalHealth + " health")
    def displayTotalHealth (self):
        print ("Your maximum health is " + self.__totalHealth)
    def displayStrength (self):
        print ("Your strength is " + self.__strength)

#Methods to change stats
    def levelUp(self):
        self.__level += 1
        
    def changeTotalHealth(self, healthUpgrade):
        self.__totalHealth = self.__totalHealth + healthChange
        self.__health = self.__totalHealth
    
    def damage(self, damage):
        self.__health = str(int(self.__health) - damage)
        
            



#ENEMY CLASS
class Enemy(object):
    #Enemy constructor    
    def __init__ (self, statLine):
        #all variables are stored as strings
        self.__ID = statLine[0]
        self.__name = statLine[1]
        self.__level = statLine[2]
        self.__health = statLine[3]
        self.__totalHealth = statLine[3]
        self.__strength = statLine[4]
        self.__expValue = str(int(self.__level) * 10)
        self.__goldValue = str(int(self.__level) * (5 + random.randint(1,10)))

#Methods to receive specific class information
    def getID (self):
        return self.__ID
    def getName (self):
        return self.__name
    def getLevel (self):
        return self.__level
    def getHealth (self):
        return self.__health
    def getTotalHealth (self):
        return self.__totalHealth
    def getHealthFraction (self):
        return self.__health + "/" + self.__totalHealth
    def getStrength (self):
        return self.__strength
    def getExpValue (self):
        return self.__expValue
    def getGoldValue (self):
        return self.__goldValue
    def getEnemyStats (self):
        enemyStats = ["ID:" + self.__ID, "Name:" + self.__name, "Level:" + self.__level, "Health:" + self.__health, "Total Health:" + self.__totalHealth, "Strength:" + self.__strength, "EXP Value:" + self.__expValue, "Gold Value:" + self.__goldValue]
        return enemyStats

#Methods to display specific class information for the user
    def displayName (self):
        print ("Enemy's Name: " + self.__name)
    def displayLevel (self):
        print (self.__name + "'s " + "Level: " + self.__level)
    def displayHealth (self):
        print (self.__name + "'s " + "Health " + self.__health)
    def displayTotalHealth (self):
        print (self.__name + "'s " + "Total Health " + self.__totalHealth)
    def displayStrength (self):
        print (self.__name + "'s " + "Strength: " + self.__strength)
    def displayExpValue (self):
        print (self.__name + " is worth " + self.__expValue + " experience.")
    def displayGoldValue (self):
        print (self.__name + " has " + self.__goldValue + " gold.")

#Methods to change stats
    def changeTotalHealth(self, healthUpgrade):
        self.__totalHealth = self.__totalHealth + healthChange
        self.__health = self.__totalHealth
        
    def damage(self, damage):
        self.__health = self.__health - damage
        

#Print methods
    def __str__ (self):
        
        return self.__name
        #return str(self.__name) + "," + str(self.__level) + "," + str(self.__health) + "," + str(self.__totalHealth) + "," + str(self.__strength)

    def __repr__ (self):
        
        return self.__name
        #return str(self.__name) + "," + str(self.__level) + "," + str(self.__health) + "," + str(self.__totalHealth) + "," + str(self.__strength)
