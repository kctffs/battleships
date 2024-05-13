print("   0  1  2  3  4  5  6  7 ")

hit = [63]
position = 0
for xaxis in range(8):
    rows = ""
    for yaxis in range(8):
        water = " ~ "
        if position in hit:
            water = " X "
        rows = rows + water
        position += 1
    print(xaxis, rows)

















#class Board:
    """
    Class for the games board which will hold lists, create the boards size, number of battleships,
    and the players name. Class will also print.
    """
    #def __init__(self, size, num_ships, player_name):
        #self.size = size
        #self.num_ships = num_ships
        #self.player_name = player_name

#def validate_chosen_guess():
    """
    In place to secure guesses are playable from the player
    """

#def chosen_guess():
    """
    Creating the input for the coord guessed by the player on the board.
    """


#def run_game():
    """
    Starts the battleships game and creates the board by correlating with the Board class; choosing
    size, number of battleships and name. Will reset previous plays.
    """