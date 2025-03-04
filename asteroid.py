from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x , y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        first_angle = self.velocity.rotate(angle)
        second_angle = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_astro = Asteroid(self.position.x, self.position.y, new_radius)
        second_astro = Asteroid(self.position.x, self.position.y, new_radius)
        first_astro.velocity = first_angle * 1.2
        second_astro.velocity = second_angle * 1.2

