class Minion:
    def __init__(self,name,health,attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def get_minion(self):
        return f"Name:{self.name}\n  Health:{self.health}\n"

minion1 = Minion("Skeleton",1000,100)
minion2 = Minion("Goblin",1800,120)
minion3 = Minion("Orc",2500,180)
minion4 = Minion("Zombie",1500,120)
minion5 = Minion("Ghoul",2000,150)
minion6 = Minion("Praetorian Guard",3000,200)

minions = [minion1,minion2,minion3,minion4,minion5,minion6]
