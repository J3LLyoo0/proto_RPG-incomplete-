from movement import good_moves, evil_moves
from MinionAndSummon import good_summon_moves,mythic_summon_moves,minion_moves
import minionstats
import damage
import random

class Good: 
    def __init__(self,name,health,attack_power): 
        self.name = name 
        self.health = health 
        self.attack_power = attack_power 
        
    def get_gcharacter(self): 
        return f"Name:{self.name}\n  Health:{self.health}\n  Attack Power:{self.attack_power}\n" 
    
character1 = Good("Hero",5500,350) 
character2 = Good("Priest",2500,200) 
character3 = Good("Knight",4000,380) 
character4 = Good("Mage",2000,400) 
character5 = Good("Archer",1500,380) 
character6 = Good("Assassin",1800,400) 
character7 = Good("Beast Master",2500,270) 

good_faction = [character1,character2,character3,character4,character5,character6,character7] 

class Evil: 
    def __init__(self,name,health,attack_power): 
        self.name = name 
        self.health = health 
        self.attack_power = attack_power 

    def get_echaracter(self): 
        return f"Name:{self.name}\n  Health:{self.health}\n  Attack Power:{self.attack_power}\n" 
        
character1 = Evil("Demon King",6000,450) 
character2 = Evil("Dark Knight",4500,410) 
character3 = Evil("Necromancer",2500,180) 
character4 = Evil("Dragon",8000,500) 
character5 = Evil("Dark Mage",2550,300) 

evil_faction = [character1,character2,character3,character4,character5] 

print("Select a faction to begin your adventure:\n") 
print("Good Faction\nEvil Faction") 
print("\nPress 1 for joining the Good Faction") 
print("Press 2 for joining the Evil Faction\n") 

faction_select = int(input()) 
print() 
l = 1 

if faction_select == 1: 
    print("You have choosen the Good Faction, please select a character\n") 

    for l,g in enumerate(good_faction,1): 
        print(l) 
        print(" ",g.get_gcharacter()) 
        
    choice = int(input()) 
    selected_character = good_faction[choice - 1] 
    print("\nYou selected:\n") 
    print (" ",selected_character.get_gcharacter()) 
        
    for m in good_moves [selected_character.name]: 
        print ("-",m) 
elif faction_select == 2: 
    print("You have choosen the Evil Faction, please select a character\n") 

    for l,e in enumerate(evil_faction,1): 
        print(l) 
        print(" ",e.get_echaracter()) 
        
    choice = int(input()) 
    selected_character = evil_faction[choice - 1] 
        
    print("\nYou selected:\n") 
    print(" ",selected_character.get_echaracter()) 
    for m in evil_moves [selected_character.name]: 
        print ("-",m) 
else: 
    print("Invalid Input")

"""
print("\nThis is the list of minions you will encounter during your adventure:\n")
for b,a in enumerate(minionstats.minions,1): 
        print(b)
        print(" ",a.get_minion())
"""

if selected_character.name == "Hero": 
    print("\nThis is the story of the Hero, one of the mightiest warriors in the land of Elaria...\nPress Enter to continue story")
    press = input()
    print("\nWe will follow the Hero and experience the journey along with the Hero's sight...\nPress Enter to continue story")
    press = input()

    print("\nYou have entered the forest of Eldoria, a place known for its mystical creatures and hidden dangers...\nPress Enter to continue story")
    press = input()

    while True:
        print("\nWhat will you do?\n")
        print("1. Explore the forest\n2. Set up camp and rest\n3. Exit Game\n")
        action = int(input())
        if action == 1:
            print("\nYou searched your surrounding...\n")

            search = ["Nothing","A wild Goblin appears!","A wild Orc appears","Found an Item"]
            weights = [0.3,0.4,0.2,0.1]
            result = random.choices(search,weights)
            print(result[0])

            if result[0] == "A wild Goblin appears!":
                goblin = minionstats.minion2
                print(f"\nYou are confronted by a {goblin.name}!\n")
                print("Prepare for battle!\n")

                while goblin.health > 0 and selected_character.health > 0:
                    print("What will you do?\n")
                    print("1. Action\n2. Use Item\n3. Rest\n4. Flee\n")
                    action = int(input("Choose:"))

                    if action == 1:
                        print("\nChoose Your Move:\n")
                        for l,m in enumerate(good_moves[selected_character.name],1):
                            print(l,m)

                        move = int(input("Move Number:"))
                        selected_move = good_moves[selected_character.name][move-1]

                        dmg,heal,tags = damage.calculate_damage(selected_character.attack_power,selected_character.health,selected_move)

                        if dmg > 0:
                            goblin.health -= dmg
                            print(f"\nYou used {selected_move} and dealt {dmg} damage to the {goblin.name}!\n")

                        if heal > 0:
                            selected_character.health += heal
                            print(f"\nYou used {selected_move} and healed yourself for {heal} health!\n")

                        if "Buff" in tags:
                            selected_character.attack_power = int(selected_character.attack_power*1.2)
                            print(f"\n{selected_character.name}'s attack power has increased!\n")

                        if "Debuff" in tags:
                            goblin.attack_power = int(goblin.attack_power*(0.8))
                            print(f"The {goblin.name}'s attack power has decreased!\n")

                        if goblin.health <= 0:
                            print(f"The {goblin.name} has been defeated!\n")

                    elif action == 2:
                        print("You are searching for an item in the inventory...(not yet implemented)\n")

                    elif action == 3:
                        print("You take a short moment to rest and recover some health...\n")
                        rest_heal = [200,250,300]
                        recover = random.choice(rest_heal)
                        selected_character.health += recover

                    elif action == 4:
                        print("You fled from the battle...\n")
                        print("What a coward!\n")
                        break

                    if goblin.health > 0:
                        goblin.move = random.choice(minion_moves[goblin.name])
                        dmg,heal,tags = damage.calculate_damage(goblin.attack_power,goblin.health,goblin.move)

                        if dmg > 0:
                            selected_character.health -= dmg
                            print(f"The {goblin.name} used {goblin.move} and dealt {dmg} damage to you!\n")

                        if heal >0:
                            goblin.health += heal
                            print(f"The {goblin.name} healed for {heal} HP!\n")

                        if "Buff" in tags:
                            goblin.attack_power = int(goblin.attack_power*1.2)
                            print(f"The {goblin.name} used {goblin.move} and its attack power has increased\n")

                        if "Debuff" in tags:
                            selected_character.attack_power = int(selected_character.attack_power *0.8)
                            print(f"The {goblin.name} used {goblin.move} and caused {selected_character.name}'s attack power to decrease!\n")

                        if selected_character.health <= 0:
                            print("\nYOU DIED\nGAME OVER\n")
                            exit()

                    print(f"\nYour Health: {selected_character.health} | Goblin's Health: {goblin.health}\n")

            elif result[0] == "A wild Orc appears":
                orc = minionstats.minion3
                print(f"\nYou are confronted by an {orc.name}!\n")
                print("Prepare for battle!\n")

                while orc.health > 0 and selected_character.health > 0:
                    print("What will you do?\n")
                    print("1. Action\n2. Use Item\n3. Rest\n4. Flee\n")
                    action = int(input("Choose:"))

                    if action == 1:
                        print("\nChoose Your Move:\n")
                        for l,m in enumerate(good_moves[selected_character.name],1):
                            print(l,m)

                        move = int(input("Move Number:"))
                        selected_move = good_moves[selected_character.name][move-1]

                        dmg,heal,tags = damage.calculate_damage(selected_character.attack_power,selected_character.health,selected_move)

                        if dmg > 0:
                            orc.health -= dmg
                            print(f"\nYou used {selected_move} and dealt {dmg} damage to the {orc.name}!\n")

                        if heal > 0:
                            selected_character.health += heal
                            print(f"\nYou used {selected_move} and healed yourself for {heal} health!\n")

                        if "Buff" in tags:
                            selected_character.attack_power = int(selected_character.attack_power*1.2)
                            print(f"\n{selected_character.name}'s attack power has increased!\n")

                        if "Debuff" in tags:
                            orc.attack_power = int(orc.attack_power*(0.8))
                            print(f"The {orc.name}'s attack power has decreased!\n")

                        if orc.health <= 0:
                            print(f"The {orc.name} has been defeated!\n")

                    elif action == 2:
                        print("You are searching for an item in the inventory...(not yet implemented)\n")

                    elif action == 3:
                        print("You take a short moment to rest and recover some health...\n")
                        rest_heal = [200,250,300]
                        recover = random.choice(rest_heal)
                        selected_character.health += recover

                    elif action == 4:
                        print("You fled from the battle...\n")
                        print("What a coward!\n")
                        break

                    if orc.health > 0:
                        orc.move = random.choice(minion_moves[orc.name])
                        dmg,heal,tags = damage.calculate_damage(orc.attack_power,orc.health,orc.move)

                        if dmg > 0:
                            selected_character.health -= dmg
                            print(f"The {orc.name} used {orc.move} and dealt {dmg} damage to you!\n")

                        if heal >0:
                            orc.health += heal
                            print(f"The {orc.name} healed for {heal} HP!\n")

                        if "Buff" in tags:
                            orc.attack_power = int(orc.attack_power*1.2)
                            print(f"The {orc.name} used {orc.move},its attack power has increased\n")

                        if "Debuff" in tags:
                            selected_character.attack_power = int(selected_character.attack_power *0.8)
                            print(f"The {orc.name} used {orc.move} and cause {selected_character.name}'s attack power to decrease!\n")

                        if selected_character.health <= 0:
                            print("\nYOU DIED\nGAME OVER\n")
                            exit()

                    print(f"\nYour Health: {selected_character.health} | Orc's Health: {orc.health}\n")

            elif result[0] == "Found an Item":
                items = ["Health Potion","Mana Potion","Sword of Valor","Shield of Light"]
                found_item = random.choice(items)
                print(f"\nYou found a {found_item}!\n")

            elif result[0] == "Nothing":
                print("\nYou found nothing of interest.\n")

        elif action == 2:
            print("\nYou decide to take a break on your journey...\nPress Enter to Continue")
            press = input()
            print("\nYou set up tha camp and rest for a while...\n")

            rest_heal = [1000,1500,2000]
            recover = random.choice(rest_heal)
            selected_character.health += recover

            dialog = ["You feel rejuvenated and ready to continue your adventure!\n",
                    "The warmth of the campfire soothes your weary soul.\n",
                    "You reflect on your journey so far and feel a sense of purpose.\n",
                    "The sounds of the forest lull you into a peaceful sleep.\n",
                    "You cooked a meal and ate it, it was delicious.\n",
                    "You felt a breeze blow past you, you feel refreshed.\n"]
            display = random.choice(dialog)
            print(f"{display}\nYou recovered {recover} HP!\n")

        elif action == 3:
            print("\nYou have exited the game.\n")
            print("Thank you for playing!\n")
            exit()
        