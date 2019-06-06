'''
This module contains a class that symbolizes 
the playing surface. It is therefore this module
 that manages the generation of the level and
  the display of the elements of the game.
'''

from GUI.position import Position
import random
from config import constants


class Labyrinth:
    '''Class that manages the initialization of the maze from a text file,
    generating the objects at a random position and managing the display.
    '''

    def __init__(self, filename):
        self.filename = filename
        self.gates = []
        self.walls = []
        self.item = []
        self.start = None
        self.arrival = None
        self.hero = None
        self.width = None
        self.height = None
        # We must use the method of the Labyrinth class
        # to load the start position of our character
        self.load_from_file()
        # We must use the method of the Labyrinth class
        # to load the items position
        self.generate_item_position()

    def load_from_file(self):
        '''Manage the initialization of the maze
        from a text file self.filename.
        The method processes all the rows
        and columns of the file one by one and
        associates a character with a position of doors,
        walls, etc.
        '''
        with open(self.filename, 'r') as f:
            for num_line, line in enumerate(f):
                for num_column, carac in enumerate(line):
                    if carac == constants.GATES_CHAR:
                        self.gates.append(Position(num_line, num_column))
                    elif carac == constants.WALL_CHAR:
                        self.walls.append(Position(num_line, num_column))
                    elif carac == constants.START_CHAR:
                        self.start = Position(num_line, num_column)
                        self.gates.append(Position(num_line, num_column))
                    elif carac == constants.ARRIVAL_CHAR:
                        self.arrival = Position(num_line, num_column)
                        self.gates.append(Position(num_line, num_column))
                    self.width = num_column
                    self.height = num_line

    def generate_item_position(self):
        '''Manage the objects generating at
        a random position with random module
        The method generates the position of
        the objects by randomly selecting 3 crossing positions
        avoiding the starting position.'''
        self.item = random.sample(
            set(self.gates)-{self.start, self.arrival}, 3)
        return self.item

    def display_pygame(self, fenetre):
        for pos in self.walls:
            fenetre.blit(constants.load_image(constants.WALL),
                         (pos.y*constants.SIZE_SPRITE,
                          pos.x*constants.SIZE_SPRITE))
        for it, pos in enumerate(self.item):
            if it == 0:
                fenetre.blit(constants.load_image(
                    constants.SYRINGE),
                    (pos.y*constants.SIZE_SPRITE, pos.x*constants.SIZE_SPRITE))
            elif it == 1:
                fenetre.blit(constants.load_image(
                    constants.ETHER),
                    (pos.y*constants.SIZE_SPRITE, pos.x*constants.SIZE_SPRITE))
            elif it == 2:
                fenetre.blit(constants.load_image(
                    constants.TUBE),
                    (pos.y*constants.SIZE_SPRITE,
                     pos.x*constants.SIZE_SPRITE))
        fenetre.blit(constants.load_image(constants.GUARD),
                     (self.arrival.y * constants.SIZE_SPRITE,
                      self.arrival.x*constants.SIZE_SPRITE))
