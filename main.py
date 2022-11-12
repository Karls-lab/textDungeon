# Python Dungeon Text Crawler
import CombatPhase
import Sprites
import Util
from MonsterManual import MonsterManual


def main():
    print("Welcome to the Dungeon.")
    
    shortSword = Util.Weapon("Short Sword", Util.Dice(6))
    Inventory = {shortSword.getName(): [shortSword, 1]}


    goblin_0 = Sprites.Creature("red goblin", MonsterManual.getGoblinStats(), Inventory, shortSword)
    goblin_1 = Sprites.Creature("blue goblin", MonsterManual.getGoblinStats(), Inventory, shortSword)
    hero = Sprites.Creature("Claude", MonsterManual.getPlayerStats(), Inventory, shortSword)

    monsterList = []
    monsterList.append(goblin_0)
    monsterList.append(goblin_1)

    hero.addToInventory(shortSword, 1)
    # print(hero.getItemFromInventory(shortSword))
    # print(hero.getAmountOf(shortSword))

    hero.changeWeapon(hero.getItemFromInventory(shortSword))

    
    #Action.attackCreature
    #hero.attackCreature(goblin_0)

    # give list of monsters
    combatPhase = CombatPhase.CombatPhase(hero, monsterList)
    combatPhase.run()
    #combatPhase.meleeAttack()


    #combatPhase.meleeAttack(hero, goblin_0)

    # Okay, so every Creature has a dictionary of stats and inventory items



if __name__ == "__main__":
    main()


    