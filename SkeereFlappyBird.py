# Imports
import pygame

def checkActive():
    # Check if the bird doesn't hit the floor or flies too high (outside of the screen)
    if birdPosition.top >= 700 or birdPosition.bottom <= 0:
        return False

pygame.init()
clock = pygame.time.Clock()

# Settings
screenwidth = 600
screenheight = 800

gravity = 0.30
birdY = 0


# Popping the screen up.
size = (screenwidth, screenheight)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("May Linh's flappy bird")

# Loop control.
end = False
gameActive = True

# Converting the images
# Background
background = pygame.image.load("images/background.png").convert()
background = pygame.transform.scale(background, size)
# Bird
bird = pygame.image.load("images/bird_up.png")
bird = pygame.transform.scale(bird, (42, 30))
# Ground
ground = pygame.image.load("images/ground.png").convert()
ground = pygame.transform.scale(ground, (screenwidth, 200))
# Pipe
pipe = pygame.image.load("images/pipe.png").convert()

# Positions
# Bird position
#birdX = 150
#birdY = 350
birdPosition = bird.get_rect(center=(150, 350))
#birdUpdateTime = pygame.time.get_ticks()

# Ground position
groundX = 0
groundY = 700

# Main program loop.
while not end:

    # Closing the screen when the player presses the close button.
    for event in pygame.event.get():
        if event.type == pygame.QUIT or gameActive == False:
            end = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                birdY = 0
                birdY -= 10
    # update bird position
    #if beginTime - birdUpdateTime >= 25:
    #    birdY += gravity
    #    birdUpdateTime = beginTime

    # Drawing code
    # Background
    screen.blit(background, (0, 0))
    # Bird
    birdY += gravity
    birdPosition.centery += birdY
    screen.blit(bird, birdPosition)
    #screen.blit(bird, (birdX, birdY))
    # Colliding
    gameActive = checkActive()

    # Ground
    screen.blit(ground, (groundX, groundY))
    screen.blit(ground, (groundX + screenwidth, groundY))
    groundX -= 1
    if groundX <= -screenwidth:
        groundX = 0

    pygame.display.update()
    clock.tick(120)

pygame.quit()
