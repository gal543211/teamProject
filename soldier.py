import game_field
import consts

field = game_field.create_field()
game_field.print_field(field)




#Function to move the player in the matrix
#The functions gets a code, the code is one of these:
#TOP_KEY = 1, BOTTOM_KEY = 2, LEFT_KEY = 3, RIGHT_KEY = 4
def move_soldier(code):
    soldier_row, soldier_col = game_field.get_soldier_tile(field)

    #if the user pressed the left key
    if code == consts.LEFT_KEY:
        if soldier_col == 0: # checking the limits
            return False

        #if the tile we are moving the soldier into is a mine or a flag, we don't move him
        if field[soldier_row][soldier_col - 1] != consts.MINES_TILE \
            or field[soldier_row][soldier_col - 1] != consts.FLAG_TILE:
            field[soldier_row][soldier_col] = consts.EMPTY_TILE
            field[soldier_row][soldier_col - 1] = consts.SOLDIER_TILE

    # if the user pressed the right key
    elif code == consts.RIGHT_KEY:
        if soldier_col >= len(field):  # checking the limits
            return False

        #if the tile we are moving the soldier into is a mine or a flag, we don't move him
        if field[soldier_row][soldier_col + 1] != consts.MINES_TILE \
            or field[soldier_row][soldier_col + 1] != consts.FLAG_TILE:
            field[soldier_row][soldier_col] = consts.EMPTY_TILE
            field[soldier_row][soldier_col + 1] = consts.SOLDIER_TILE

    elif code == consts.TOP_KEY:
        if soldier_row <= 0:  # checking the limits
            return False

        #if the tile we are moving the soldier into is a mine or a flag, we don't move him
        if field[soldier_row - 1][soldier_col] != consts.MINES_TILE \
            or field[soldier_row - 1][soldier_col] != consts.FLAG_TILE:
            field[soldier_row][soldier_col] = consts.EMPTY_TILE
            field[soldier_row - 1][soldier_col] = consts.SOLDIER_TILE

    elif code == consts.BOTTOM_KEY:
        if soldier_row >= len(field):  # checking the limits
            return False

        #if the tile we are moving the soldier into is a mine or a flag, we don't move him
        if field[soldier_row + 1][soldier_col] != consts.MINES_TILE \
            or field[soldier_row + 1][soldier_col] != consts.FLAG_TILE:
            field[soldier_row][soldier_col] = consts.EMPTY_TILE
            field[soldier_row + 1][soldier_col] = consts.SOLDIER_TILE
    else:
        print("something went wrong")

    return True




def is_soldier_touching_flag():
    soldier_row, soldier_col = game_field.get_soldier_tile(field)
    for row in range(soldier_row, soldier_row + consts.SOLDIER_ROWS):
        for col in range(soldier_col, soldier_col + consts.SOLDIER_COLS):
            if field[row][col] == consts.FLAG_TILE:
                return True
    return False

def is_soldier_touching_mine():
    soldier_row, soldier_col = game_field.get_soldier_tile(field)
    for row in range(soldier_row, soldier_row + consts.SOLDIER_ROWS):
        for col in range(soldier_col, soldier_col + consts.SOLDIER_COLS):
            if field[row][col] == consts.MINES_TILE:
                return True
    return False
