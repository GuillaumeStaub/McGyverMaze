'''
This module contains one class to manage the character. 
Methods that manage the movement, the collection
 of objects and the final confrontation. 
 '''

from terminal.labyrinthe import Labyrinth
from terminal.position import Position


class Character:
    '''Class that manages the character, his position, his movements,
    how he pick up the objects and how he reacts to the guard.
    '''

    def __init__(self, laby):
        self.labyrinth = laby
        self.position = self.labyrinth.start
        self.labyrinth.hero = self
        self.inventory = []
        self.name = "M"

    def move(self, direction):
        '''Manage the character's movement by going to the position
        class and the Labyrinth class to find out
        if moving is possible or not.
        '''
        nouvelle_position = self.position + direction
        if nouvelle_position in self.labyrinth.gates:
            self.position = nouvelle_position
        return self.position

    def pick_up_object(self):
        '''Manages the collection of objects scattered in the labyrinth.
        When the hero passes over the object, the object is picked up
        and stored in the Labyrinth.
        '''
        self.inventory.append(self.position)
        print("You have picked up an object")
        print(f"You have {len(self.inventory)} objects in your inventory")

    def fight(self):
        '''Manages the final fight with the goalkeeper.
        If our hero has the three items in his inventory he passes the keeper
        and wins the game otherwise he loses.
        '''
        if len(self.inventory) == 3:
            print("You win !")
        else:
            print("You lose !")
