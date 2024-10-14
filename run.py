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
    Investigates the ships length, starting placement and the
     direction the ship is facing
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
    Produces valid warships to be placed on the board for the
     game by picking out the best from the list of ships
    """

    valid_ships = []
    for length_ships in ships:
        ship = [-1]
        while ship[0] == -1:
            create_ships = randint(0, 99)
            direction_ships = ["N", "S", "E", "W"]
            shuffle(direction_ships)
            ship = investigate_ship(length_ships, create_ships,
                                    direction_ships[0], occupied)
        valid_ships.append(ship)
        occupied = occupied + ship

    return valid_ships, occupied


def run_board(hit, miss, sunk):

    """
    Creates the board for the game by printing it
    """

    print("\n    Battleships: 1 player mode")
    print("   0  1  2  3  4  5  6  7  8  9")

    position = 0
    for xaxis in range(10):
        rows = ""
        for yaxis in range(10):
            water = " ~ "
            if position in hit:
                water = " x "
            elif position in miss:
                water = " = "
            elif position in sunk:
                water = " @ "
            rows = rows + water
            position = position + 1

        print(xaxis, rows)


def ok_guess(guess, in_play_warships, hit, miss, sunk):

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
    if valid is False:
        try:
            guess = input("\nEnter the coordinates for your guess: \n")
            guess = int(guess)
            if guess < 0:
                print(f"""\n{int(guess)} is invalid.
                Try coordinates between 0 and 99.""")
            elif guess > 99:
                print(f"""\n{int(guess)} is invalid.
                Try coordinates between 0 and 99.""")
            elif guess in player_guesses_taken:
                print("\nCoordinates already in use. Try again.")
            else:
                valid = True
        except ValueError:
            print("""\nThe guess you entered is invalid.
            Try coordinates between 0 and 99.""")

    return guess


def initial_info():

    """
    Serves the purpose of the rules and asking for the players name
    """
    print("=" * 30)
    print("Welcome to Battleships.")
    print("=" * 30)
    print("""This Battleships version is a strategic 1 player where you have 50
    shots to find and take out the enemies warships. If you have successfully
    sunk all warships in 50 moves, you win. However, if you don't quite sink
    all ships within the 50 strikes, the game resets.

    *** H I N T ***

    Coordinates are between 0 and 99.
    The first digit of your answer is for the row and the second is
    for your column.""")
    print("=" * 30)
    print("""LEGEND:
        WARSHIP MISS: =
        WARSHIP HIT:  x
        WARSHIP SUNK: @""")
    print("=" * 30)
    username = input("\nEnter a username: \n")
    if username == "":
        print("Username cannot be blank. Please enter a username.")
        print(" " * 30)
        return initial_info()
    else:
        return username

    print(f"\nWelcome {username}, Let's win this war at sea!")


def checking_empty_list(multiple_lists):

    """
    returns all empty lists considering whether they're empty or not
    """

    return all([not elem for elem in multiple_lists])


hit = []
miss = []
sunk = []
player_guesses_taken = []
missed_shot = 0
occupied = []

warships = [5, 4, 4, 3, 2, 2]
in_play_warships, occupied = building_ships(occupied, warships)
username = initial_info()

for num in range(50):
    player_guesses_taken = hit + miss + sunk
    guess = player_guess(player_guesses_taken)
    in_play_warships, hit, miss, sunk, missed_shot = ok_guess(guess,
                                                              in_play_warships,
                                                              hit, miss,
                                                              sunk)
    run_board(hit, miss, sunk)

    if checking_empty_list(in_play_warships):
        print("Congratulations, you've won the war at sea in", num, "shots.\n")
        break
