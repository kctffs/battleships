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


def building_ships(occupied, ships):


    """
    Produces valid warships to be placed on the board for the game by picking out the 
    best from the list of ships
    """

    valid_ships = []
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
    Creates the board for the game by printing it
    """

    print("\n   Battleships")
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
            position = position + 1

        print(xaxis, rows)


def validate_guess(guess, in_play_warships, hit, miss ,sunk):


    """
    Confirms that the players guesses are either hitting, missing,
    or sinking the warships in the game
    """

    missed_shot = 0
    for i in range(len(in_play_warships)):
        if guess in in_play_warships[i]:
            in_play_warships[i].remove(guess)
            if len(in_play_warships[i]) > 0:
                hit.append(guess)
                missed_shot = 1
            else:
                sunk.append(guess)
                missed_shot = 2
    if missed_shot == 0:
        miss.append(guess)

    return in_play_warships, hit, miss, sunk, missed_shot


def player_guess(player_guesses_taken):


    """
    Takes the players guess with parameters that show errors where
    invalid inputs are being entered
    """

    valid = False
    while valid == False:
        try:
            guess = input("\nEnter the coordinates for your guess: \n")
            guess = int(guess)
            if guess < 0:
                print(f"\n{int(guess)} is invalid. Try coordinates between 0 and 99.")
            elif guess > 99:
                print(f"\n{int(guess)} is invalid. Try coordinates between 0 and 99.")
            elif guess in player_guesses_taken:
                print("\nCoordinates already in use. Try again.")
            else:
                valid = True
        except ValueError:
            print("\nThe guess you entered is invalid. Try coordinates between 0 and 99")

    return guess


def initial_info():


    """
    Serves the purpose of the rules and asking for the players name
    """

    print("Welcome to Battleships.")
    print("""\nThis Battleships version is a strategic 1 player where you have 50 shots
to find and take out the enemies warships.""")
    print("""\nLEGEND:
    WARSHIP MISS: -
    WARSHIP HIT: x
    WARSHIP SUNK: @""")
    username = input("\nEnter a username: \n")
    print(f"\nWelcome {username}, Let's win this war at sea!")


hit = []
miss = []
sunk = []
player_guesses_taken = []
missed_shot = 0
occupied = []

warships = [4, 4, 3, 3, 2, 2]
in_play_warships, occupied = building_ships(occupied, warships)
username = initial_info()

for num in range(5):
    player_guesses_taken = hit + miss + sunk
    guess = player_guess(player_guesses_taken)
    in_play_warships, hit, miss, sunk, missed_shot = validate_guess(guess, in_play_warships, hit, miss, sunk)
    run_board(hit, miss, sunk)

    if len(in_play_warships) < 1:
        print(f"\nCongratulations {username}, you've won the war at sea.")
