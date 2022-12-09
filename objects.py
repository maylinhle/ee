# Check if the player hasn't "died" yet
def check_active(birdPosition):
    # Check if the bird doesn't hit the floor or flies too high (outside the screen).
    if birdPosition.bottom >= 700 or birdPosition.top <= -10:
        return False
    else:
        return True