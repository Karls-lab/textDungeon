# Python Dungeon Text Crawler
from ExplorationPhase import ExplorationPhase
from CombatPhase import CombatPhase
from Sprites import Creature
import Util as Util
from MonsterManual import MonsterManual
from random import randint

# General simple layout:
# First, enter the room and read description
# If there are monsters, resolve combat phase
# Search room, aquire items
# Go into next room

def getRandomAmountOfMonsters():
    shortSword = Util.Weapon("Short Sword", Util.Dice(6))
    Inventory = {shortSword.getName(): [shortSword, 1]}
    monsterManual = MonsterManual()
    monsterList = []
    amountOfMonsters = randint(0, 1)
    for monster in range(amountOfMonsters):
        goblin = Creature("red goblin", monsterManual.getGoblinStats(), Inventory, shortSword)
        monsterList.append(goblin)
    return monsterList



def main():
    print("-----------------------")
    print("Welcome to the Dungeon.")
    
    shortSword = Util.Weapon("Short Sword", Util.Dice(6))
    Inventory = {shortSword.getName(): [shortSword, 1]}


    monsterManual = MonsterManual()
    goblin_0 = Creature("red goblin", monsterManual.getGoblinStats(), Inventory, shortSword)
    goblin_1 = Creature("blue goblin", monsterManual.getGoblinStats(), Inventory, shortSword)
    hero = Creature("Claude", monsterManual.getPlayerStats(), Inventory, shortSword)

    # Inventory manegement
    hero.addToInventory(shortSword, 1)
    hero.changeWeapon(hero.getItemFromInventory(shortSword))

    # Main game loop:
    while(True):
        print("You kick open the door!")
        listOfMonsters = getRandomAmountOfMonsters()
        if len(listOfMonsters) > 0:
            print(f'there are {len(listOfMonsters)} goblins in the room!')

        combatPhase = CombatPhase(hero, listOfMonsters)
        combatPhase.run()
        pause = input("Press Enter to Continue...")

        explorationPhase = ExplorationPhase(hero)
        explorationPhase.run()
        pause = input("Press Enter to Continue...")


if __name__ == "__main__":
    main()


    