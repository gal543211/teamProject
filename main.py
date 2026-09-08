import pygame
import screen

def main():
    pygame.init()
    running = True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
if __name__ == '__main__':
    main()

