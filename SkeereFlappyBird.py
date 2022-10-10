# Imports
import pygame
# from ground import ground

pygame.init()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (114, 177, 100)
blue = (194, 219, 229)
brown = (72, 63, 49)

# Popping the screen up.
size = (600, 600)
screen = pygame.display.set_mode(size)
# Titel verzinnen.
pygame.display.set_caption("game")

# Loop control.
end = False
clock = pygame.time.Clock()

# mainground = ground(0, 600, 200, 600, 0, green)

# Main program loop.
while not end:

    # Closing the screen when the player presses the close button.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
        if event.type == pygame.K_SPACE:
                speler.fly()

    dt = clock.tick(20) / 1000


    class Popetje:
        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y

            self.

            self.rect = self.plaatje.get_rect()

            self.rect.x = x
            self.rect.y = y

        def update(self, deltaTijd):
            self.rect.move_ip(100 * deltaTijd, 0)

 #       def render(self, screen):
 #           screen.blit(self. , self.rect)

    mijnpopetje = Popetje(10, 10, 100, 100)

    # drawing code
   # screen.fill(blue)

#mainground.update(dt)
#mainground.display(screen)

    pygame.display.flip()

pygame.quit()
