import time
import sys

mage = 0
warrior = 0
hunter = 0
rogue = 0
hp = 0
mp = 0
dmg = 0
spell  = 0
#Unique
rage = 0
energy = 0
shadow = 0
pet = 0

atk_dmg = 5
spell_dmg = 10
special_rogue = 20
goblin_hp = 5
goblin_dmg = 1 

def slowPrint(string, speed=0.05):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

def welcome():
    world_of_suton = "Welcome to the World of Suton! What is your name... "
    slowPrint(world_of_suton, 0.1)
    name = input("")
    slowPrint("Hello ", 0.1)
    slowPrint(name , 0.1)
    slowPrint(" pick your Class...", 0.1)
    print("")
    slowPrint(' 1) Warrior', 0.1)
    slowPrint(' 2) Mage', 0.1)
    slowPrint(' 3) Hunter', 0.1)
    slowPrint(' 4) Rogue', 0.1)#/n
    print("")
    class_choice()

def add_stats(classs):
    if classs == "1": #overall stats von 15
        hp += 10
        mp += 5 #Sinister Strike
        dmg += 5 #Normal attack
        spell += 7 #Sinister Strike
        energy += 100 #Stealth
        slowPrint("Stats: \n", 0.1)
    elif classs == "2": 
        hp += 10
        mp += 5
        dmg += 7
        spell += 5
        rage += 100
        slowPrint("Stats: \n", 0.1)
    elif classs == "3":
        hp += 10
        mp += 10
        dmg += 1
        spell += 10
        shadow += 100
        slowPrint("Stats: \n", 0.1)
    elif classs == "4":
        hp += 10
        mp += 5
        dmg += 10
        spell += 6
        pet += 100
        slowPrint("Stats: \n", 0.1)

def class_choice():
    print(("Pick Your Class 1-4:  "))
    classs = input("")
    if classs == "1":
        slowPrint("You are a Warrior now!\n ", 0.1)
        
    elif classs == "2":
        slowPrint("You are a Mage now! \n", 0.1) 
        
    elif classs == "3":
        slowPrint("You are a Hunter now! \n", 0.1) 

    elif classs == "4":
        slowPrint("You are a Rogue now!\n", 0.1) #fav class

    add_stats(classs)
    stats_print(classs)
    
def stats_print(classs):
    print("HP:", hp)
    print("MP:", mp)
    print("DMG:", dmg)
    print("SPELL:", spell)
    if classs == 1:
        print(f"ENERGY: {energy}")
        
    elif classs == 2:
        print(f"RAGE: {rage}")

    elif classs == 3:
        print(f"SHADOW: {shadow}")

    elif classs == 4:
        print(f"PET: {pet}")
    print("")


start = input("Start a New Game? 'Y' 'N':  ")
if start == "Y":
    slowPrint("Lets Go. ", 0.1)
else:
    exit()
welcome()


    
slowPrint("Now that you picked your Class lets go ahead and pick our first Quest! \n", 0.1)
slowPrint("There are 3 beginner Quests...\n", 0.1)

print('1: Goblin Cave *')
print('2: Rescue PITT *')
print('3: Find Ony *')
quest_1= input("Pick Your Quest 1-3:  ")
if quest_1 == "1":
    slowPrint("You picked Goblin Cave...\n", 0.1)
    slowPrint("You are traveling to Goblin Cave... \n", 0.1)
    slowPrint("Do you want to enter the Cave? \n", 0.1)
    decision_1 = input("Y or N: ")
    if decision_1 == "Y":
        slowPrint("Good Choice you are walking towards the Entrance...\n", 0.1)
    elif decision_1 == "N":
        print("You are traveling back to the Guild...")
    else:
        exit()
    if decision_1 == "Y":
        slowPrint("You entered the Cave, there are 3 paths in front of you...\n", 0.1)
        slowPrint("Choose one path...\n", 0.1)
        print('1: Left')
        print('2: Middle')
        print('3: Right')
        path = input("Pick: 1, 2 or 3: ")
        if path == "1":
            print("You picked Path 1...")
            print("While you are walking you feel a fearful presence...")
            print("There is a Goblin in font of you...")
            print("What are you going to do?")
            print('1: Fight ')
            print('2: Run ')
            choice = input("1 or 2: ")
            if choice == "1":
                print("[COMBAT MENU]")
                print('1: Attack ')
                print('2: Sinister Strike ')
                print('3: Stealth ')
                combat = input("1, 2 or 3: ")
                if combat == "1":
                    print("You attacked the Goblin...")
                    if dmg >= goblin_hp:
                        print("You killed the Goblin u did ", atk_dmg , "Damage!") 
                elif combat == "2":
                    print("You stabbed the Goblin with Sinister Strike...")
                    if spell_dmg >= goblin_hp:
                        print("You killed the Goblin u did", spell_dmg, "Damage! ")
                elif combat == "3":
                    print("You went invisibel and stabbed the Goblin...")
                    if special_rogue >= goblin_hp:
                        print("You killed the Goblin u did ", special_rogue, "Damage! ")
        print("After fighting the Goblin you feel confident you are walking deeper into the Cave... ")
        print("There is something bigger than a Goblin... ")
        print("There is a Ogre running towards you! ")
        print("What are you going to do? ")
        print('1: Fight ')
        print('2: Run ')
        choice = input("1 or 2: ")

