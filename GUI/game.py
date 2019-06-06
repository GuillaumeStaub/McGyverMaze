'''
This module represents the heart of the game. 
It initializes all other classes and harmonizes 
all the methods. It contains the main function of 
the game it is here that the game is launched.
'''

from GUI.labyrinthe import Labyrinth
from GUI.character import Character, EndOfGame
from GUI.menubar import MenuBar
from GUI.mute_button import MuteButton
from config import constants
import pygame
from pygame.locals import *


class Game:
    '''Class managing the execution of the game'''

    def __init__(self):
        # Initializing all classes and elements for the game
        self.mute = MuteButton()
        self.labyrinth = Labyrinth(constants.MAZE_1)
        self.character = Character(self.labyrinth)
        self.menu = MenuBar(self.character)
        # Initializing the game window and the background
        self.window = pygame.display.set_mode(
            [constants.SIZE_SCREEN_WIDTH, constants.SIZE_SCREEN_HEIGHT])
        self.background = constants.load_image(constants.BACKGROUND)
        pygame.display.set_caption(constants.NAME_GAME)
        # Create our Sprties to Initialize them
        self.char_sprite = pygame.sprite.RenderPlain((self.character))
        self.mute_sprite = pygame.sprite.RenderPlain((self.mute))
        self.text_box_sprite = pygame.sprite.RenderPlain((self.menu))
        self.allsprites = pygame.sprite.RenderPlain(
            (self.menu, self.mute, self.character))
        self.running = False

    def move(self, direction):
        '''Method to move McGyver and update his position in the maze'''
        self.character.walk(direction)
        self.character.rect = (
            self.character.position.y_pixel, self.character.position.x_pixel)
        self.char_sprite.clear(self.window, self.background)
        self.text_box_sprite.clear(self.window, self.menu.background)

    def endgame(self):
        '''Manage the end of game. The player lose or win the game and press return
        or escape to leave the game
        '''
        self.window.blit(self.character.message, (0, 100))
        running = True
        while running:
            pygame.time.Clock().tick(constants.FPS)
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key in (K_ESCAPE, K_RETURN):
                        running = False
            pygame.display.flip()

    def play_music(self):
        '''Manages the game background music in a loop'''
        pygame.mixer.init()
        constants.load_sound(constants.BACKGROUND_MUSIC)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(constants.VOLUME)

    def update_draw(self):
        '''Manages the update and the display of all sprites'''
        self.window.blit(self.menu.background, (0, 450))
        self.allsprites.update()
        self.mute_sprite.draw(self.window)
        self.text_box_sprite.draw(self.window)
        self.char_sprite.draw(self.window)
        pygame.display.flip()

    def start(self):

        # Initialize Pygame
        pygame.init()

        # Create and Display The Backgound
        self.window.blit(self.background, [0, 0])
        self.labyrinth.display_pygame(self.window)

        # Create The ToolBar
        self.window.blit(self.menu.background, (0, 450))

        # Initialize the background music
        self.play_music()

        # Hold down the keys on the keyboards
        pygame.key.set_repeat(400, 30)

        # MainLoop
        self.running = True
        try:
            while self.running:
                pygame.time.Clock().tick(constants.FPS)

                # Handle Input Events
                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.running = False

                    # For each event we erase the previous sprites
                    # and update them with their new features
                    elif event.type == KEYDOWN:
                        if event.key == (K_RIGHT):
                            self.move('R')
                        elif event.key == K_LEFT:
                            self.move('L')
                        elif event.key == K_UP:
                            self.move('U')
                        elif event.key == K_DOWN:
                            self.move('D')

                # Event to mute or play the background music
                    elif event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if self.mute.rect.collidepoint(event.pos):
                                self.mute.click_button()
                                self.mute_sprite.clear(
                                    self.window, self.menu.background)

                # If the character passes over the object,
                # the object disappears from the screen
                # and appears in the character's inventory
                self.character.pick_up_object()

                # Message end game, if you have all objects you win
                # else you lose. Blit message and quit game.
                self.character.fight()

                # Update and Draw everything
                self.update_draw()

        except EndOfGame:
            self.endgame()


def main():
    jeu = Game()
    jeu.start()


# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()
