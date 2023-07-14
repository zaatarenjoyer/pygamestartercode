import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!

# DONE: Create a Ball class.
# DONE: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# DONE: Methods: __init__, draw, move

class Ball:
    def __init__(self, screen, color, x, y, radius, speed_x, speed_y):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        # Update pos
        self.x += self.speed_x
        self.y += self.speed_y

        # Check if the ball needs 2 be bouncy bouncy
        if self.x - self.radius < 0 or self.x + self.radius > self.screen.get_width():
            self.speed_x *= -1  # Reverse the horizontal direction

        if self.y - self.radius < 0 or self.y + self.radius > self.screen.get_height():
            self.speed_y *= -1  # Reverse the vertical direction

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    balls = []

    for x in range(100):
        color = pygame.color.Color((random.randint(0,255), random.randint(0,255), random.randint(0,255)))

        balls.append(Ball(screen, color, random.randint(0, screen.get_width()),
                            random.randint(0, screen.get_height()), random.randint(5,50),
                                random.randint(1,5), random.randint(1,5)))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # DONE: Move the ball
        for ball in balls:
            ball.move()
            ball.draw()

        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   DONE After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   DONE Make each ball a different color
#   DONE Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   DONE Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
