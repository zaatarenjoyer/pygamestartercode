import pygame, sys
import math


def distance(mouse, center):
    """ Distance Between Two Tuples """
    dist_x, dist_y = mouse
    center_x, center_y = center

    return math.sqrt((dist_x-center_x)**2+(dist_y-center_y)**2)


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Click In The Circle!")
    font = pygame.font.Font(None, 25)

    sound1 = pygame.mixer.Sound("drums.wav")

    instruction_text = 'Click in the circle'
    text_color = (222, 222, 0)
    instructions_image = font.render(instruction_text, True, text_color)

    circle_color = (154, 58, 212)
    circle_center = (screen.get_width() // 2, screen.get_height() // 2)
    circle_radius = 50
    circle_border_width = 3

    message_text = ''

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # DONE 2: For a MOUSEBUTTONDOWN event get the click position.
            if event.type == pygame.MOUSEBUTTONDOWN:

                # DONE 3: Determine the distance between the click position and the circle_center using the distance

                distance_from_circle = distance(pygame.mouse.get_pos(), circle_center)

                # DONE 5: If distance_from_circle is less than or equal to circle_radius, set message_text to 'Bullseye!'
                if distance_from_circle <= circle_radius:
                    message_text = 'Bullseye!'
                
                    # DONE 9: Start playing the music mixer looping forever if the click is within the circle
                    sound1.play(loops=-1)

                # DONE 5: If distance_from_circle is greater than the circle_radius, set the message_text to 'You missed!'
                elif distance_from_circle > circle_radius:
                    message_text = 'You missed!'

                    # DONE 10: Stop playing the music if the click is outside the circle
                    sound1.stop()

        screen.fill(pygame.Color("Black"))

        # DONE 1: Draw the circle using the screen, circle_color, circle_center, circle_radius, and circle_border_width
        pygame.draw.circle(screen, circle_color, circle_center, circle_radius, circle_border_width)

        # DONE 6: Create a text image (render the text) based on the message_text with the color (122, 237, 201)
        message_color = pygame.color.Color(122, 237, 201)
        font1 = pygame.font.SysFont("Comic Sans", 30)

        message_render = font1.render(message_text, True, message_color)

        screen.blit(instructions_image, (25, 25))

        # DONE 7: Draw (blit) the message to the user that says 'Bullseye!' or 'You misssed!'
        screen.blit(message_render, ((screen.get_width()-message_render.get_width())*.5, screen.get_height()*.75))

        pygame.display.update()


main()
