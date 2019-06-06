'''
This module allows in our game to display 
a text bar that indicates the progress 
of the player. Indicates the number of items 
he has in his inventory and whether 
he can lull the guard.
'''
from GUI.character import Character
from config import constants
import pygame


class MenuBar(pygame.sprite.Sprite):

    def __init__(self, character):
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()
        self.perso = character
        self.background = constants.load_image(constants.MENU, conv=False)
        self.message = pygame.font.SysFont(
            constants.FONT_GAME, constants.SIZE_FONT_MENU)
        self.image = self.render_object()
        self.rect = self.image.get_rect()
        self.rect.topleft = 20, 465

    def update(self):
        self.render_object()

    def render_object(self):
        if len(self.perso.inventory) == 0:
            self.image = self.message.render(
                f"Collect the 3 items to put the guard to sleep",
                True, constants.COLOR_FONT_MENU)
        elif len(self.perso.inventory) == 1:
            self.image = self.message.render(
                f"You have {len(self.perso.inventory)}/3"
                " item in your inventory",
                True, constants.COLOR_FONT_MENU)
        elif len(self.perso.inventory) > 1 and len(self.perso.inventory) < 3:
            self.image = self.message.render(
                f"You have {len(self.perso.inventory)}/3"
                "items in your inventory",
                True, constants.COLOR_FONT_MENU)
        elif len(self.perso.inventory) == 3:
            self.image = self.message.render(
                f"You can put the guard to sleep",
                True, constants.COLOR_FONT_MENU)

        return self.image
