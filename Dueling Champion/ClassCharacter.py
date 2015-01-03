import random

#HERO CLASS
class Hero(object):
    def __init__ (self, heroInitList):
        #all variables are stored as strings
        self.__name = heroInitList[0]
        self.__level = int(heroInitList[1])
        self.__health = int(heroInitList[2])
        self.__totalHealth = int(heroInitList[2])
        self.__strength = int(heroInitList[3])
        self.__exp = 0
        
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
        return str(self.__health) + "/" + str(self.__totalHealth)   
    def getStrength (self):
        return self.__strength
    def getHeroStats (self):
            heroStats = ["Name:" + self.__name, "Level:" + str(self.__level), "Health:" + str(self.__health), "Total Health:" + str(self.__totalHealth), "Strength:" + str(self.__strength)]
            return heroStats   

#Methods to display specific class information for the user
    def displayName (self):
        print ("Your Name is " + str(self.__name))
    def displayLevel (self):
        print ("You are level " + str(self.__level))
    def displayHealth (self):
        print ("You currently have " + str(self.__health) + " out of " + str(self.__totalHealth) + " health")
    def displayTotalHealth (self):
        print ("Your maximum health is " + str(self.__totalHealth))
    def displayStrength (self):
        print ("Your strength is " + str(self.__strength))

#Methods to change stats
    def levelUp(self):
        self.__level += 1
        
    def changeTotalHealth(self, healthUpgrade):
        self.__totalHealth = self.__totalHealth + healthChange
        self.__health = self.__totalHealth
    
    def damage(self, damage):
        self.__health = self.__health - damage
        
    def heal(self, heal):
        if self.__health == self.__totalHealth:
            print(self.__name + "'s health is full.")
        self.__health = self.__health + heal
        if self.__health > self.__totalHealth:
            self.__health = self.__totalHealth
            



#ENEMY CLASS
class Enemy(object):
    #Enemy constructor    
    def __init__ (self, statLine):
        #all variables are stored as strings
        self.__ID = statLine[0]
        self.__name = statLine[1]
        self.__level = int(statLine[2])
        self.__health = int(statLine[3])
        self.__totalHealth = int(statLine[3])
        self.__strength = int(statLine[4])
        self.__expValue = int(self.__level * 10)

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
        return str(self.__health) + "/" + str(self.__totalHealth)
    def getStrength (self):
        return self.__strength
    def getExpValue (self):
        return self.__expValue
    def getGoldValue (self):
        return self.__goldValue
    def getEnemyStats (self):
        enemyStats = ["ID:" + self.__ID, "Name:" + self.__name, "Level:" + str(self.__level), "Health:" + self.__health, "Total Health:" + self.__totalHealth, "Strength:" + self.__strength, "EXP Value:" + self.__expValue, "Gold Value:" + self.__goldValue]
        return enemyStats

#Methods to display specific class information for the user
    def displayName (self):
        print ("Enemy's Name: " + self.__name)
    def displayLevel (self):
        print (self.__name + "'s " + "Level: " + str(self.__level))
    def displayHealth (self):
        print (self.__name + "'s " + "Health " + str(self.__health))
    def displayTotalHealth (self):
        print (self.__name + "'s " + "Total Health " + str(self.__totalHealth))
    def displayStrength (self):
        print (self.__name + "'s " + "Strength: " + str(self.__strength))
    def displayExpValue (self):
        print (self.__name + " is worth " + str(self.__expValue) + " experience.")
    def displayGoldValue (self):
        print (self.__name + " has " + str(self.__goldValue) + " gold.")

#Methods to change stats
    def changeTotalHealth(self, healthUpgrade):
        self.__totalHealth = str(self.__totalHealth) + str(healthChange)
        self.__health = str(self.__totalHealth)
        
    def damage(self, damage):
        self.__health = self.__health - damage
        
    def heal(self, heal):
        if self.__health == self.__totalHealth:
            print(self.__name + "'s health is full.")
        else:
            self.__health = self.__health + heal
            if self.__health > self.__totalHealth:
                self.__health = self.__totalHealth

#Print methods
    def __str__ (self):
        
        return self.__name
        #return str(self.__name) + "," + str(self.__level) + "," + str(self.__health) + "," + str(self.__totalHealth) + "," + str(self.__strength)

    def __repr__ (self):
        
        return self.__name
        #return str(self.__name) + "," + str(self.__level) + "," + str(self.__health) + "," + str(self.__totalHealth) + "," + str(self.__strength)
