import pygame
import consts
import screen
import game_field
import soldier

def main():
    pygame.init()
    running = True
    field = game_field.create_field()

    while running:
        code = handle_events()

        if code == consts.EXIT:
            running = False

        if code:
            soldier.move_soldier(code)

        #creen.print_screen(field)



def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return consts.EXIT
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        return consts.LEFT_KEY
    if keys[pygame.K_RIGHT]:
        return consts.RIGHT_KEY
    if keys[pygame.K_UP]:
        return consts.TOP_KEY
    if keys[pygame.K_DOWN]:
        return consts.BOTTOM_KEY

    return 0

if __name__ == '__main__':
    main()

