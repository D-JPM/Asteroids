# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from AsteroidField import AsteroidField
from CircleShape import CircleShape



black = (0, 0, 0) # Solid black colour (placed here for scope)

# Adding in Groups
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()


# After initializing all groups
asteroid_field = AsteroidField(asteroids, updatable, drawable)
updatable.add(asteroid_field)

# Adding a container and we want player to be in them both.
Player.containers = (updatable, drawable)


def main(): # Everything so far is inside main (code structure)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init() #Initializes pygame
    clock = pygame.time.Clock() # Make a clock.
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # This determines the display resolution.

    iteration = 0 # Initializing iteration and setting starting value.
    
    # Infinite loop to keep the screen open and background display black until user closes window.
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    new_shot = player.shoot()
                    shots.add(new_shot)
                    updatable.add(new_shot)
                    drawable.add(new_shot)

        # Update game state
        dt = clock.tick(60) / 1000.0
        for sprite in updatable:
            sprite.update(dt)

        # Check collisions
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                running = False

        # Draw everything
        screen.fill(black)
        for sprite in drawable:
            sprite.draw(screen)

        # Update the display
        pygame.display.flip()

        # Increment the iteration counter
        iteration += 1
        print(f"Iteration: {iteration}")

# Quit Pygame
pygame.quit()

if __name__ == "__main__":
    main()

    # Notes on understanding the above block:
    # This checks if the script is being run directly and its not and import module.
    # If this condition is 'True' it will execute. if the Main is run directly it is called if not it aint called.
    # __name__ is a variable already built into the interpreter. When it is run directly __name__ will hold the string "main".
    # When a script is imported as a module, __name__ will hold the name of the module.
    # So to conclude, having this block allows us to identify straight away if this is the main script or an import module. 

