import game_field
import consts

field = game_field.create_field()
list_of_mines = game_field.return_mines_location(field)


#Function to move the player in the matrix
#The functions gets a code, the code is one of these:
#TOP_KEY = 1, BOTTOM_KEY = 2, LEFT_KEY = 3, RIGHT_KEY = 4
def move_soldier(code):
    soldier_row, soldier_col = game_field.get_soldier_tile(field)

    print(f"Got code {code}")
    #if the user pressed the left key
    if code == consts.LEFT_KEY:
        if soldier_col == 0: # checking the limits
            return False

        print(f"going to {soldier_row},  {soldier_col - 1}")
        #if the tile we are moving the soldier into is a mine or a flag, we don't move him
        if field[soldier_row][soldier_col - 1] != consts.MINES_TILE \
            or field[soldier_row][soldier_col - 1] != consts.FLAG_TILE:
            field[soldier_row][soldier_col] = consts.EMPTY_TILE
            field[soldier_row][soldier_col - 1] = consts.SOLDIER_TILE

    # if the user pressed the right key
    elif code == consts.RIGHT_KEY:
        if soldier_col >= len(field[soldier_row]):  # checking the limits
            return False

        print(f"going to {soldier_row}, {soldier_col + 1}")
        #if the tile we are moving the soldier into is a mine or a flag, we don't move him
        if field[soldier_row][soldier_col + 1] != consts.MINES_TILE \
            or field[soldier_row][soldier_col + 1] != consts.FLAG_TILE:
            field[soldier_row][soldier_col] = consts.EMPTY_TILE
            field[soldier_row][soldier_col + 1] = consts.SOLDIER_TILE

    # if the user pressed the top key
    elif code == consts.TOP_KEY:
        if soldier_row <= 0:  # checking the limits
            return False


        print(f"going to {soldier_row - 1} {soldier_col}")
        #if the tile we are moving the soldier into is a mine or a flag, we don't move him
        if field[soldier_row - 1][soldier_col] != consts.MINES_TILE \
            or field[soldier_row - 1][soldier_col] != consts.FLAG_TILE:
            field[soldier_row][soldier_col] = consts.EMPTY_TILE
            field[soldier_row - 1][soldier_col] = consts.SOLDIER_TILE

    # if the user pressed the bottom key
    elif code == consts.BOTTOM_KEY:
        if soldier_row >= len(field):  # checking the limits
            return False

        #if the tile we are moving the soldier into is a mine or a flag, we don't move him
        print(f"going to {soldier_row + 1} {soldier_col}")
        if field[soldier_row + 1][soldier_col] != consts.MINES_TILE \
            or field[soldier_row + 1][soldier_col] != consts.FLAG_TILE:
            field[soldier_row][soldier_col] = consts.EMPTY_TILE
            field[soldier_row + 1][soldier_col] = consts.SOLDIER_TILE
    else:
        print("something went wrong")

    return True


#function that checks if the soldier is touching the flag
def is_soldier_touching_flag():
    soldier_row, soldier_col = game_field.get_soldier_tile(field)
    for row in range(soldier_row, soldier_row + consts.SOLDIER_ROWS):
        for col in range(soldier_col, soldier_col + consts.SOLDIER_COLS):
            if field[row][col] == consts.FLAG_TILE:
                return True
    return False

#function the checks if the soldier is touching a mine
def is_soldier_touching_mine():
    soldier_row, soldier_col = game_field.get_soldier_tile(field)
    left_foot, right_foot = get_soldier_two_foots(soldier_row, soldier_col)

    left_row, left_col = left_foot
    if field[left_row][left_col] == consts.MINES_TILE:
        return True

    right_row, right_col = right_foot
    if field[right_row][right_col] == consts.MINES_TILE:
        return True

    return False

def get_soldier_two_foots(soldier_row, soldier_col):
    return (soldier_row + 3, soldier_col), (soldier_row + 3 , soldier_col + 1)


print(is_soldier_touching_mine())