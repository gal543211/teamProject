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
    bushes_lst = screen.create_bush()

    # יצירת שחקן בתחילת הלוח:
    day_solider_img = pygame.image.load("soldier.png")
    screen.create_player(day_solider_img,0,0)

    while running:
        code = 0
        code = handle_events()

        screen.draw_day(bushes_lst, field, code)

        if code == consts.EXIT:
            running = False

        if code==5:
            pygame.time.wait(1000)

        if code:
            field = soldier.move_soldier(code, field)

        print(f"The soldier is at: {game_field.get_soldier_tile(field)}")
        if soldier.is_soldier_touching_mine(field):
            print("You lost")
            running = False

        if soldier.is_soldier_touching_flag(field):
            print("You won")
            running = False

        #screen.print_screen(field)

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return consts.EXIT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                return consts.LEFT_KEY
            if event.key == pygame.K_RIGHT:
                return consts.RIGHT_KEY
            if event.key == pygame.K_UP:
                return consts.TOP_KEY
            if event.key == pygame.K_DOWN:
                return consts.BOTTOM_KEY
            if event.key == pygame.K_RETURN:
                return consts.ENTER_KEY

    return 0

if __name__ == '__main__':
    main()

