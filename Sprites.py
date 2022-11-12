import Util


class Creature():
    def __init__(self, name, stats: dict, inventory: dict, equipedWeapon):
        self.name = name
        self.stats = stats
        self.inventory = inventory
        self.equipedWeapon = equipedWeapon

    def isDead(self):
        if(self.getHealth() <= 0):
            return True

    def changeWeapon(self, Newweapon):
        self.equipedWeapon = Newweapon
    
    def compareAC(self, attackNumber):
        if(attackNumber > self.stats["AC"]):return True
        else: return False

    def attackRoll(self):
        d20 = Util.Dice(20)
        return d20.roll()

    def attackDamage(self):
        return self.equipedWeapon.rollAttack()

    def takeDamage(self, damageTaken):
        self.stats["HP"] = self.stats["HP"] - damageTaken

    def getHealth(self):
        return self.stats["HP"]

    def itemExistsInInventory(self, item):
        if(self.inventory.__contains__(item)):
            return True
        else: 
            return False

    def addToInventory(self, item, amount):
        # check if item is in inventory first
        if(self.itemExistsInInventory(item)):
            self.inventory[item][amount] += 1
        else: # add item to dictionary
            self.inventory[item] = [item, amount]

    def getItemFromInventory(self, item):
        if(self.itemExistsInInventory(item)):
            # zero represents object, 1 is the amount
            return self.inventory[item][0] 

    def getAmountOf(self, item):
        if(self.itemExistsInInventory(item)):
            return self.inventory[item][1]
        else:
            return None