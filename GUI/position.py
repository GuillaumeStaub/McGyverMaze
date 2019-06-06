'''
This module is the backbone of the game. 
It contains the class position that serves 
as a template for positioning game elements 
and managing the movement of the hero.
'''

from config import constants


class Position:
    '''Class that manages all the positions in the maze
     x being the line number and y the column number
     '''

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    @property
    def x_pixel(self):
        '''Property that calculates the pixel position'''
        return self.x*constants.SIZE_SPRITE

    @property
    def y_pixel(self):
        '''Property that calculates the pixel position'''
        return self.y*constants.SIZE_SPRITE

    def move_down(self):
        '''Manages the downward movement of the hero'''
        return Position(self.x+1, self.y)

    def move_up(self):
        '''Manages the upward movement of the hero'''
        return Position(self.x-1, self.y)

    def move_left(self):
        '''Manages the movement to the left of the hero'''
        return Position(self.x, self.y-1)

    def move_right(self):
        '''Manages the movement to the right of the hero'''
        return Position(self.x, self.y+1)

    def __add__(self, direction):
        '''Operator overload plus to facilitate the call of the
         direction function
         '''
        if direction == "U":
            return self.move_up()
        elif direction == "D":
            return self.move_down()
        elif direction == "L":
            return self.move_left()
        elif direction == 'R':
            return self.move_right()

    def __eq__(self, item_to_compare):
        '''Equal operator overload to compare positions'''
        if self.x == item_to_compare.x and self.y == item_to_compare.y:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y))
