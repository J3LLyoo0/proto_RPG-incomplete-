"""
def calculate_damage1(attack_power,health, move):
    if move == "Slash":
        return attack_power
    elif move == "Shield Bash":
        return attack_power * 0.8
    elif move == "Divine Judgemet":
        return attack_power * 1.2
    elif move == "Inspire":
        return 0  # Inspire is a buff, no damage
    elif move == "Last Stand":
        return attack_power * 1.5
    elif move == "Rest":
        return (0, health+300,"Heal")  # Rest is a healing action, no damage
    else:
        return 0  # Default case for unrecognized moves

def calculate_damage2(attack_power,health, move):
    if move == "Heal":
        return -(health + 250)  # Heal is a healing action, no damage
    elif move == "Barrier":
        return 0  # Barrier is a defensive action, no damage
    elif move == "Judgement":
        return attack_power * 1.1
    elif move == "Purify":
        return 0  # Purify is a cleansing action, no damage
    elif move == "Rest":
        return -(health + 200)  # Rest is a healing action, no damage
    else:
        return 0  # Default case for unrecognized moves

def calculate_damage3(attack_power,health, move):
    if move == "Holy Slash":
        return attack_power * 1.0
    elif move == "Taunt":
        return 0  # Taunt is a defensive action, no damage
    elif move == "Piercing Strike":
        return attack_power * 1.3
    elif move == "Iron Will":
        return 0  # Iron Will is a buff, no damage
    elif move == "Sanctuary":
        return 0  # Sanctuary is a healing action, no damage
    elif move == "Light's Protection":
        return 0  # Light's Protection is a defensive action, no damage
    elif move == "Rest":
        return -(health + 330)  # Rest is a healing action, no damage
    else:
        return 0  # Default case for unrecognized moves

def calculate_damage4(attack_power,health, move):
    if move == "Wrath of Hephaestus":
        return attack_power * 1.4
    elif move == "Ice Spear":
        return attack_power * 1.2
    elif move == "Earth Bound":
        return attack_power * 1.1
    elif move == "Protection of Gaia":
        return 0  # Protection of Gaia is a defensive action, no damage
    elif move == "Athena's Blessing":
        return 0  # Athena's Blessing is a buff, no damage
    elif move == "Rest":
        return -(health + 200)  # Rest is a healing action, no damage
    else:
        return 0  # Default case for unrecognized moves

def calculate_damage5(attack_power,health, move):
    if move == "Shoot Arrow":
        return attack_power * 1.0
    elif move == "Multi Shot":
        return attack_power * 0.9 * 3  # Hits 3 times
    elif move == "Take Aim":
        return attack_power * 1.5
    elif move == "High Alert":
        return 0  # High Alert is a buff, no damage
    elif move == "Explosive Arrow":
        return attack_power * 1.3
    elif move == "Arrow of Artemis (Ultimate)":
        return attack_power * 2.0
    elif move == "Rest":
        return -(health + 250)  # Rest is a healing action, no damage
    else:
        return 0  # Default case for unrecognized moves

def calculate_damage6(attack_power,health, move):
    if move == "Backstab":
        return attack_power * 1.5
    elif move == "Sneak Attack":
        return attack_power * 1.2
    elif move == "Poisoned Blade":
        return attack_power * 1.1
    elif move == "Shadow Step":
        return 0  # Shadow Step is a movement action, no damage
    elif move == "Evasion":
        return 0  # Evasion is a defensive action, no damage
    elif move == "Rest":
        return -(health + 280)  # Rest is a healing action, no damage
    else:
        return 0  # Default case for unrecognized moves

def calculate_damage7(attack_power,health, move):
    if move == "Summon":
        return 0  # Summon is a summoning action, no damage
    elif move == "Call of the Wild":
        return 0  # Call of the Wild is a buff, no damage
    elif move == "Attack":
        return attack_power * 1.0
    elif move == "Defend":
        return 0  # Defend is a defensive action, no damage
    elif move == "Buff":
        return 0  # Buff is a buff action, no damage
    elif move == "Debuff":
        return 0  # Debuff is a debuff action, no damage
    elif move == "Mythic Summoning(Ultimate)":
        return 0  # Mythic Summoning is a summoning action, no damage
    elif move == "Rest":
        return -(health+220)  # Rest is a healing action, no damage
    else:
        return 0  # Default case for unrecognized moves

def calculate_damage8(attack_power,health, move):
    if move == "Slash":
        return attack_power * 1.0
    elif move == "Dracula's Touch":
        return attack_power * 1.3, -(health+150) # Deals damage and heals
    elif move == "Infernal Command":
        return attack_power * 1.2
    elif move == "Hellfire Nova":
        return attack_power * 1.5
    elif move == "Befall of Erebus(Ulti)":
        return attack_power * 2.0
    else:
        return 0  # Default case for unrecognized moves

def calculate_damage9(attack_power,health, move):
    if move == "Shadow Slash":
        return attack_power * 1.0
    elif move == "Crimson Strike":
        return attack_power * 1.2, -(health+100)  # Deals damage and heals
    elif move == "Shadowbound Chains":
        return attack_power * 1.1
    elif move == "Blood Pact":
        return 0  # Blood Pact is a buff, no damage
    elif move == "Master's Call":
        return 0  # Master's Call is a buff, no damage
    elif move == "Tyrant's Order":
        return 0  # Tyrant's Order is a buff, no damage
    elif move == "Dark Rally":
        return 0  # Dark Rally is a buff, no damage
    else:
        return 0  # Default case for unrecognized moves

def calculate_damage10(attack_power, move):
    if move == "Summon Skeleton":
        return 0  # Summon Skeleton is a summoning action, no damage
    elif move == "Summon Zombie":
        return 0  # Summon Zombie is a summoning action, no damage
    elif move == "Summon Ghoul":
        return 0  # Summon Ghoul is a summoning action, no damage
    elif move == "Curse of Weakness":
        return 0  # Curse of Weakness is a debuff, no damage
    elif move == "Curse of Frailty":
        return 0  # Curse of Frailty is a debuff, no damage
    elif move == "Curse of Silence":
        return 0  # Curse of Silence is a debuff, no damage
    elif move == "Plague Touch":
        return attack_power * 1.1
    elif move == "Bone Prison":
        return 0  # Bone Prison is a control action, no damage
    elif move == "Bone Armor":
        return 0  # Bone Armor is a defensive action, no damage
    elif move == "Mana Leech":
        return attack_power * 0.8
    elif move == "Sacrificial Pact":
        return attack_power * 1.5
    else:
        return 0  # Default case for unrecognized moves

def calculate_damage11(attack_power, move):
    if move == "Flame Burst":
        return attack_power * 1.3
    elif move == "Tail Smash":
        return attack_power * 1.2
    elif move == "Wing Buffet":
        return attack_power * 1.1
    elif move == "Dragon's Roar":
        return attack_power * 1.4
    elif move == "Infernal Flight":
        return 0  # Infernal Flight is a movement action, no damage
    elif move == "Eternal Scales":
        return 0  # Eternal Scales is a defensive action, no damage
    else:
        return 0  # Default case for unrecognized moves

def calculate_damage12(attack_power, move):
    if move == "Cataclysmic Void":
        return attack_power * 1.4
    elif move == "Nether Eclipse":
        return attack_power * 1.3
    elif move == "Soul Annihilation":
        return attack_power * 1.5
    elif move == "Forbidden Ascension":
        return 0  # Forbidden Ascension is a buff, no damage
    elif move == "Apocalypse Rain":
        return attack_power * 1.2
    elif move == "Phantom Shroud":
        return 0  # Phantom Shroud is a defensive action, no damage
    elif move == "WorldBreaker Hex (Ultimate)":
        return attack_power * 2.0
    else:
        return 0  # Default case for unrecognized moves


def calculate_minion_damage1(attack_power, move):
    if move == "Slash":
        return attack_power * 1.0

def calculate_minion_damage2(attack_power, move):
    if move == "Slash":
        return attack_power * 0.8
    elif move == "Goblin's Call":
        return attack_power * 1.1
    elif move == "Abominable Face":
        return attack_power * 1.2


def calculate_minion_damage3(attack_power, move):
    if move == "Crushing Blow":
        return attack_power * 1.3
    elif move == "Roar of Confidence":
        return 0  # Roar of Confidence is a buff, no damage


def calculate_minion_damage4(attack_power, move):
    if move == "Scratch":
        return attack_power * 0.9
    elif move == "Bite":
        return attack_power * 1.1
    elif move == "Growl":
        return 0  # Growl is a debuff, no damage


def calculate_minion_damage5(attack_power, move):
    if move == "Putrid Claw":
        return attack_power * 1.0
    elif move == "Corrupting Bite":
        return attack_power * 1.2
    elif move == "Grave Howl":
        return 0  # Grave Howl is a debuff, no damage
    elif move == "Soul Siphon":
        return attack_power * 1.3, -(100)  # Deals damage and heals


def calculate_minion_damage6(attack_power, move):
    if move == "Iron Phalanx":
        return 0  # Iron Phalanx is a defensive action, no damage
    elif move == "Spear Thrust":
        return attack_power * 1.2
    elif move == "Shield Bash":
        return attack_power * 0.8
    elif move == "Fotress Stance":
        return 0  # Fotress Stance is a defensive action, no damage
"""

"""
def calculate_damage(character,attack_power,health,move):
    if character == "Hero":
        if move == "Slash":
            return (attack_power,0,["Physical"])
        elif move == "Shield Bash":
            return (attack_power * 0.8, 0, ["Physical"])
        elif move == "Divine Judgement":
            return (attack_power *1.2, 0, ["Holy"])
        elif move =="Inspire":
            return (0,0,["Buff"]) #this skill is a buff to increase attack power
        elif move == "Last Stand":
            return (0,0,["Health Lock"])#this is a skill to force the hero to stay alive with 1 health if the hero would die
        elif move == "Rest":
            return (0, 300,["Heal"])

    elif character == "Priest":
        if move == "Heal":
            return(0, 250, ["Heal"])#this skill is to heal the priest or an ally
        elif move == "Barrier":
            return(0,0,["Shield"]) #this skill is to shield the priest or an ally from damage
        elif move == "Judgement":
            return(attack_power * 2,0,["Holy"])
        elif move =="Purify":
            return(0,0,["Cleanse"]) #this skill is to cleanse the priest or an ally from debuffs
        elif move =="Rest":
            return(0, 200, ["Heal"])

    elif character == "Knight":
        if move == "Holy Slash":
            return (attack_power * 1.1,0,["Holy"])
        elif move == "Taunt":
            return (0,0,["Taunt"]) #this skill is to force the enemy to attack the knight
        elif move == "Piercing Strike":
            return (attack_power * 1.3,0,["Physical"])
        elif move == "Iron Will":
            return (0,0,["Buff"]) #this skill is a buff to increase defense
        elif move == "Sanctuary":
            return (0, 300,["Heal"])
        elif move == "Light's Protection":
            return (0,0,["Shield"]) #this skill is to shield the knight or an ally from damage
        elif move == "Rest":
            return (0, 330,["Heal"])

    elif character =="Mage":
        if move == "Wrath of Hephaestus":
            return (attack_power * 1.4,0,["Fire"])
        elif move =="Ice Spear":
            return (attack_power * 1.2,0,["Ice"])
        elif move =="Earth Bound":
            return (attack_power * 1.1,0,["Earth"])
        elif move =="Protection of Gaia":
            return (0,0,["Shield"]) #this skill is to shield the mage or an ally from damage
        elif move =="Athena's Blessing":
            return (0,0,["Buff"]) #this skill is a buff to increase attack power and defense
        elif move =="Rest":
            return (0, 200,["Heal"])

    elif character == "Archer":
        if move == "Shoot Arrow":
            return (attack_power,0,["Physical"])
        elif move == "Multi Shot":
            return (attack_power * 0.9 * 3,0,["Physical"]) #hits 3 times
        elif move == "Take Aim":
            return (0,0,["Buff"])#increse hit chance and critical chance
        elif move == "High Alert":
            return (0,0,["Buff","Awareness"]) #this skill is a buff to decrease enemy hit chance
        elif move == "Explosive Arrow":
            return (attack_power * 1.5,0,["Fire"])
        elif move == "Arrow of Artemis (Ultimate)":
            return (attack_power * 2.0,0,["Physical"])
        elif move == "Rest":
            return (0, 250,["Heal"])

    elif character == "Assassin":
        if move == "Backstab":
            return (attack_power * 1.5,0,["Physical"])
        elif move == "Sneak Attack":
            return (attack_power * 1.2,0,["Physical"])
        elif move == "Poisoned Blade":
            return (attack_power * 1.1,0,["Poison"])
        elif move == "Shadow Step":
            return (0,0,["Evade"]) #this skill is to evade the next enemy attack
        elif move == "Evasion":
            return (0,0,["Buff"]) #this skill is a buff to increase evasion chance
        elif move == "Rest":
            return (0, 280,["Heal"])

    elif character == "Beast Master":
        if move == "Summon":
            return (0,0,["Summon"]) #this skill is to summon a minion to fight alongside the beast master
        elif move == "Call of the Wild":
            return (0,0,["Buff"]) #this skill is a buff to increase minion attack power and defense
        elif move == "Attack":
            return (attack_power,0,["Physical"])
        elif move == "Defend":
            return (0,0,["Shield"]) #this skill is to shield the beast master or an ally from damage
        elif move == "Buff":
            return (0,0,["Buff"]) #this skill is a buff to increase attack power and defense
        elif move == "Debuff":
            return (0,0,["Debuff"]) #this skill is a debuff to decrease enemy attack power and defense
        elif move == "Mythic Summoning(Ultimate)":
            return (0,0,["Summon"]) #this skill is to summon a mythic minion to fight alongside the beast master
        elif move == "Rest":
            return (0, 220,["Heal"])

    elif character == "Demon King":
        if move =="Slash":
            return (attack_power,0,["Physical"])
        elif move =="Dracula's Touch":
            return (attack_power * 1.3, 150, ["Physical", "Heal"]) #this skill deals damage and heals the demon king
        elif move == "Infernal Command":
            return (attack_power * 1.2,0,["Fire"])
        elif move == "Hellfire Nova":
            return (attack_power * 1.5,0,["Fire", "Dark"])
        elif move == "Befall of Erebus(Ulti)":
            return (attack_power * 2.0,0,["Dark"])

    elif character == "Dark Knight":
        if move == "Shadow Slash":
            return (attack_power+(attack_power*0.2),0,["Physical", "Dark"])
        elif move == "Crimson Strike":
            return (attack_power * 1.2, 100, ["Physical","Heal"]) #this skill deals damage and heals the dark knight
        elif move == "Shadowbound Chains":
            return (attack_power * 1.1,0,["Dark"])
        elif move == "Blood Pact":
            return (0,0,["Buff"]) #this skill is a buff to increase attack power and defense
        elif move == "Master's Call":
            return (0,0,["Buff"]) #this skill is a buff to increase minion attack power and defense
        elif move == "Tyrant's Order":
            return (0,0,["Buff"]) #this skill is a buff to increase enemy hit chance
        elif move == "Dark Rally":
            return (0,0,["Buff"]) #this skill is a buff to increase attack power and defense

    elif character == "Necromancer":
        if move == "Summon Skeleton":
            return (0,0,["Summon"]) #this skill is to summon a skeleton minion to fight alongside the necromancer
        elif move == "Summon Zombie":
            return (0,0,["Summon"]) #this skill is to summon a zombie minion to fight alongside the necromancer
        elif move == "Summon Ghoul":
            return (0,0,["Summon"]) #this skill is to summon a ghoul minion to fight alongside the necromancer
        elif move == "Curse of Weakness":
            return (0,0,["Debuff"]) #this skill is a debuff to decrease enemy attack power
        elif move == "Curse of Frailty":
            return (0,0,["Debuff"]) #this skill is a debuff to decrease enemy defense
        elif move == "Curse of Silence":
            return (0,0,["Debuff"]) #this skill is a debuff to prevent enemy from using skills
        elif move == "Plague Touch":
            return (attack_power * 1.1,0,["Poison"])
        elif move == "Bone Prison":
            return (0,0,["Control"]) #this skill is to control an enemy for 1 turn
        elif move == "Bone Armor":
            return (0,0,["Shield"]) #this skill is to shield the necromancer or an ally from damage
        elif move == "Mana Leech":
            return (attack_power * 0.1,0,["Dark"])
        elif move == "Sacrificial Pact":
            return (attack_power * 1.5,0,["Dark"])

    elif character == "Dragon":
        if move == "Flame Burst":
            return (attack_power * 1.3,0,["Fire"])
        elif move == "Tail Smash":
            return (attack_power * 1.2,0,["Physical"])
        elif move == "Wing Buffet":
            return (attack_power * 1.1,0,["Air"])
        elif move == "Dragon's Roar":
            return (attack_power * 1.4,0,["Fire","Air"])
        elif move == "Infernal Flight":
            return (attack_power*0.9*3,0,["Physical","Evade"]) #this skill is to evade the next enemy attack
        elif move == "Eternal Scales":
            return (0,0,["Buff"]) #this skill is a buff to increase defense

    elif character == "Dark Mage":
        if move == "Cataclysmic Void":
            return (attack_power * 1.4,0,["Arcane"])
        elif move == "Nether Eclipse":
            return (attack_power * 1.3,0,["Dark","Fire"])
        elif move == "Soul Annihilation":
            return (attack_power * 1.5,0,["Dark", "Ice"])
        elif move == "Forbidden Ascension":
            return (0,0,["Buff"]) #this skill is a buff to increase attack power and defense
        elif move == "Apocalypse Rain":
            return (attack_power * 1.2,0,["Dark", "Earth"])
        elif move == "Phantom Shroud":
            return (0,0,["Evade","Invisible"]) #this skill is to evade the next enemy attack and become invisible for 1 turn
        elif move == "WorldBreaker Hex (Ultimate)":
            return (attack_power * 2.0,0,["Dark", "Physical"])

    elif character == "Skeleton":
        if move == "Slash":
            return (attack_power,0,["Physical"])

    elif character == "Goblin":
        if move == "Slash":
            return (attack_power,0,["Physical"])
        elif move == "Goblin's Call":
            return (attack_power * 1.1,0,["Physical"])
        elif move == "Abominable Face":
            return (attack_power * 1.2,0,["Dark"])

    elif character == "Orc":
        if move == "Crushing Blow":
            return (attack_power * 1.3,0,["Physical"])
        elif move == "Roar of Confidence":
            return (0,0,["Buff"]) #this skill is a buff to increase attack power

    elif character == "Zombie":
        if move == "Scratch":
            return (attack_power,0,["Physical"])
        elif move == "Bite":
            return (attack_power * 1.1,0,["Physical"])
        elif move == "Growl":
            return (0,0,["Debuff"]) #this skill is a debuff to decrease enemy attack power

    elif character == "Ghoul":
        if move == "Putrid Claw":
            return (attack_power,0,["Physical"])
        elif move == "Corrupting Bite":
            return (attack_power * 1.2,0,["Poison"])
        elif move == "Grave Howl":
            return (0,0,["Debuff"]) #this skill is a debuff to decrease enemy defense
        elif move == "Soul Siphon":
            return (attack_power * 1.3,100,["Physical", "Heal"]) #this skill deals damage and heals the ghoul

    elif character == "Praetorian Guard":
        if move == "Iron Phalanx":
            return (0,0,["Shield"]) #this skill is to shield the praetorian guard or an ally from damage
        elif move == "Spear Thrust":
            return (attack_power * 1.2,0,["Physical"])
        elif move == "Shield Bash":
            return (attack_power * 0.8,0,["Physical"])
        elif move == "Fortress Stance":
            return (0,0,["Buff"]) #this skill is a buff to increase defense
"""

def calculate_damage(attack_power, health, move):
    dmg = 0
    heal = 0
    tags = []

    if move == "Slash":
        dmg = attack_power

    elif move == "Shield Bash":
        dmg = int(attack_power * 0.8)

    elif move == "Divine Judgemet":
        dmg = int(attack_power * 1.2)

    elif move == "Inspire":
        # Buff move → no damage, but apply buff
        tags.append("Buff")

    elif move == "Last Stand":
        dmg = int(attack_power * 1.5)

    elif move == "Rest":
        heal = 300  # you can tweak this value
        # Rest is healing only

    # --- Example: minion moves ---
    elif move == "Goblin's Call":
        dmg = int(attack_power * 1.1)

    elif move == "Abominable Face":
        tags.append("Debuff")

    elif move == "Crushing Blow":
        dmg = int(attack_power * 1.3)

    elif move == "Roar of Confidence":
        tags.append("Buff")

    elif move == "Scratch":
        dmg = attack_power

    elif move == "Bite":
        dmg = int(attack_power * 1.2)

    elif move == "Growl":
        tags.append("Debuff")

    elif move == "Putrid Claw":
        dmg = int(attack_power * 1.1)

    elif move == "Corrupting Bite":
        dmg = int(attack_power * 1.3)

    elif move == "Grave Howl":
        tags.append("Debuff")

    elif move == "Soul Siphon":
        dmg = int(attack_power * 1.2)
        heal = int(attack_power * 0.5)

    elif move == "Iron Phalanx":
        tags.append("Buff")

    elif move == "Spear Thrust":
        dmg = int(attack_power * 1.1)

    elif move == "Shield Bash":
        dmg = int(attack_power * 0.9)

    elif move == "Fotress Stance":
        tags.append("Buff")

    # Always return 3 values
    return dmg, heal, tags
