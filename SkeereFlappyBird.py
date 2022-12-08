# Imports
import pygame

# funtions, putting these in a seperate document later
def checkActive():
    # Check if the bird doesn't hit the floor or flies too high (outside of the screen).
    if birdPosition.bottom >= 700 or birdPosition.top <= -10:
        return False
    else:
        return True

pygame.init()
clock = pygame.time.Clock()

# Settings
screenwidth = 600
screenheight = 800
gravity = 0.30
birdY = 0
birdCenterX = 150
birdCenterY = 200
groundX = 0
groundY = 700

# Popping the screen up.
size = (screenwidth, screenheight)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("May Linh's flappy bird")

# Loop control.
end = False
gameActive = True

# Converting the images.
# Background
background = pygame.image.load("images/background.png").convert()
background = pygame.transform.scale(background, size)
# Messages
getReady = pygame.image.load("images/getready.png")
#getReady = pygame.transform.scale2x(getReady, size)
gameOver = pygame.image.load("images/gameover.png")
gameOver = pygame.transform.scale2x(gameOver)
gameOverRect = gameOver.get_rect(center=(300, 300))
# Bird
bird = pygame.image.load("images/bird_up.png")
bird = pygame.transform.scale(bird, (42, 30))
# Ground
ground = pygame.image.load("images/ground.png").convert()
ground = pygame.transform.scale(ground, (screenwidth, 200))
# Pipe
pipe = pygame.image.load("images/pipe.png").convert()

# Bird position.
birdPosition = bird.get_rect(center=(birdCenterX, birdCenterY))

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
            # Respawn
            if event.key == pygame.K_SPACE and gameActive == False:
                birdPosition.center = (birdCenterX, birdCenterY)
                birdY = 0
                gameActive = True
    # Drawing code
    # Background
    screen.blit(background, (0, 0))
    # Bird
    #if gameActive:
    if gameActive:
        birdY += gravity
        birdPosition.centery += birdY
        screen.blit(bird, birdPosition)
        # Colliding
        gameActive = checkActive()
    elif gameActive == False:
        screen.blit(gameOver, (gameOverRect))
    # Ground
    screen.blit(ground, (groundX, groundY))
    screen.blit(ground, (groundX + screenwidth, groundY))
    groundX -= 1
    if groundX <= -screenwidth:
        groundX = 0

    pygame.display.update()
    clock.tick(120)

pygame.quit()
