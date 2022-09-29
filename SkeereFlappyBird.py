# Imports
import pygame

pygame.init()

# Colors
green = (114, 177, 100)

# The size of the screen.
size = (600, 600)
screen = pygame.display.set_mode(size)
# Titel verzinnen.
pygame.display.set_caption("game")

# Loop control.
end = False
# clock
# clock = pygame.time.Clock()

# Main program loop.
while not end:
    # Closing the screen.
    for event in pygame.event.get():
        if event.type == pygame.Quit:
            end = True
# fps invullen
# clock.tick()

pygame.quit()
