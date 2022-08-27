import pygame as pg
import random
from game import *

#pg.mixer.pre_init(44100, -16, 1, 512)
#pg.init()

if __name__ == '__main__':
    new_game = Game()
    new_game.start()
    pg.quit()
