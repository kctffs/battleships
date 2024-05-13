from random import randint, shuffle


def investigate_ship(length_ships, start_ships, direction):
    """
    Investigates the ships length, starting placement and the direction the ship is facing
    """
    ship = []
    if direction == "N":
        for num in range(length_ships):
            ship.append(start_ships - num * 10)
            print(start_ships - num * 10)
    elif direction == "S":
        for num in range(length_ships):
            ship.append(start_ships + num * 10)
            print(start_ships + num * 10)
    elif direction == "E":
        for num in range(length_ships):
            ship.append(start_ships + num)
            print(start_ships + num)
    elif direction == "W":
        for num in range(length_ships):
            ship.append(start_ships - num)
            print(start_ships - num)


ships = [4]
for length_ships in ships:
    create_ships = randint(0, 63)
    direction_ships = ["N", "S", "E", "W"]
    shuffle(direction_ships)
    print(length_ships, create_ships, direction_ships[0])
    investigate_ship(length_ships, create_ships, direction_ships[0])

"""
def run_game(hit, miss, sunk):
    
    Creates the board for the game and prints it and holds lists for the players actions
    
    print("   0  1  2  3  4  5  6  7 ")
    
    position = 0
    for xaxis in range(8):
        rows = ""
        for yaxis in range(8):
            water = " ~ "
            if position in hit:
                water = " X "
            elif position in miss:
                water = " - "
            elif position in sunk:
                water = " @ "

            rows = rows + water
            position += 1
        print(xaxis, rows)

hit = []
miss = []
sunk = []

run_game(hit, miss, sunk)
"""
