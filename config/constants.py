'''
 Contains all game constants, parameters and main functions of the program
'''
import os
import pygame
from pygame.compat import geterror

pygame.init()


def load_sound(name, music=True):
    '''Functions to create  musical resources'''
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join('data', 'sound', name)
    if music == True:
        try:
            sound = pygame.mixer.music.load(fullname)
        except pygame.error:
            print('Cannot load sound: %s' % fullname)
            raise SystemExit(str(geterror()))
    else:
        try:
            sound = pygame.mixer.Sound(fullname)
        except pygame.error:
            print('Cannot load sound: %s' % fullname)
            raise SystemExit(str(geterror()))
    return sound


def load_image(name, conv=True, colorkey=None):
    '''Functions to create  visual resources'''
    fullname = os.path.join('data', 'images', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print('Cannot load image:', fullname)
        raise SystemExit(str(geterror()))
    if conv == True:
        image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


# Read file
START_CHAR = 'M'
ARRIVAL_CHAR = 'A'
GATES_CHAR = "#"
WALL_CHAR = "X"
OBJ_CHAR = "O"

# Representation
START_REP = 'M'
CHAR_REP = "M"
ARRIVAL_REP = 'A'
GATES_REP = " "
WALL_REP = "X"
OBJ_REP = "O"

# Game Element
FPS = 60

# Size elements
SIZE_SPRITE = 30
SIZE_SCREEN_WIDTH = 450
SIZE_SCREEN_HEIGHT = 500
SIZE_MENU_HEIGHT = 50
SIZE_MENU_WIDTH = 450


# Image elements
MAZE_1 = os.path.join('data', 'mazes', 'labyrinth1.txt')
MAZE_2 = os.path.join('data', 'mazes', 'labyrinth2.txt')
CHARACTER = 'MacGyver.png'
WALL = 'block.png'
SYRINGE = 'syringe.png'
ETHER = 'ether.png'
TUBE = 'tube.png'
GUARD = 'guard.png'
NAME_GAME = "McGyver Maze"
BACKGROUND = "background.png"

# Font elements
MENU = "menu.png"
FONT_GAME = "Chalkboard.ttc"
SIZE_FONT_MENU = 17
COLOR_FONT_MENU = (0, 0, 0)

# Sound element
BACKGROUND_MUSIC = 'music.wav'
DROP_SOUND = 'drop.ogg'
WIN_SOUND = 'win.ogg'
LOSE_SOUND = 'lose.ogg'
VOLUME = 0.2
MUSIC_OFF = 'musicOff.png'
MUSIC_ON = 'musicOn.png'
