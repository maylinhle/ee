# Imports
import pygame
import math
import random


pygame.init()
clock = pygame.time.Clock()

# Settings
screenwidth = 600
screenheight = 800

gravity = 2

# Popping the screen up.
size = (screenwidth, screenheight)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("May Linh's flappy bird")

# Loop control.
end = False

# Converting the images
background = pygame.image.load("images/background.png").convert()
background = pygame.transform.scale(background, size)

bird = pygame.image.load("images/bird_wingup.png")
bird = pygame.transform.scale(bird,(42, 30))
birdRect = bird.get_rect(center=(100, 512))

ground = pygame.image.load("images/ground.png").convert()
ground = pygame.transform.scale(ground, (screenwidth, 200))

# Positions images
# Bird position
birdX = 150
birdY = 350
birdUpdateTime = pygame.time.get_ticks()

# Ground position
groundX = 0
groundY = 650

# Main program loop.
while not end:
    # Closing the screen when the player presses the close button.
    beginTime = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                birdY -= 50

    # update bird position
    if beginTime - birdUpdateTime >= 25:
        birdY += gravity
        birdUpdateTime = beginTime

    # Drawing code
    screen.blit(background, (0, 0))
    screen.blit(bird, (birdX, birdY))

    #ground
    screen.blit(ground, (groundX, groundY))
    screen.blit(ground, (groundX + screenwidth, groundY))
    groundX -= 1
    if groundX <= -screenwidth:
        groundX = 0

    pygame.display.update()
    clock.tick(120)
pygame.quit()
