import pygame
import consts
import screen
import game_field

def main():
    pygame.init()
    running = True
    field = game_field.create_field()

    while running:
        code = handle_events()

        if code == consts.EXIT:
            running = False

        screen.print_screen(field)


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return consts.EXIT
    return 0

if __name__ == '__main__':
    main()

