# Imports
import random
from settings import *

# Check if the bird hasn't "died" yet
def check_active(birdPosition):
    # Check if the bird doesn't hit the floor or flies too high (outside the screen).
    if birdPosition.bottom >= 700 or birdPosition.top <= -10:
        return False
    else:
        return True

# Creating pipes with random heights.
def spawn_pipe(pipeImage, pipeHeights):
    randomPipeHeight = random.choice(pipeHeights)
    topPipe = pipeImage.get_rect(midbottom=(800, randomPipeHeight -250))
    bottomPipe = pipeImage.get_rect(midtop=(800, randomPipeHeight))
    return topPipe, bottomPipe

# Letting the pipes move.
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= birdSpeed
    return pipes