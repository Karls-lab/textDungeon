# Python Dungeon Text Crawler
import CombatPhase
import Sprites
import Util
import ExplorationPhase
from MonsterManual import MonsterManual


def main():
    print("Welcome to the Dungeon.")
    
    shortSword = Util.Weapon("Short Sword", Util.Dice(6))
    Inventory = {shortSword.getName(): [shortSword, 1]}


    monsterManual = MonsterManual()
    goblin_0 = Sprites.Creature("red goblin", monsterManual.getGoblinStats(), Inventory, shortSword)
    goblin_1 = Sprites.Creature("blue goblin", monsterManual.getGoblinStats(), Inventory, shortSword)
    hero = Sprites.Creature("Claude", monsterManual.getPlayerStats(), Inventory, shortSword)

    monsterList = []
    monsterList.append(goblin_0)
    monsterList.append(goblin_1)

    # Inventory manegement
    hero.addToInventory(shortSword, 1)
    hero.changeWeapon(hero.getItemFromInventory(shortSword))

    
    # give list of monsters
    #combatPhase = CombatPhase.CombatPhase(hero, monsterList)
    #combatPhase.run()

    # Exploration phase - this phase entails exploring a room, and gathering items
    explorationPhase = ExplorationPhase.ExplorationPhase(hero)
    explorationPhase.run()



if __name__ == "__main__":
    main()


    