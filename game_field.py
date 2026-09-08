import random
import consts


#Function to create the main field
#the main field contains empty tiles, mines, and the flag at the end
#soldier location will be operated in soldier.py
def create_field():
    #creating empty field
    empty_field = create_empty_field()

    #adding the soldier to the field
    empty_field[0][0] = consts.SOLDIER_TILE

    #adding the flag to the field
    field_soldier_flag = insert_flag(empty_field)

    #filling the field with mines
    full_field = insert_landmines(field_soldier_flag)

    return full_field



#Function to create an empty field, containing for now only consts.EMPTY_TILE
#consts.EMPTY_TILE = "E", field full of E
def create_empty_field():
    field = []
    #going over each row
    for row in range(consts.BOARD_ROWS):
        field.append([])
        #going over each column
        for col in range(consts.BOARD_COLS):
            field[row].append(consts.EMPTY_TILE) #appending empty tiles
    return field

#Function to insert the flag to the bottom right location in the field
def insert_flag(field_with_soldier):
    for row in range(len(field_with_soldier) - consts.FLAG_ROWS, len(field_with_soldier)):
        for col in range(len(field_with_soldier[row]) - consts.FLAG_COLS, len(field_with_soldier[row])):
            field_with_soldier[row][col] = consts.FLAG_TILE
    return field_with_soldier


#Function to insert mines, mines takes 3 column
#The function randomize row and column, then checks if it is possible to place the mine there
def insert_landmines(empty_field):
    #going 20 times for 20 mines needed
    for mine in range(consts.MINES_COUNT):
        row = random.randint(0, consts.BOARD_ROWS - 1) #random row for the mine
        column = random.randint(0, consts.BOARD_COLS - 1) #random col for the min

        while not can_put_mines(empty_field, row, column):
            row = random.randint(0, consts.BOARD_ROWS - 1)  # random row for the mine
            column = random.randint(0, consts.BOARD_COLS - 1)  # random col for the min

        #with functions that I made, checking if it is possible to place the mind
        if can_put_mines(empty_field, row, column): #because the mine is 3 columns, placing mine on the next 3 columns
            empty_field[row][column] = consts.MINES_TILE
            empty_field[row][column + 1] = consts.MINES_TILE
            empty_field[row][column + 2] = consts.MINES_TILE

    return empty_field


#Function to check if it is possible to insert the mine
#cannot insert mines for 4 options:
#1. mines are on the soldier respawn point
#2. mines are already in the possession we want to insert
#3. mines column is out of range
#4. mines are on the flag
def can_put_mines(field, row, column):
    for checking_col in range(column, column + consts.MINE_COLS):
        if row <= consts.SOLDIER_ROWS and column <= consts.SOLDIER_COLS: #if mine on soldier respawn point
            return False
        if checking_col > consts.BOARD_COLS - 1: #if the column is out of range
            return False
        #if the mine is already a mine or a flag
        if field[row][checking_col] == consts.MINES_TILE and field[row][checking_col] == consts.FLAG_TILE \
                or (column > 0 and field[row][checking_col - 1] == consts.MINES_TILE):
                return False
    return True



#function to print the field
#not needed for the game, more for debug
def print_field(field):
    for row in range(len(field)):
        for column in range(len(field[row])):
            print(field[row][column], end=" ")
        print()



#IGNORE
#Function to insert the soldier to the top left location in the field
# def insert_soldier(empty_field):
#     for row in range(consts.SOLDIER_ROWS):
#         for col in range(consts.SOLDIER_COLS):
#             empty_field[row][col] = consts.SOLDIER_TILE
#     return empty_field