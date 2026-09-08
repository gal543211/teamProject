import pygame
import consts
import screen
import time

def main():
    pygame.init()
    running = True

    screen.screen_green_color()
    bush_img = pygame.image.load("bush.png")
    screen.create_bush(bush_img)
    bush_img = pygame.image.load("bush.png")
    screen.create_bush(bush_img)

    while running:
        code = handle_events()

        if code == consts.EXIT:
            running = False



def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return consts.EXIT

if __name__ == '__main__':
    main()

