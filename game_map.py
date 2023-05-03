# In this file, I'll randomly create a "maze" of some sorts, where 
# the tiles in the maze are rooms/walls. 

import random
import Rooms

class Tile(object):
    def __init__(self) -> None:
        self.position = None
        self.visited = False
        self.north = None
        self.south = None
        self.east = None
        self.west = None

class Map(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rooms = []
        self.walls = []
        self.tiles = []
        self.generate()

    def printTiles(self):
        for tile in self.tiles:
            print(tile.position)

    def get_current_tile(self):
        return self.tiles[0]
    
    def set_current_tile(self, tile):
        self.tiles[0] = tile

    # Will use a randomized depth-first search to create a maze
    def generate(self):
        for i in range(self.width):
            for j in range(self.height):
                random_stone_rooom = Rooms.stoneHallway()
                #print(f"Initializing a new room with {random_stone_rooom.getDescription()}")
                self.tiles.append(random_stone_rooom)
                self.tiles[-1].position = (i, j)

        # Randomized depth-first search
        visited = [] # Start at the top left corner
        visited.append(self.tiles[0])
        self.tiles[0].visited = True
        print(f"Visited 0: {visited[0].position}")

        while len(visited) > 0:
            current = visited.pop() # 1. pop a cell from the stack and make it a current cell
            possible_moves = []
            # find all neighbors of current that have not been visited
            x = current.position[1]
            y = current.position[0]
            E = (y, x + 1)
            W = (y, x - 1)
            N = (y - 1, x)
            S = (y + 1, x)
            for tile in self.tiles:
                print(f"Tile position: {tile.position}")
                if E == tile.position: #and tile.visited == False:
                    possible_moves.append(["E",tile])
                if W == tile.position and tile.visited == False:
                    possible_moves.append(["W", tile])
                if N == tile.position and tile.visited == False:
                    possible_moves.append(["N", tile])
                if S == tile.position and tile.visited == False:
                    possible_moves.append(["S", tile]) 

            # 2. if the currenct cell has any neighbors that have not been visited:
            # 1. push the current cell to the stack
            visited.append(current) 
            # 2. Choose one of the unvisited neighbors
            if len(possible_moves) == 0:
                #print("No possible moves")
                break
            random_choice = random.choice(possible_moves)
            print(f"Direction: {random_choice[0]} Tile position: {random_choice[1].position}")
            # 3. Remove the wall between the current cell and the chosen cell
            if random_choice[0] == "E":
                current.east = random_choice[1]
                random_choice[1].east = current
            elif random_choice[0] == "W":
                current.west = random_choice[1]
                random_choice[1].west = current
            elif random_choice[0] == "N":
                current.north = random_choice[1]
                random_choice[1].north = current
            elif random_choice[0] == "S":
                current.south = random_choice[1]
                random_choice[1].south = current
            # 4. Mark the chosen cell as visited and push it to the stack
            random_choice[1].visited = True
            visited.append(random_choice[1])


if __name__ == '__main__':
    map = Map(3, 3)
    #ap.printTiles()
    # for i in range(9):
    #     print(map.tiles[i].position)
