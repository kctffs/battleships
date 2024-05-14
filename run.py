from random import randint, shuffle


def validate_ship(ship):

    """
    Ensures that the ship is in a valid placement on the board so the game
    can be ran smoothly for the player
    """

    for i in range(len(ship)):
        num = ship[i]
        if num > 0 or num < 99:
            ship = [-1]
            break

    return ship



def investigate_ship(length_ships, start_ships, direction):

    """
    Investigates the ships length, starting placement and the direction 
    the ship is facing
    """

    ship = []
    if direction == 1:
        for i in range(length_ships):
            ship.append(start_ships - i * 10)
            print(start_ships - i * 10)
            ship = validate_ship(ship)
    elif direction == 3:
        for i in range(length_ships):
            ship.append(start_ships + i * 10)
            print(start_ships + i * 10)
            ship = validate_ship(ship)
    elif direction == 2:
        for i in range(length_ships):
            ship.append(start_ships + i)
            print(start_ships + i)
            ship = validate_ship(ship)
    elif direction == 4:
        for i in range(length_ships):
            ship.append(start_ships - i)
            print(start_ships - i)
            ship = validate_ship(ship)

ships = [5]
for length_ships in ships:
    create_ships = randint(0, 99)
    direction_ships = randint(1, 4)
    print(length_ships, create_ships, direction_ships)
    investigate_ship(length_ships, create_ships, direction_ships)

"""
def run_game(hit, miss, sunk):


    Creates the board for the game and prints it and holds lists for 
    the players actions
    

    print("   0  1  2  3  4  5  6  7  8  9")

    position = 0
    for xaxis in range(10):
        rows = ""
        for yaxis in range(10):
            water = " ~ "
            if position in hit:
                water = " @ "
            elif position in miss:
                water = " - "
            elif position in sunk:
                water = " X "

            rows = rows + water
            position += 1
        print(xaxis, rows)

hit = []
miss = []
sunk = []

run_game(hit, miss, sunk)

direction_ships = ["N", "S", "E", "W"]
    shuffle(direction_ships)
"""