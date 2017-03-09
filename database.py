############################################SYSTEMS###############################################

############################################SKILLS################################################
class Skill(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def __str__(self):
        return self.name + "\n" + self.description

class Damage_Skill(Skill):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage

    def get_damage(self):
        return self.damage

class DOT_Skill(Damage_Skill):
    def __init__(self, name, description, damage, dot, turns):
        super().__init__(name, description, damage)
        self.dot = dot
        self.turns = turns

    def get_dot(self):
        return self.dot

    def get_turns(self):
        return self.turns

class Heal_Skill(Skill):
    def __init__(self, name, description, heal_amt):
        super().__init__(name, description)
        self.heal_amt = heal_amt

    def get_heal_amt(self):
        return self.heal_amt

class HOT_Skill(Heal_Skill):
    def __init__(self, name, description, heal_amt, hot, turns):
        super().__init__(name, description, heal_amt)
        self.hot = hot
        self.turns = turns

    def get_hot(self):
        return self.hot

    def get_turns(self):
        return self.turns

class Status_Skill(Skill):
    def __init__(self, name, description, turns, recover_chance):
        super().__init__(name, description)
        self.turns = turns
        self.recover_chance = recover_chance

    def get_turns(self):
        return self.turns

    def get_recover_chance(self):
        return self.recover_chance
class SD_Skill(Status_Skill):
    def __init__(self, name, description, turns, recover_chance, damage):
        super().__init__(name, description, turns, recover_chance)
        self.damage = damage

    def get_damage(self):
        return self.damage
        
###########################################CLASSES##############################################
class Player(object):
    def __init__(self, name, clss, lvl, maxhp, maxmp, maxexp, dfn, mdfn, atk, matk, spd):
        self.name = name
        self.clss = clss
        self.lvl = lvl
        self.maxhp = maxhp
        self.hp = maxhp
        self.maxmp = maxmp
        self.mp = maxmp
        self.maxexp = maxexp
        self.exp = 0
        self.dfn = dfn
        self.mdfn = mdfn
        self.atk = atk
        self.matk = matk
        self.spd = spd
        self.items = [["Potions"], ["Armour"], ["Weapons"], ["Consumables"]]
        self.skills = []

    def attack(self, target):
        damage(self, target)

    def display_status(self):
        print(self.name + "(LVL." + str(self.lvl) + " " + self.clss +"): ")
        print("Experience points: " + str(self.exp) + "/" + str(self.maxexp))
        print("Health Points: " + str(self.hp) + "/" + str(self.maxhp))
        print("Mana Points: " + str(self.mp) + "/" + str(self.maxmp))
        print("Attack : " + str(self.atk))
        print("Magic Attack : " + str(self.matk))
        print("Armour : " + str(self.dfn))
        print("Magic defense: " + str(self.mdfn))
        print("Speed: " +str(self.spd))

    def display_items(self):
        for item_type in self.items:
            result_item = item_type[0] + ": "
            for i in range(len(item_type)):
                if i != 0 :
                    result_item += item_type[i].get_name() + ", "
            print(result_item[:-2])

    def display_item_discription(self, item_type, item_no):
        return str(self.items[item_type][item_no + 1])

class Warrior(Player):
    def __init__(self, name, lvl, maxhp, maxmp, maxexp, dfn, mdfn, atk, matk, spd):
        super().__init__(name, "Warrior", lvl, maxhp, maxmp, maxexp, dfn, mdfn, atk, matk, spd)

    def lvl_up:
        pass
    
############################################OBJECTS############################################

#############################################ENEMIES###########################################

