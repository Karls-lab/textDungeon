# Python Dungeon Text Crawler
from ExplorationPhase import ExplorationPhase
from CombatPhase import CombatPhase
from Sprites import Creature
import Util as Util
from MonsterManual import MonsterManual
from random import randint
import game_map

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
        goblin = Creature("red goblin", monterManual.getGoblinStats(), Inventory, shortSword)
        monsterList.append(goblin)
    return monsterList



def main():
    print("\n\n\n\n")
    print("Welcome To The")
    print("-----------------------")
    # pause = input("Press Enter to Continue...\n\n")
    
    shortSword = Util.Weapon("Short Sword", Util.Dice(6))
    Inventory = {shortSword.getName(): [shortSword, 1]}

    monsterManual = MonsterManual()
    hero = Creature("Claude", monsterManual.getPlayerStats(), Inventory, shortSword)

    # Inventory manegement
    hero.addToInventory(shortSword, 1)
    hero.changeWeapon(hero.getItemFromInventory(shortSword))

    # Main game initialization:
    main_map = game_map.Map(2, 2)
    current_tile = main_map.get_current_tile()

    # Main game loop:
    while(True):
        # print("You kick open the door!")
        # listOfMonsters = [] #getRandomAmountOfMonsters()
        # if len(listOfMonsters) > 0:
        #     print(f'there are {len(listOfMonsters)} goblins in the room!')

        # combatPhase = CombatPhase(hero, listOfMonsters)
        # combatPhase.run()
        # pause = input("Press Enter to Continue...\n\n")

        explorationPhase = ExplorationPhase(hero, current_tile)
        explorationPhase.run()
        current_tile = explorationPhase.get_next_tile()
        main_map.set_current_tile(current_tile)
        print(f"my next tile: {current_tile}")
        pause = input("Press Enter to Continue...\n\n")


if __name__ == "__main__":
    main()


    