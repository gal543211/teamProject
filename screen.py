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
    for row in range(consts.BOARD_COLS):
        pygame.draw.line(screen, 'red', field[row][0], field[0][consts.BOARD_ROWS])
        row=row+1
        pygame.display.update()


# מתודה לציור החייל

# TODO: להוסיף תמונה למוקשים
