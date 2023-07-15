import pygame
import sys


# --------------------------- Conversion helper functions ---------------------------

def get_row_col(mouse_pos):
    """ Converts an (x, y) screen position into a row, col value. """
    mouse_x = mouse_pos[0]  # Note: a point tuple is now passed into this function.
    mouse_y = mouse_pos[1]
    # Note: the top row is row=0 (bottom row=2), left col is col=0 (right col=2)
    spacing_x = 86 + 8
    spacing_y = 98 + 5
    top_y = 50
    left_x = 50
    return (mouse_y - top_y) // spacing_y, (mouse_x - left_x) // spacing_x


def get_xy_position(row, col):
    """ Converts a row, col value into an x, y screen position (upper left corner of that location). """
    spacing_x = 86 + 11
    spacing_y = 98 + 8
    top_y = 50
    left_x = 50
    return left_x + col * spacing_x, top_y + row * spacing_y


# --------------------------- Model Object ---------------------------


class Game:
    def __init__(self):
        # Create an empty board, called board
        # A list that contains 3 lists, each of those lists has 3 "." values.
        # Create a game_state_string set to X's turn
        # Create a turn_counter variable set to 0
        # Create a game_is_over variable set to False
        self.board = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
            ]
        self.game_state_string = 'X'
        self.turn_counter = 0
        self.game_is_over = False
        self.music = pygame.mixer.Sound("win.mp3")
        self.font = pygame.font.SysFont("Comic Sans", 30)

    def __repr__(self):
        """Returns a string that represents the game."""
        # Use a "".format() command to create a string that shows the board, turn_counter, and game_state_string
        return "\n {}\nTurns: {}\n{}'s turn".format(str(self.board).replace('],', '\n').replace('[', '').replace(']', '').replace("'", "").replace(",", ""), self.turn_counter, self.game_state_string)


    def take_turn(self, row, col):
        """Handle the current turn of the player and update board array"""
        if self.game_is_over:
            return

        if not 0 <= row <= 2 or not 0 <= col <= 2:
            return

        if self.board[row][col] != '.':
            return

        if self.game_state_string == 'X':
            self.board[row][col] = 'X'
            self.game_state_string = 'O'
        else:
            self.board[row][col] = 'O'
            self.game_state_string = 'X'

        self.turn_counter += 1

        self.check_for_game_over()

    def check_for_game_over(self):
        if self.turn_counter >= 9:
            self.game_state_string = "Tie Game"
            self.game_is_over = True

        lines = []
        lines.append(self.board[0][0] + self.board[0][1] + self.board[0][2])  # Top row
        lines.append(self.board[1][0] + self.board[1][1] + self.board[1][2])  # Middle row
        lines.append(self.board[2][0] + self.board[2][1] + self.board[2][2])  # Bottom row
        lines.append(self.board[0][0] + self.board[1][0] + self.board[2][0])  # Left column
        lines.append(self.board[0][1] + self.board[1][1] + self.board[2][1])  # Middle column
        lines.append(self.board[0][2] + self.board[1][2] + self.board[2][2])  # Right column
        lines.append(self.board[0][0] + self.board[1][1] + self.board[2][2])  # Diagonal from top-left to bottom-right
        lines.append(self.board[0][2] + self.board[1][1] + self.board[2][0])  # Diagonal from top-right to bottom-left

        for line in lines:
            if line == 'XXX':
                self.game_state_string = "X wins"
                self.game_is_over = True
                self.music.play()
                return
            elif line == 'OOO':
                self.game_state_string = "O wins"
                self.game_is_over = True
                self.music.play()
                return



# --------------------------- View Controller ---------------------------

class ViewController:

    def __init__(self, screen):
        """ Creates the view controller (the Tic-Tac-Toe game you see) """
        # DONE 4: Initialize the ViewController, as follows:
        #     - Store the screen.
        #     - Create the game model object.
        #     - Create images for the board, X, and O images filenames.
        #  Use instance variables:   screen game board_image x_image o_image
        self.screen = screen
        self.game = Game()
        self.board_image = pygame.image.load("board.png")
        self.o_image = pygame.image.load("o_mark.png")
        self.x_image = pygame.image.load("x_mark.png")

    def check_event(self, event):
        """ Takes actions as necessary based on the current event. """
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            row, col = get_row_col(mouse_pos)
            self.game.take_turn(row, col)

        elif event.type == pygame.KEYDOWN:
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_SPACE]:
                # Reset the game
                self.game = Game()

        # DONE 17: If the event is pygame.KEYDOWN
        #     Get the pressed_keys
        #     If the key is pygame.K_SPACE, then reset the game.

    def draw(self):
        """ Draw the board based on the marked store in the board configuration array """
        # Set the image size as a square centered in the middle of the window
        image_size = min(self.screen.get_width(), self.screen.get_height())
        image_pos = ((self.screen.get_width() - image_size) // 2, (self.screen.get_height() - image_size) // 2)

        # Resize the board image to the calculated size
        board_image = pygame.transform.scale(self.board_image, (image_size, image_size))

        # DONE 13: Blit the board_image onto the screen at the calculated position
        self.screen.blit(board_image, image_pos)

        # DONE 14: Use a nested loop (via range) to go over all marks of the game.board
        # If the mark is "X", blit an X image at the calculated position of row col
        # If the mark is "O", blit an O image at the calculated position of row col
        for row_idx, row in enumerate(self.game.board):
            for col_idx, col in enumerate(row):
                if col == 'O':
                    x_pos = image_pos[0] + int(image_size * (col_idx / 3))
                    y_pos = image_pos[1] + int(image_size * (row_idx / 3))
                    o_image = pygame.transform.scale(self.o_image, (int(image_size / 3), int(image_size / 3)))
                    self.screen.blit(o_image, (x_pos, y_pos))
                elif col == 'X':
                    x_pos = image_pos[0] + int(image_size * (col_idx / 3))
                    y_pos = image_pos[1] + int(image_size * (row_idx / 3))
                    x_image = pygame.transform.scale(self.x_image, (int(image_size / 3), int(image_size / 3)))
                    self.screen.blit(x_image, (x_pos, y_pos))

        # DONE 15: Update the display caption to be the game.game_state_string
        pygame.display.set_caption(self.game.game_state_string + "'s turn")



# --------------------------- Controller ---------------------------


def main():
    pygame.init()
    pygame.mixer.music.load("win.mp3")
    screen = pygame.display.set_mode((380, 400))

    # DONE 1: Create an instance of the ViewController class called view_controller
    view_controller = ViewController(screen)

    # DONE 6: Write test code as needed to develop your model object.
    game = Game()
    print(game.__repr__)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # DONE 2: Pass the event to the view_controller
            data = view_controller.check_event(event)

        screen.fill(pygame.Color("white"))

        # DONE 3: Draw the view_controller
        view_controller.draw()

        pygame.display.update()


main()
