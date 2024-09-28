import pygame
from constants import *
from CircleShape import CircleShape


white = (255, 255, 255)  # For scope and readability

SHOT_RADIUS = 5  # As specified in the assignment

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        self.image = pygame.Surface((SHOT_RADIUS * 2, SHOT_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, white, (SHOT_RADIUS, SHOT_RADIUS), SHOT_RADIUS)
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen):
        pygame.draw.circle(screen, white, self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt