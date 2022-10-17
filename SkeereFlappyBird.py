# Imports
import pygame


pygame.init()

# Variables
gravity = 0.25

# Popping the screen up.
size = (600, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("May Linh's flappy bird")

# Loop control.
end = False
# clock = pygame.time.Clock()

# Converting the images
background = pygame.image.load("images/background.png").convert()
#background = pygame.transform.scale(background, size)
background_rect = background.get_rect()
size_factor = size[1] / background_rect.height
background = pygame.transform.scale(background,
                                    (background_rect.width * size_factor,
                                    background_rect.height * size_factor))

bird = pygame.image.load("images/bird_wingup.png")
bird = pygame.transform.scale(bird,(42, 30))

ground = pygame.image.load("images/ground.png").convert()
ground = pygame.transform.scale(ground, (600, 200))

# Main program loop.
while not end:
    # Closing the screen when the player presses the close button.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    # Drawing code
    screen.blit(background, (0, 0))
    screen.blit(bird, (150, 350))
    screen.blit(ground, (0, 650))

    pygame.display.update()
pygame.quit()
