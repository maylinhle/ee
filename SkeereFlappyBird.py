# Imports
import pygame

pygame.init()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (114, 177, 100)
blue = (194, 219, 229)

# Popping the screen up.
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

    # Closing the screen when the player presses the close button.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    # drawing code
    screen.fill(blue)
    # pygame.draw.line(screen, green, [0, 10], [100, 110], 5)

# fps invullen
# clock.tick()

pygame.quit()
