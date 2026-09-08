import pygame
import consts
import screen
import game_field

def main():
    pygame.init()
    running = True
    field = game_field.create_field()
    # screen.screen_green_color()
    # bush_img = pygame.image.load("bush.png")
    # screen.create_bush(bush_img)
    # bush_img = pygame.image.load("bush.png")
    # screen.create_bush(bush_img)

    # בדיקה של מצב2
    screen.screen_dark_color()
    screen.create_lines_net(field)
    bush_img = pygame.image.load("bush.png")
    screen.mines_field_ui(field, bush_img)

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

