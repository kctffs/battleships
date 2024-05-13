def run_game(hit, miss, sunk):
    """
    Creates the board for the game and prints it and holds lists for the players actions
    """
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








