import pygame
from circleshape import CircleShape

class Asteroid(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
        pygame.sprite.Sprite.__init__(self)

        if hasattr(Asteroid, 'containers'):
            for group in Asteroid.containers:
                group.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color("white"), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
