import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:

    def __init__(self, screen, x, y):
        """ Creates a Raindrop sprite that travels down at a random speed. """

        # DONE 8: Initialize this Raindrop
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5, 10)
        self.color = pygame.color.Color((26, 83, 91))


    def move(self):
        """ Move the self.y value of the Raindrop down the screen (y increase) at the self.speed. """

        # DONE 11: Change the  y  position of this Raindrop by its speed.
        self.y += self.speed

    def off_screen(self):

        """ Returns true if the Raindrop y value is not shown on the screen, otherwise false. """

        # Note: this will be used for testing, but not used in the final version of the code for the sake of simplicity.
        # DONE 13: Return  True  if the  y  position of this Raindrop is greater than 800.
        return self.y > self.screen.get_height()

    def draw(self):

        """ Draws this sprite onto the screen. """

        # DONE 9: Draw a vertical line that is 5 pixels long, 2 pixels thick,
        #      from the current position of this Raindrop (use either a black or blue color).
        pygame.draw.line(self.screen, self.color, (self.x, self.y), (self.x, self.y+5), 2)


class Hero:

    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
        self.screen = screen
        self.x = x
        self.y = y
        self.image_umbrella = pygame.image.load(with_umbrella_filename)  # Load image with umbrella
        self.image_no_umbrella = pygame.image.load(without_umbrella_filename)  # Load image without umbrella
        self.last_hit_time = 0
        self.current_image = self.image_no_umbrella  # Set initial image to image without umbrella

    def draw(self):
        """ Draws this sprite onto the screen. """
        if time.time() - self.last_hit_time < 0.5:
            self.current_image = self.image_umbrella  # Change image to image with umbrella
        else:
            self.current_image = self.image_no_umbrella  # Change image to image without umbrella
        self.screen.blit(self.current_image, (self.x, self.y))

    def hit_by(self, raindrop):
        """ Returns true if the given raindrop is hitting this Hero, otherwise false. """
        return pygame.Rect(self.x, self.y, self.current_image.get_width(), self.current_image.get_height()).colliderect(
            pygame.Rect(raindrop.x, raindrop.y, 5, 5))


class Cloud:

    def __init__(self, screen, x, y, image_filename):

        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """
        # DONE 24: Initialize this Cloud, as follows:
        #     - Store the screen.
        #     - Set the initial position of this Cloud to x and y.
        #     - Set the image of this Cloud to the given image filename.
        #     - Create a list for Raindrop objects as an empty list called raindrops.
        #   Use instance variables:
        #      screen  x  y  image   raindrops.
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_filename)
        self.raindrops = []


    def draw(self):

        """ Draws this sprite onto the screen. """
        # DONE 25: Draw (blit) this Cloud's image at its current position.
        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):

        """ Adds a Raindrop to the array of raindrops so that it looks like the Cloud is raining. """

        # Append a new Raindrop to this Cloud's list of raindrops
        x = random.randint(self.x, self.x + 300)
        y = self.y + 100
        raindrop = Raindrop(self.screen, x, y)
        self.raindrops.append(raindrop)



def main():

    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """

    # DONE 1: Initialize the game, display a caption, and set   screen   to a 1000x600 Screen.
    pygame.init()

    pygame.display.set_caption("Mike and Alyssa's Rainy Day")

    screen = pygame.display.set_mode((1000, 600))

    # DONE 2: Make a Clock
    clock = pygame.time.Clock()

    # DONE 7: As a temporary test, make a new Raindrop called test_drop at x=320 y=10
    # test_drop = Raindrop(screen, 320, 10)

    # DONE 15: Make a Hero, named mike, with appropriate images, starting at position x=200 y=400.
    mike = Hero(screen, 200, 400, "Mike_umbrella.png", "Mike.png")

    # DONE 15: Make a Hero, named alyssa, with appropriate images, starting at position x=700 y=400.
    alyssa = Hero(screen, 700, 400, "Alyssa_umbrella.png", "Alyssa.png")

    # DONE 23: Make a Cloud, named cloud, with appropriate images, starting at position x=300 y=50.
    cloud = Cloud(screen, 300, 50,"cloud.png")

    # DONE 3: Enter the game loop, with a clock tick of 60 (or so) at each iteration.
    while True:

        clock.tick(60)

        # DONE 4:   Make the pygame.QUIT event stop the game.
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

        # DONE 27: Inside the game loop (AFTER the events loop above), get the list of keys that are currently pressed.
        #     Arrange so that the Cloud moves:
        #       5 pixels (or 10 pixels) to the right if the Right Arrow key (pygame.K_RIGHT) is pressed.
        #       5 pixels (or 10 pixels) to the left  if the Left  Arrow key (pygame.K_LEFT)  is pressed.
        #       5 pixels (or 10 pixels) up           if the Up    Arrow key (pygame.K_UP)    is pressed.
        #       5 pixels (or 10 pixels) down         if the Down  Arrow key (pygame.K_DOWN)  is pressed.
        # DISCUSS: If you want something to happen once per key press, put it in the events loop above
        #          If you want something to continually happen while holding the key, put it after the events loop.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and cloud.x != screen.get_width():
            cloud.x += 5
        elif keys[pygame.K_LEFT] and cloud.x != 0:
            cloud.x -= 5
        elif keys[pygame.K_UP] and cloud.y != 0:
            cloud.y -= 5
        elif keys[pygame.K_DOWN]:
            cloud.y += 5


        # DONE 5: Inside the game loop, draw the screen (fill with white)
        screen.fill((255, 255, 255))

        # --- begin area of test_drop code that will be removed later
        # DONE 12: As a temporary test, move test_drop
        # test_drop.move()



        # DONE 10: As a temporary test, draw test_drop
        # test_drop.draw()

        # DONE 20: As a temporary test, check if test_drop is hitting Mike (or Alyssa), if so set their last_hit_time
        # DONE 22: Remove the code that reset the y of the test_drop when off_screen()
        #          Instead reset the test_drop y to 10 when mike is hit, additionally set the x to 750
        #          Then add similar code to alyssa that sets her last_hit_time and moves the test_drop to 10 320
        # --- end area of test_drop code that will be removed later
        # if alyssa.hit_by(test_drop):
        #    alyssa.last_hit_time = time.time()
        #    test_drop.x, test_drop.y = (320,10)

        # if mike.hit_by(test_drop):
        #    mike.last_hit_time = time.time()
        #    test_drop.x, test_drop.y = (750,10)

        # DONE 26: Draw the Cloud.
        cloud.draw()
        # Update and draw raindrops

        cloud.rain()

        for raindrop in cloud.raindrops:

            raindrop.move()
            raindrop.draw()

            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)

            elif alyssa.hit_by(raindrop):
                alyssa.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)

            elif raindrop.off_screen():
                cloud.raindrops.remove(raindrop)


        # DONE 29: Remove the temporary testdrop code from this function and refactor it as follows:
        # DONE: Make the Cloud "rain", then:
        # DONE    For each Raindrop in the Cloud's list of raindrops:
            #       - move the Raindrop.
            #       - draw the Raindrop.
            # DONE  30: if the Hero (Mike or Alyssa) is hit by a Raindrop, set the Hero's last_time_hit to the current time.
            # Optional  - if the Raindrop is off the screen or hitting a Hero, remove it from the Cloud's list of raindrops.

        mike.draw()
        alyssa.draw()

        # DONE 6: Update the display and remove the pass statement below
        pygame.display.update()


main()