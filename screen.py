import pygame
from pygame.surface import Surface

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

# מתודה לציור רנדומלי של שיחים
def create_bush(bush_img):
    size=pygame.transform.scale(bush_img, (consts.BUSH_WIDTH, consts.BUSH_HEIGHT))
    for i in range(20):
        x = random.randrange(consts.WINDOW_WIDTH-consts.BUSH_WIDTH)
        y = random.randrange(consts.WINDOW_HEIGHT-consts.BUSH_HEIGHT)
        screen.blit(size, (x, y))
        pygame.display.update()

# מתודה לציור רשת המטריצה
def create_lines_net(field):
    for x in range(0, consts.WINDOW_WIDTH, consts.CELL_SIZE):
        for y in range(0, consts.WINDOW_HEIGHT, consts.CELL_SIZE):
            rect = pygame.Rect(x, y, consts.CELL_SIZE, consts.CELL_SIZE)
            pygame.draw.rect(screen, 'red', rect, 1)
    pygame.display.update()

# מתודה לציור המוקשים
def mines_field_ui(field, mine_png):
    mine=pygame.transform.scale(mine_png, (consts.CELL_SIZE * 3, consts.CELL_SIZE * 3))
    for row in range(len(field)-1):
        for col in range(len(field[row])-1):
            if field[row][col+1] == consts.MINES_TILE:
                continue
            elif field[row][col] == consts.MINES_TILE:
                screen.blit(mine, ((col+1) * consts.CELL_SIZE, row * consts.CELL_SIZE))
                pygame.display.update()


# מתודה לציור החייל בתחילת הלוח
def create_player(solider_png):
    solider=pygame.transform.scale(solider_png, (consts.CELL_SIZE * 2, consts.CELL_SIZE * 4))
    screen.blit(solider, (0, 0))
    pygame.display.update()

# מתודה למציאת משבצות חלק תחתון- חייל
# def top_place(solider_png, field):


# מתודה למציאת משבצות חלק עליון- חייל
# def bottom_place(solider_png, field):


# מתודה לציור הדגל בסוף הלוח
def create_flag(flag_png):
    flag = pygame.transform.scale(flag_png, (consts.CELL_SIZE * consts.FLAG_COLS,consts.CELL_SIZE * consts.FLAG_ROWS))
    screen.blit(flag, (consts.FLAG_X_LOCATION*consts.CELL_SIZE, consts.FLAG_Y_LOCATION*consts.CELL_SIZE))
    pygame.display.update()

# TODO: פונקציה לגודל החייל

