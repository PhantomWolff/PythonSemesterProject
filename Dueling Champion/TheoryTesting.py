#i = 1
#d = {"chair": "arm"}
#print (d["chair"])
#d = {"so" + "fa": "cushion"}
#print (d["sofa"])
#d["enemy" + str(i)] = "bowser"
#print (d["enemy1"])
#print (d)



#i = 1
#k = 2
##I want to assign enemy1 to bowser and enemy2 to bowser junior WITHOUT typing the values 1 or 2
#list1 = ["enemy" + str(1), "enemy2"]
#print (list1)

class Test(object):
    def __init__ (self, name = "", age = 0, color = ""):
        self.__name = name
        self.__age = age
        self.__color = color
    
    def getName (self):
        return self.__name
    
    def getAge (self):
        return self.__age
    
    def getColor (self):
        return self.__color
    
    def __str__ (self):
        return (str(self.__name) + str(self.__age) + str(self.__color))