class skillLimit:
    def __init__(self):
        self.usage = {} #skill name use count
        self.cooldown = {} #skill name cooldown time

    def can_use(self,skill_name,max_uses=None,cooldown=None):
        #check the skill if it is on cooldown or max uses reached
        if max_uses is not None and self.usage.get(skill_name,0) >= max_uses:
            return False

        if cooldown is not None and self.cooldown.get(skill_name,0) > 0:
            return False

        return True

def apply_use(self,skill_name,cooldown=None):
    #register the skill usage and start the cooldown if there are any
    self.usage[skill_name] = self.usage.get(skill_name,0) + 1
    if cooldown:
        self.cooldown[skill_name] = cooldown

def reduce_cooldowns(self):
    #Reduce all the cooldown by 1 turn(call this at the end of each turn)
    for skill in list(self.cooldown.keys()):
        if self.cooldowns[skill] > 0:
            self.cooldowns[skill] -= 1