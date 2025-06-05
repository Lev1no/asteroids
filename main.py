import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #game init
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #time for fps
    clock = pygame.time.Clock()
    dt = 0

    #instantiate the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return

        #clear screen
        screen.fill((0, 0, 0))  
        #draw the player
        player.draw(screen)
        #flip the display
        pygame.display.flip()

        #tick the clock to maintain 60fps and get delta time
        dt = clock.tick(60) / 1000 #convert ms to s

if __name__ == "__main__":
    main()     
