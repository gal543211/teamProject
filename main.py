import pygame
import consts
import screen
import game_field
import soldier

def main():
    pygame.init()
    running = True
    field = game_field.create_field()
    screen.screen_green_color()
    bush_img = pygame.image.load("bush.png")
    screen.create_bush(bush_img)
    bush_img = pygame.image.load("bush.png")
    screen.create_bush(bush_img)

    # בדיקה של מצב2
    # screen.screen_dark_color()
    # screen.create_lines_net(field)
    # mine_img = pygame.image.load("mine.png")
    # screen.mines_field_ui(field, mine_img)

    # יצירת שחקן בתחילת הלוח:

    day_solider_img = pygame.image.load("soldier.png")
    screen.create_player(day_solider_img)

    # יצירת דגל בסוף הלוח
    flag_img = pygame.image.load("flag.png")
    screen.create_flag(flag_img)

    while running:
        code = 0
        code = handle_events()

        if code == consts.EXIT:
            running = False

        if code:
            soldier.move_soldier(code)

        #screen.print_screen(field)

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return consts.EXIT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print(f"Returning: {consts.LEFT_KEY}")
                return consts.LEFT_KEY
            if event.key == pygame.K_RIGHT:
                print(f"Returning: {consts.RIGHT_KEY}")
                return consts.RIGHT_KEY
            if event.key == pygame.K_UP:
                print(f"Returning: {consts.RIGHT_KEY}")
                return consts.TOP_KEY
            if event.key == pygame.K_DOWN:
                print(f"Returning: {consts.BOTTOM_KEY}")
                return consts.BOTTOM_KEY

    return 0

if __name__ == '__main__':
    main()

