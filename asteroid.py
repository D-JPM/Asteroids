import pygame
import random
from constants import *
from CircleShape import CircleShape

white = (255, 255, 255) # For scope and readbility.


class Asteroid(CircleShape):  # Assuming CircleShape is correctly imported
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)  # An empty surface with transparency
        pygame.draw.circle(self.image, (255, 255, 255), (radius, radius), radius, 2)
        self.rect = self.image.get_rect(center=(x, y))
         

    def draw(self, screen):
        pygame.draw.circle(screen, white, self.position, self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt
