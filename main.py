# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
black = (0, 0, 0) # Solid black colour (placed here for scope)

def main(): # Everything so far is inside main (code structure)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init() #Initializes pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # This determines the display resolution.

    iteration = 0 # Initializing iteration and setting starting value.
    
    # Infinite loop to keep the screen open and background display black until user closes window.
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Fill the entire surface with black
        screen.fill(black)
                
        # Update the display
        pygame.display.flip()
                
        # Increment the iteration counter
        iteration += 1
                
        # Print the current iteration
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

