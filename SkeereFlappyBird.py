# Imports
import pygame


pygame.init()

# Popping the screen up.
size = (600, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("May Linh's flappy bird")

# Loop control.
end = False
#clock = pygame.time.Clock()

# Main program loop.
while not end:

    # Closing the screen when the player presses the close button.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

#    dt = clock.tick(20) / 1000
    pygame.display.update()
pygame.quit()
