import pygame
import consts
import random

screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

# מתודה לציור רקע ירוק
def screen_green_color():
    screen.fill(pygame.Color("darkolivegreen1"))
    pygame.display.update()

# מתודה לציור רנדומלי של שיחים
def create_bush(bush_img):
    size=pygame.transform.scale(bush_img, (consts.BUSH_WIDTH, consts.BUSH_HEIGHT))
    for i in range(20):
        x = random.randrange(consts.WINDOW_WIDTH)
        y = random.randrange(consts.WINDOW_HEIGHT)
        screen.blit(size, (x, y))
        pygame.display.update()

# מתודה לציור רשת המטריצה והמוקשים
