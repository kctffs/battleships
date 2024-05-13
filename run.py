def run_game():
    """
    Starts the battleships game and creates the board by correlating with the Board class; choosing
    size, number of battleships and name. Will reset previous plays.
    """
    print("   0  1  2  3  4  5  6  7 ")
    miss = []
    hit = []
    sunk = []
    
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

run_game()








