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

# Pipes
pipeImage = pygame.image.load("images/pipe.png").convert()
pipeImage = pygame.transform.scale(pipeImage, (73.2, 449.7))

pipeList = []
pipeHeights = [300, 350, 400, 450, 500, 550, 600]
pygame.time.set_timer(pygame.USEREVENT, 1100)

# Loop control.
end = False
gameActive = False

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
                birdY -= 8
            # Respawning the bird by pressing space.
            if event.key == pygame.K_SPACE and gameActive is False:
                birdY = 0
                birdPosition.center = (birdCenterX, birdCenterY)
                gameActive = True
                pipeList.clear()
        # Creating the pipes and putting them in a list.
        if event.type == pygame.USEREVENT and gameActive:
            pipeList.extend(spawn_pipe(pipeImage, pipeHeights))

    # Drawing code
    # Background
    screen.blit(background, (0, 0))

    # Showing the "get ready" screen while the game is not active.
    if gameActive is False:
        screen.blit(getReady, getReadyRect)

    # Letting things run when the game is active.
    if gameActive:
        # Bird movement
        birdY += gravity
        birdPosition.centery += birdY
        screen.blit(bird, birdPosition)

        # Loading the (random) pipes.
        pipeList = move_pipe(pipeList)
        # Drawing them
        for pipe in pipeList:
            if pipe.bottom >= 700:
                screen.blit(pipeImage, pipe)
            else:
                flipTopPipe = pygame.transform.flip(pipeImage, False, True)
                screen.blit(flipTopPipe, pipe)

        # Checking if the game is still active.
        gameActive = check_hit(birdPosition, pipeList)

    # Loading the (endless) ground.
    screen.blit(ground, (groundX, groundY))
    screen.blit(ground, (groundX + screenwidth, groundY))
    groundX -= birdSpeed
    if groundX <= -screenwidth:
        groundX = 0

    pygame.display.update()
    clock.tick(120)

pygame.quit()
