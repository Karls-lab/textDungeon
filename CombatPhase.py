class CombatPhase():
    def __init__(self, attackers: list, defenders: list):
        self.attackers = attackers
        self.defenders = defenders


    def meleeAttack(self, attacker, defender):
        print("--------------------")
        print(attacker.name + " attacked " + defender.name)
        attackModifer = attacker.stats["STR"]
        attackRoll = attacker.attackRoll() + attackModifer
        print(attacker.name + "'s  attack roll was: " + str(attackRoll))
        if(defender.compareAC(attackRoll)):
            print(attacker.name + " Hits!")
            dmg = attacker.attackDamage()
            defender.takeDamage(dmg)
            print(str(defender.name) + " took " + str(dmg) + " Damage! Their health is now: " + str(defender.getHealth()))
        else:
            print(str(attacker.name) + " misses!")

    def run(self):
        #This is where I will create my combat loop for 
        # encounters based on the list of attackers and defenders
        attacker = self.attackers
        defender = self.defenders[0]

        hasCombatEnded = False
        while(not hasCombatEnded):
            print("--------------------")
            print("available targets: ")
            for i in range(len(self.defenders)):
                defender = self.defenders[i]
                print(f'[{i}] {defender.name} HP: {defender.stats["HP"]}')
            targetId = int(input("Which one do you attack?: "))
            target = self.defenders[targetId]
            self.meleeAttack(attacker, target)
        