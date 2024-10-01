import pygame
import constants

def main():
    pygame.init()
    print("Starting asteroids!")
    
    # Set up the game screen
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        screen.fill((0, 0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    main()
