import pygame as pg
import os
import sys

pg.mixer.pre_init(44100, -16, 1, 512)
pg.init()

def res(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


jump_sound = pg.mixer.Sound(res(r'Sounds\Rrr.wav'))
fall_sound = pg.mixer.Sound(res(r'Sounds\Bdish.wav'))
loss_sound = pg.mixer.Sound(res(r'Sounds\loss.wav'))
heart_plus_sound = pg.mixer.Sound(res(r'Sounds\hp+.wav'))
button_sound = pg.mixer.Sound(res(r'Sounds\button.wav'))
bullet_sound = pg.mixer.Sound(res(r'Sounds\shot.wav'))
pg.mixer.Sound.set_volume(jump_sound, 0.6)
pg.mixer.Sound.set_volume(fall_sound, 1)
pg.mixer.Sound.set_volume(loss_sound, 0.6)
pg.mixer.Sound.set_volume(heart_plus_sound, 0.5)
pg.mixer.Sound.set_volume(button_sound, 1)
pg.mixer.Sound.set_volume(bullet_sound, 1)
