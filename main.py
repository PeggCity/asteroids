import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player, Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0
    
    asteroids = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatables = pygame.sprite.Group()

    Asteroid.containers = (asteroids, drawables, updatables)
    AsteroidField.containers = (updatables,)
    Player.containers = (drawables, updatables)
    Shot.containers = (drawables, updatables, shots)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for sprite in updatables:
            sprite.update(dt)
               
        for sprite in asteroids:
            if sprite.collision(player):
                print("Game over!")
                event.type = pygame.QUIT
            
            for shot in shots:
                if sprite.collision(shot):
                    sprite.split()

        for sprite in drawables:
            sprite.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000
        


if __name__ == "__main__":
    main() 