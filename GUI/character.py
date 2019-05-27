from GUI.labyrinthe import Labyrinth
from config import constants
import pygame


class EndOfGame(Exception):
    '''Manage end of the game by raising an exception'''
    pass


class Character(pygame.sprite.Sprite):
    '''Class that manages the character, his position,
    his movements, how he pick up the objects and
    how he reacts to the guard.
    '''

    def __init__(self, laby):
        pygame.sprite.Sprite.__init__(self)
        self.labyrinth = laby
        self.position = self.labyrinth.start
        self.labyrinth.hero = self
        self.inventory = []
        self.image = constants.load_image(constants.CHARACTER, conv=False)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position.y_pixel, self.position.x_pixel
        self.message = None

    def walk(self, direction):
        '''Manage the character's movement by going to the position class and
        the Labyrinth class to find out if moving is possible or not.
        '''
        new_position = self.position + direction
        if new_position in self.labyrinth.gates:
            self.position = new_position
        return self.position

    def pick_up_object(self):
        '''Manages the collection of objects scattered in the labyrinth.
         When the hero passes over the object,
         the object is picked up and stored in the Labyrinth.
         '''
        pygame.init()
        if self.position in self.labyrinth.item:
            if self.position in self.inventory:
                pass
            else:
                # Whenever our character pick up an object a sound sounded
                sound = constants.load_sound(constants.DROP_SOUND, music=False)
                sound.play()
                self.inventory.append(self.position)

    def fight(self):
        '''Manages the final fight with the goalkeeper.
        If our hero has the three items in his inventory
        he passes the keeper and wins the game otherwise he loses.
        '''

        if self.position == self.labyrinth.arrival:
            pygame.mixer.music.stop()
            if len(self.inventory) == 3:
                self.message = constants.load_image('win.png')
                sound = constants.load_sound(constants.WIN_SOUND, music=False)
                sound.play()
                raise EndOfGame("You win")
            else:
                self.message = constants.load_image('lose.png')
                sound = constants.load_sound(constants.LOSE_SOUND, music=False)
                sound.play()
                raise EndOfGame("You lose")
