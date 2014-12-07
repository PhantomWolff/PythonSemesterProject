class Character(object):

#Character constructor    
    def __init__ (self, statLine):
        self.__ID = statLine[0]
        self.__name = statLine[1]
        self.__level = statLine[2]
        self.__health = statLine[3]
        self.__totalHealth = statLine[3]
        self.__strength = statLine[4]

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
    def getStrength (self):
        return self.__strength
    
#Methods to change stats
    def changeTotalHealth(self, healthUpgrade):
        self.__totalHealth = self.__totalHealth + healthChange
        self.__health = self.__totalHealth
        
    def changeHealth(self, damage):
        self.__health = self.__health - damage
        

#Print methods
    def __str__ (self):
        
        return self.__name
        #return str(self.__name) + "," + str(self.__level) + "," + str(self.__health) + "," + str(self.__totalHealth) + "," + str(self.__strength)

    def __repr__ (self):
        
        return self.__name
        #return str(self.__name) + "," + str(self.__level) + "," + str(self.__health) + "," + str(self.__totalHealth) + "," + str(self.__strength)
