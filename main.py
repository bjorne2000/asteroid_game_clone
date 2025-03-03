import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()


    AsteroidField.containers = updatables
    Player.containers = updatables, drawables
    Asteroid.containers = (asteroids, updatables, drawables)

    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    clock = pygame.time.Clock()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in asteroids:
            if player.collision_check(obj):
                print("Game Over")
                return
            
        for obj in updatables:
            obj.update(dt)
    

        screen.fill((0, 0, 0))

        for obj in drawables:
            obj.draw(screen)

        pygame.display.flip()


        dt = clock.tick(60) / 1000





if __name__ == "__main__":
    main()