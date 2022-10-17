# Imports
import pygame


pygame.init()

# Popping the screen up.
size = (600, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("May Linh's flappy bird")

# Loop control.
end = False
# clock = pygame.time.Clock()

# Converting the images
background = pygame.image.load("images/background.png").convert()
background = pygame.transform.scale(background, size)
#                                    background.width * 1.481481481,
#                                   background.height * 1.481481481)

bird = pygame.image.load("images/bird_wingup.png")
# bird = pygame.transform.scale(bird, )

# Main program loop.
while not end:
    # Closing the screen when the player presses the close button.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    # Drawing code
    screen.blit(background, (0, 0))
    screen.blit(bird, (150, 300))

    pygame.display.update()
pygame.quit()
