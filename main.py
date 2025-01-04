import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0
    
    asteroids = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    updatables = pygame.sprite.Group()

    Asteroid.containers = (asteroids, drawables, updatables)
    AsteroidField.containers = (updatables,)
    Player.containers = (drawables, updatables)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("Black")

        for sprite in updatables:
            sprite.update(dt)

        for sprite in drawables:
            sprite.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000
        


if __name__ == "__main__":
    main() 