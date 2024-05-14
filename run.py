from random import randint, shuffle


def validate_ship(ship):

    """
    Ensures that the ship is in a valid placement on the board so the game
    can be ran smoothly for the player
    """

    for i in range(len(ship)):
        number = ship[i]
        if number < 0:
            ship = [1000]
            break
        elif number > 99:
            ship = [1000]
            break
        elif ship[i] % 10 == 9 and i < len(ship)-1:
            if ship[i + 1] % 10 == 0:
                ship = [1000]
                break

    return ship



def investigate_ship(length_ships, start_ships, direction):

    """
    Investigates the ships length, starting placement and the direction 
    the ship is facing
    """

    ship = []
    if direction == "N":
        for i in range(length_ships):
            ship.append(start_ships - i * 10)
            ship = validate_ship(ship)
    elif direction == "S":
        for i in range(length_ships):
            ship.append(start_ships + i * 10)
            ship = validate_ship(ship)
    elif direction == "E":
        for i in range(length_ships):
            ship.append(start_ships + i)
            ship = validate_ship(ship)
    elif direction == "W":
        for i in range(length_ships):
            ship.append(start_ships - i)
    ship = validate_ship(ship)
    return ship

valid_ships = []
ships = [4, 3, 3]
for length_ships in ships:
    ship = [1000]
    while ship[0] == 1000:
        create_ships = randint(0, 99)
        direction_ships = ["N", "S", "E", "W"]
        shuffle(direction_ships)
        print(length_ships, create_ships, direction_ships[0])
        ship = investigate_ship(length_ships, create_ships, direction_ships[0])
    valid_ships.append(ship)
    print(valid_ships)

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
"""