'''
This module controls the background music 
of the game. In the text bar a small button allows you 
to activate or deactivate the sound of the game. 
By default it is disabled.
'''

import pygame
from config import constants


class MuteButton(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.click = 0
        self.image = self.mute()
        self.rect = self.image.get_rect()
        self.rect.topleft = (370, 450)

    def update(self):
        self.mute()

    def click_button(self):
        if self.click == 0:
            self.click = 1
        else:
            self.click = 0

    def mute(self):
        if self.click == 0:
            self.image = constants.load_image(constants.MUSIC_OFF, conv=False)
            pygame.mixer.music.pause()
            pygame.mixer.pause()
        else:
            self.image = constants.load_image(constants.MUSIC_ON, conv=False)
            pygame.mixer.music.unpause()
            pygame.mixer.unpause()
        return self.image
