# Imports
import pygame
from objects import *
from settings import *

pygame.init()
clock = pygame.time.Clock()

# Popping the screen up.
size = (screenwidth, screenheight)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("May Linh's flappy bird")

# Loop control.
end = False
gameActive = False

# Converting the images.
# Background
background = pygame.image.load("images/background.png").convert()
background = pygame.transform.scale(background, size)

# Messages
getReady = pygame.image.load("images/getready.png")
getReady = pygame.transform.scale2x(getReady)
getReadyRect = getReady.get_rect(center=(300, 400))
gameOver = pygame.image.load("images/gameover.png")
gameOver = pygame.transform.scale2x(gameOver)
gameOverRect = gameOver.get_rect(center=(300, 300))

# Bird
bird = pygame.image.load("images/bird_up.png")
bird = pygame.transform.scale(bird, (42, 30))
birdPosition = bird.get_rect(center=(birdCenterX, birdCenterY))

# Ground
ground = pygame.image.load("images/ground.png").convert()
ground = pygame.transform.scale(ground, (screenwidth, 200))

# Pipe
pipe = pygame.image.load("images/pipe.png").convert()
pipe = pygame.transform.scale2x(pipe)

pipeList = []
pygame.time.set_timer(pygame.USEREVENT, 1000)

# Main program loop.
while not end:

    # Closing the screen when the player presses the close button.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
        # Making the bird move by pressing space.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and gameActive:
                birdY = 0
                birdY -= 10
            # Respawning the bird by pressing space.
            if event.key == pygame.K_SPACE and gameActive is False:
                birdPosition.center = (birdCenterX, birdCenterY)
                birdY = 0
                gameActive = True

    # Drawing code
    # Background
    screen.blit(background, (0, 0))

    # Showing the "get ready" screen while the game is not active.
    if gameActive is False:
        screen.blit(getReady, getReadyRect)

    # Bird movement
    if gameActive:
        birdY += gravity
        birdPosition.centery += birdY
        screen.blit(bird, birdPosition)
        # Checking if the game is still active.
        gameActive = check_active(birdPosition)

    # Loading the (endless) ground.
    screen.blit(ground, (groundX, groundY))
    screen.blit(ground, (groundX + screenwidth, groundY))
    groundX -= 1
    if groundX <= -screenwidth:
        groundX = 0

    pygame.display.update()
    clock.tick(120)

pygame.quit()
