import pygame
import constants
from player import Player

def main():
    pygame.init()
    print("Starting asteroids!")
    
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt=0

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        screen.fill((0, 0, 0))
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
