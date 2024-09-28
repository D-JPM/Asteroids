
import pygame
from CircleShape import CircleShape
from constants import *
from constants import PLAYER_TURN_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS
from shot import Shot



class Player(CircleShape): # Class Player created and inherits from circleshape.
    def __init__ (self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.angle = 0  # Initialize angle to 0 (facing upwards)
         # Define the image as a surface (same size as the player)
        self.image = pygame.Surface((PLAYER_RADIUS * 2, PLAYER_RADIUS * 2), pygame.SRCALPHA)
    
        # Draw your player on this surface
        pygame.draw.polygon(self.image, "white", self.triangle())

        # Get a rect from the image
        self.rect = self.image.get_rect(center=(x, y))


    def move(self, dt, direction):  
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * direction
         

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        # Ensure rotation stays between 0 and 360
        self.rotation %= 360

        
    

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2 )

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt) 
        if keys[pygame.K_d]:
            self.rotate(+dt)
        if keys[pygame.K_w]:
            self.move(dt, 1)
        if keys[pygame.K_s]:
            self.move(dt, -1)

    # If a variable is greyed out by the IDE, its means that this variable is not being used yet. (reminder).

    def shoot(self):
        shot_direction = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_position = self.position + shot_direction * (self.radius + SHOT_RADIUS)
        shot_velocity = shot_direction * PLAYER_SHOOT_SPEED
        new_shot = Shot(shot_position.x, shot_position.y, shot_velocity)
        return new_shot
        
print("PLAYER_TURN_SPEED:", PLAYER_TURN_SPEED)