from constants import *
from player import *
import pygame

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0
    
    drawables = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    Player.containers = (drawables, updatables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("Black")

        for updatable in updatables:
            player.update(dt)
        for drawable in drawables:
            player.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000
        


if __name__ == "__main__":
    main() 