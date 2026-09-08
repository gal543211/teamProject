import pygame
import consts
import screen

def main():
    pygame.init()
    running = True


    while running:
        code = handle_events()

        if code == consts.EXIT:
            running = False




def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return consts.EXIT
    return 0

if __name__ == '__main__':
    main()

