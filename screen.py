import pygame
import consts
import random
import game_field

screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

# מתודה לציור רקע ירוק
def screen_green_color():
    screen.fill(pygame.Color("darkolivegreen1"))
    pygame.display.update()

# מתודה לציור רקע כהה
def screen_dark_color():
    screen.fill(pygame.Color("grey9"))
    pygame.display.update()

# מתודה לציור רנדומלי של שיחים + שמירת מיקומי השיחים
def create_bush():
    bushes_lst = []
    for i in range(20):
        x = random.randrange(consts.WINDOW_WIDTH-consts.BUSH_WIDTH)
        y = random.randrange(consts.WINDOW_HEIGHT-consts.BUSH_HEIGHT)
        bushes_lst.append((x,y))
    return bushes_lst

# מתודה לציור רשת המטריצה
def create_lines_net(field):
    for x in range(0, consts.WINDOW_WIDTH, consts.CELL_SIZE):
        for y in range(0, consts.WINDOW_HEIGHT, consts.CELL_SIZE):
            rect = pygame.Rect(x, y, consts.CELL_SIZE, consts.CELL_SIZE)
            pygame.draw.rect(screen, 'red', rect, 1)
    pygame.display.update()

# מתודה לציור המוקשים
def mines_field_ui(field, mine_png):
    mine=pygame.transform.scale(mine_png, (consts.CELL_SIZE * consts.SOLDIER_BODY_ROWS, consts.CELL_SIZE * consts.SOLDIER_BODY_ROWS))
    for row in range(len(field)-1):
        for col in range(len(field[row])-1):
            if field[row][col+1] == consts.MINES_TILE:
                continue
            elif field[row][col] == consts.MINES_TILE:
                screen.blit(mine, ((col+1) * consts.CELL_SIZE, row * consts.CELL_SIZE))
                pygame.display.update()

# מתודה לציור החייל בתחילת הלוח
def create_player(soldier_png, row, col):
    solider=pygame.transform.scale(soldier_png, (consts.CELL_SIZE * consts.SOLDIER_COLS, consts.CELL_SIZE * consts.SOLDIER_ROWS))
    screen.blit(solider, (row, col))
    pygame.display.update()

# מתודה למציאת משבצת התחלה חלק עליון- חייל
def top_place(field):
    soldier_row_and_col=game_field.get_soldier_tile(field)
    top_row= soldier_row_and_col[0]+2
    top_col= soldier_row_and_col[1]
    return (top_row, top_col)

# מתודה למציאת משבצת התחלה חלק תחתון- חייל
def bottom_place(soldier_png, field):
    soldier_row_and_col = game_field.get_soldier_tile(field)
    bottom_row = soldier_row_and_col[0]+3
    bottom_col = soldier_row_and_col[1]
    return (bottom_row, bottom_col)

# מתודה לציור הדגל בסוף הלוח
def create_flag(flag_png):
    flag = pygame.transform.scale(flag_png, (consts.CELL_SIZE * consts.FLAG_COLS,consts.CELL_SIZE * consts.FLAG_ROWS))
    screen.blit(flag, (consts.FLAG_X_LOCATION*consts.CELL_SIZE, consts.FLAG_Y_LOCATION*consts.CELL_SIZE))
    pygame.display.update()

# להדפסת מיקום החייל
def move_soldier_ui(field, soldier_img):
    row=game_field.get_soldier_tile(field)[0]*consts.CELL_SIZE
    col=game_field.get_soldier_tile(field)[1]*consts.CELL_SIZE
    create_player(soldier_img, row, col)
    pygame.display.update()

# פונקציה לגודל החייל
