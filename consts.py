#game field settings

BOARD_ROWS = 25
BOARD_COLS = 50

CELL_SIZE = 20  # pixels per cell

#screen settings
WINDOW_WIDTH = BOARD_COLS * CELL_SIZE
WINDOW_HEIGHT = BOARD_ROWS * CELL_SIZE


EMPTY_TILE = "E"

#flag location in the field
FLAG_TILE = "F"
FLAG_ROWS = 3
FLAG_COLS = 4

#mines settings
MINES_TILE = "M"
MINES_COUNT = 20
MINE_ROWS = 1
MINE_COLS = 3

#soldier settings
SOLDIER_TILE = "S"
SOLDIER_ROWS = 4
SOLDIER_COLS = 2
SOLDIER_BODY_ROWS = 3   # the upper part
SOLDIER_FEET_ROWS = 1   # the lower part

BUSH_WIDTH= CELL_SIZE*3
BUSH_HEIGHT= CELL_SIZE*3


#codes
EXIT = -1

LINE_WIDTH = 10
LINE_LONG = CELL_SIZE*BOARD_ROWS
