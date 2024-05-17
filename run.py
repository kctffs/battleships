from random import randint, shuffle


def validate_ship(ship, occupied):

    """
    Ensures that the ship is in a valid placement on the board so the game
    can be ran smoothly for the player
    """

    for i in range(len(ship)):
        number = ship[i]
        if number in occupied:
            ship = [-1]
            break
        elif number < 0:
            ship = [-1]
            break
        elif number > 99:
            ship = [-1]
            break

    return ship

def investigate_ship(length_ships, start_ships, direction, occupied):

    """
    Investigates the ships length, starting placement and the direction 
    the ship is facing
    """

    ship = []
    if direction == "N":
        for i in range(length_ships):
            ship.append(start_ships - i * 10)
    elif direction == "S":
        for i in range(length_ships):
            ship.append(start_ships + i * 10)
    elif direction == "E":
        for i in range(length_ships):
            ship.append(start_ships + i)
    elif direction == "W":
        for i in range(length_ships):
            ship.append(start_ships - i)
    ship = validate_ship(ship, occupied)

    return ship

def building_ships():

    """
    Produces valid warships to be placed on the board for the game by picking out the 
    best ships
    """

    occupied = []
    valid_ships = []
    ships = [4, 4, 3, 3, 2, 2, 2]
    for length_ships in ships:
        ship = [-1]
        while ship[0] == -1:
            create_ships = randint(0, 99)
            direction_ships = ["N", "S", "E", "W"]
            shuffle(direction_ships)
            ship = investigate_ship(length_ships, create_ships, direction_ships[0], occupied)
        valid_ships.append(ship)
        occupied = occupied + ship
    
    return valid_ships, occupied


def run_board(hit, miss, sunk):

    """
    Creates the board for the game by printing it and holds lists for 
    the games actions
    """

    print("   0  1  2  3  4  5  6  7  8  9")

    position = 0
    for xaxis in range(10):
        rows = ""
        for yaxis in range(10):
            water = " ~ "
            if position in hit:
                water = " x "
            elif position in miss:
                water = " - "
            elif position in sunk:
                water = " @ "
            rows = rows + water
            position += 1

        print(xaxis, rows)

def player_guess(player_guess_taken):

    """
    Function that takes the players guess with parameters that show errors where
    invalid inputs are being entered
    """

    valid = False
    while valid == False:
        try:
            guess = input("Enter the coordinates for your guess: \n")
            guess = int(guess)
            if guess < 0:
                print(f"{int(guess)} is invalid. Try coordinates between 0 and 99.")
            elif guess > 99:
                print(f"{int(guess)} is invalid. Try coordinates between 0 and 99.")
            elif guess in player_guess_taken:
                print("Coordinates already in use. Try again.")
            else:
                valid = True
        except ValueError:
            print("The guess you entered is invalid. Try coordinates between 0 and 99")


hit = []
miss = []
sunk = []

player_guess_taken = hit + miss + sunk
guess = player_guess(player_guess_taken)

ships, occupied = building_ships()
run_board(hit, miss, sunk)

