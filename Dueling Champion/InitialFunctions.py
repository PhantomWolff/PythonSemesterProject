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

def start_battle (hero, opponent):
    print("Let the battle between " + hero.getName() + " and " + opponent.getName() + " begin!")
    display_battle_table (hero, opponent)
    in_battle (hero, opponent)
    
def in_battle (hero, opponent):
    inFight = True
    while inFight == True:
        heroMove = input("\nMake your move: ")
        heroHealthBefore = hero.getHealth()
        opponentHealthBefore = opponent.getHealth()    
        if heroMove == "attack" or heroMove == "a":
            hero_attack(hero, opponent)
        elif heroMove == "block" or heroMove == "b":
            hero_block(hero, opponent)
        elif heroMove == "counter" or heroMove == "c":
            hero_counter(hero, opponent)
        elif heroMove == "dodge" or heroMove == "d":
            hero_dodge(hero, opponent)
        elif heroMove == "stats" or heroMove == "s":
            display_battle_table(hero, opponent)
        elif heroMove == "end":
            inFight = False
        else:
            print("Not a valid move. Try again.")
            
        #After move
        heroHealthAfter = hero.getHealth()
        opponentHealthAfter = opponent.getHealth()
       
       
#~~~~~~~~This will need to be removed and added in the moves section~~~~#

#These if/elses show if the opponent was hurt or healed.
        if opponentHealthBefore != opponentHealthAfter:
            #if opponentHealthBefore > opponentHealthAfter:
                #print("You dealt " + str(opponentHealthBefore - opponentHealthAfter) + " damage to " + opponent.getName())
            #else:
                #print(opponent.getName() + " healed, gaining " + str(opponentHealthAfter - opponentHealthBefore) + " health.")
            if opponent.getHealth() < 1:
                pass
            else:
                print(opponent.getName() + " now has " + opponent.getHealthFraction() + " health.")
        #This if statement will stop the loop if the enemy took lethal damage.
        if opponent.getHealth() < 1:
            inFight = False
            print(opponent.getName() + " has been defeated. Good work.")
            continue
        #These if/elses show if the hero was hurt or healed.
        if heroHealthBefore != heroHealthAfter:     
            
            ###what if they blocked, were dealt damage, and healed for the same amount of damage?
            #if heroHealthBefore > heroHealthAfter:
                #print(opponent.getName() + " dealt " + str(heroHealthBefore - heroHealthAfter) + " damage to you.")
            #else:
                #print("You healed, gaining " + str(heroHealthAfter - heroHealthBefore) + " health.")
            print("You now have " + hero.getHealthFraction() + " health.")              
            
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#



def display_battle_table (hero, opponent):
    #Working, but additions will be made.
    print("*" * 42)
    print("|{:<9s}{:>9s} | {:<9s}{:>9s} |".format("Name:", hero.getName(), "Name:", opponent.getName()))
    print("|{:<9s}{:>9s} | {:<9s}{:>9s} |".format("Level:", str(hero.getLevel()), "Level:", str(opponent.getLevel())))
    print("|{:<9s}{:>9s} | {:<9s}{:>9s} |".format("Strength:", str(hero.getStrength()), "Strength:", str(opponent.getStrength())))
    print("|{:<9s}{:>9s} | {:<9s}{:>9s} |".format("Health:", hero.getHealthFraction(), "Health:", opponent.getHealthFraction()))
    print("*" * 42)
    print("| {} | {} | {} | {} | {} |".format("attack(a)", "block(b)", "counter(c)", "dodge(d)", "stats(s)"))
    
    
"""the four hero moves"""
def hero_attack (hero, opponent):
    opponent_move(hero, opponent, "attack")
    
def hero_block (hero, opponent):
    opponent_move(hero, opponent, "block")
    
def hero_counter (hero, opponent):
    opponent_move(hero, opponent, "counter")

def hero_dodge (hero, opponent):
    opponent_move(hero, opponent, "dodge")


"""the four opponent moves"""
def opponent_move(hero, opponent, heroMove):
    opponentMove = random.choice(["attack","block","counter","dodge"])
    if heroMove == "attack":
        opponent_attack(hero, opponent, opponentMove)
    if heroMove == "block":
        opponent_block(hero, opponent, opponentMove)
    if heroMove == "counter":
        opponent_counter(hero, opponent, opponentMove)
    if heroMove == "dodge":
        opponent_dodge(hero, opponent, opponentMove)

#What will the opponent do if the hero attacks
def opponent_attack(hero, opponent, opponentMove):      
    if opponentMove == "attack":                        #Good
        #print(1)
        damage = hero.getStrength()
        opponent.damage(damage)             #opponent is damaged
        print("You dealt " + str(damage) + " damage to " + opponent.getName())
        if opponent.getHealth() < 1:
            pass
        
        else:
            #print(2)
            print(opponent.getName() + " attacked")
            damage = opponent.getStrength()
            hero.damage(damage)             #hero is damaged
            print(opponent.getName() + " dealt " + str(damage) + " damage to you.")
            if hero.getHealth() < 1:
                print("hero has been defeated")
            else:
                pass
            
    if opponentMove == "block":                         #What if damage equals heal?
        #print(3)
        damage = round(hero.getStrength() * 1/4)
        opponent.damage(damage)             #opponent is damaged
        if damage == 0:
            print(opponent.getName() + " completely blocked your attack")
        elif opponent.getHealth() < 1:
            pass
        else:
            print(opponent.getName() + " blocked part of your attack")
            print("You dealt " + str(damage) + " damage to " + opponent.getName())
            heal = round(opponent.getTotalHealth() * 1/6)
            opponent.heal(heal)             #opponent is healed
            print(opponent.getName() + " healed, gaining " + str(heal) + " health.")

    if opponentMove == "counter":           #Good
        #print(4)
        damage = round(hero.getStrength() * (1/3))
        opponent.damage(damage)             #opponent is damaged
        if damage == 0:
            print(opponent.getName() + " completely countered your attack")
        elif opponent.getHealth() < 1:
            print("You dealt " + str(damage) + " damage to " + opponent.getName())
        else:
            #print(5)
            print("You dealt " + str(damage) + " damage to " + opponent.getName())
            print(opponent.getName() + " countered your attack")
            damage = round(hero.getStrength() * (2/3))
            hero.damage(damage)             #hero is damaged
            
            print(opponent.getName() + " dealt " + str(damage) + " damage to you.")
    if opponentMove == "dodge":
        #print(6)
        dodgeVar = random.random()
        if dodgeVar <= .75:
            print(opponent.getName() + " dodged your attack")
        else:
            #print(7)
            print("opponent attempted to dodge, but failed")
            damage = hero.getStrength()
            opponent.damage(damage)
            print("You dealt " + str(damage) + " damage to " + opponent.getName())

#What will the opponent do if the hero blocks
def opponent_attack(hero, opponent, opponentMove):      
    if opponentMove == "attack":                        #Good
        #print(2)
        print(opponent.getName() + " attacked")
        damage = opponent.getStrength()
        hero.damage(damage)             #hero is damaged
        print(opponent.getName() + " dealt " + str(damage) + " damage to you.")
        if hero.getHealth() < 1:
            print("hero has been defeated")
        else:
            pass
            

    if opponentMove == "block":
        print(opponent.getName() + " blocked")
        damage = round(hero.getStrength() * 1/6)
        
    if opponentMove == "counter":
        print(opponent.getName() + " countered")
        damage = round(hero.getStrength() * (1/3))
        opponent.damage(damage)
        damage = round(hero.getStrength() * (2/3))
        hero.damage(damage)
    if opponentMove == "dodge":
        
        dodgeVar = random.random()
        if dodgeVar <= .75:
            print(opponent.getName() + " dodged")
        else:
            "opponent attampted to dodge, but failed"
            damage = hero.getStrength()
            opponent.damage(damage)       

#What will the opponent do if the hero counters    
def opponent_counter(hero, opponent, opponentMove):
    if opponentMove == "attack":
        print(opponent.getName() + " attacked")
        damage = hero.getStrength()
        opponent.damage(damage)
        if opponent.getHealth() < 1:
            pass
        else:
            damage = opponent.getStrength()
            hero.damage(damage)
            if hero.getHealth() < 1:
                print("hero has been defeated")
            else:
                pass
            
    if opponentMove == "block":
        print(opponent.getName() + " blocked")
        damage = round(hero.getStrength() * 1/6)
        
    if opponentMove == "counter":
        print(opponent.getName() + " countered")
        damage = round(hero.getStrength() * (1/3))
        opponent.damage(damage)
        damage = round(hero.getStrength() * (2/3))
        hero.damage(damage)
    if opponentMove == "dodge":
        
        dodgeVar = random.random()
        if dodgeVar <= .75:
            print(opponent.getName() + " dodged")
        else:
            "opponent attampted to dodge, but failed"
            damage = hero.getStrength()
            opponent.damage(damage)       

#What will the opponent do if the hero dodges    
def opponent_dodge(hero, opponent, opponentMove):
    if opponentMove == "attack":
        print(opponent.getName() + " attacked")
        damage = hero.getStrength()
        opponent.damage(damage)
        if opponent.getHealth() < 1:
            pass
        else:
            damage = opponent.getStrength()
            hero.damage(damage)
            if hero.getHealth() < 1:
                print("hero has been defeated")
            else:
                pass
            
    if opponentMove == "block":
        print(opponent.getName() + " blocked")
        damage = round(hero.getStrength() * 1/6)
        
    if opponentMove == "counter":
        print(opponent.getName() + " countered")
        damage = round(hero.getStrength() * (1/3))
        opponent.damage(damage)
        damage = round(hero.getStrength() * (2/3))
        hero.damage(damage)
    if opponentMove == "dodge":
        
        dodgeVar = random.random()
        if dodgeVar <= .75:
            print(opponent.getName() + " dodged")
        else:
            "opponent attampted to dodge, but failed"
            damage = hero.getStrength()
            opponent.damage(damage)       
            
    
"""menu functions"""
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
    
    selection = input("\nType your selection: ")
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
        confirm = input("\nAre you sure you want to exit? (yes/no): ").lower()
        while True:
            if confirm == "yes":
                print("Thanks for playing!")
                sys.exit()
            elif confirm == "no":
                break
            else:
                confirm = input("\nPlease type 'yes' or 'no'")
                
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

####################################################################


########Functions for a specific time/single use in the game########

#Creates the hero object. Should be one of the first things the user sees.
def create_hero () -> object:
    #Incomplete but working
    heroName = ""
    while heroName == "":   #Makes sure hero isn't blank
        heroName = input("\nGreetings, adventurer! What is your name? ")
    #heroLevel = input("What is your starting level? ")
    heroLevel = 1
    #heroTotalHealth = input("What is your starting health? ")
    heroTotalHealth = 15
    #heroStrength = input("What is your starting strength? ")
    heroStrength = 4
    heroInitList = [heroName, heroLevel, heroTotalHealth, heroStrength]
    hero = Hero(heroInitList)
    print("It is a pleasure to meet you, " + hero.getName())
    return hero

####################################################################


##################MAIN#####################
#Conditional boolean things
inFight = False

print( '\n\n\n\n¸,ø¤º°`°º¤ø,¸ ďµ€ℓɨɲǥ ȼhąʍρɨ๏ɲ ¸,ø¤º°`°º¤ø,¸')
input("(Enter to begin)")

#Instantiate characters    
enemyDict = create_enemy_dictionary()
hero = create_hero()

enemyNumber = 0

#Changes an enemy number to the current opponent
opponent = enemyDict["enemy" + str(enemyNumber)]

print(opponent.getName() + " will be your first enemy.")
userInput = input("(Press Enter)")
check_keywords(userInput)
start_battle(hero, opponent)

        
print("End of program")

