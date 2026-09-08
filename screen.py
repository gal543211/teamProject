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
def mines_field_ui(field, bush_png):
    img=pygame.transform.scale(bush_png, (consts.BUSH_WIDTH, consts.BUSH_HEIGHT))
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == consts.MINES_TILE:
                screen.blit(img, (row*consts.CELL_SIZE, (col+1) *consts.CELL_SIZE))
                pygame.display.update()

# מתודה לציור החייל
