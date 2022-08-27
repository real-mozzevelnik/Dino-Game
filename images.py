import pygame as pg
import os
from sound import res

pg.init()

icon = pg.image.load(res(r'Backgrounds\icon.png')).convert_alpha()
menu_background = pg.image.load(res(r'Backgrounds\Menu.jpg')).convert()
land = [pg.image.load(res(r'Backgrounds\LandLevel.jpg')).convert(), pg.image.load(res(r'Backgrounds\LandMy.png')).convert(), pg.image.load(res(r'Backgrounds\Land2.jpg')).convert()]
cactus_img = [pg.image.load(res(r'Objects\Cactus0.png')).convert_alpha(), pg.image.load(res(r'Objects\Cactus1.png')).convert_alpha(), pg.image.load(res(r'Objects\Cactus2.png')).convert_alpha()]
stone_img = [pg.image.load(res(r'Objects\Stone0.png')).convert_alpha(), pg.image.load(res(r'Objects\Stone1.png')).convert_alpha()]
cloud_img = [pg.image.load(res(r'Objects\Cloud0.png')).convert_alpha(), pg.image.load(res(r'Objects\Cloud1.png')).convert_alpha()]
orange_dino_img = [pg.image.load(res(r'Dino\Dino0.png')).convert_alpha(), pg.image.load(res(r'Dino\Dino1.png')).convert_alpha(),
            pg.image.load(res(r'Dino\Dino2.png')).convert_alpha(), pg.image.load(res(r'Dino\Dino3.png')).convert_alpha(), pg.image.load(res(r'Dino\Dino4.png')).convert_alpha()]
purple_dino_img = [pg.image.load(res(r'Dino\Dino2_0.png')).convert_alpha(), pg.image.load(res(r'Dino\Dino2_1.png')).convert_alpha(), pg.image.load(res(r'Dino\Dino2_2.png')).convert_alpha(),
                   pg.image.load(res(r'Dino\Dino2_3.png')).convert_alpha(), pg.image.load(res(r'Dino\Dino2_4.png')).convert_alpha(), ]
health_img = pg.image.load(res(r'Effects\heart.png')).convert_alpha()
bullet_img = pg.image.load(res(r'Effects\shot.png')).convert_alpha()
bullet_img = pg.transform.scale(bullet_img, (30, 9))
health_img = pg.transform.scale(health_img, (30,30))
bird_img = [pg.image.load(res(r'Bird\Bird0.png')).convert_alpha(), pg.image.load(res(r'Bird\Bird1.png')).convert_alpha(), pg.image.load(res(r'Bird\Bird2.png')).convert_alpha(),
            pg.image.load(res(r'Bird\Bird3.png')).convert_alpha(),pg.image.load(res(r'Bird\Bird4.png')).convert_alpha(), pg.image.load(res(r'Bird\Bird5.png')).convert_alpha()]
light_img = [pg.image.load(res(r'Effects\Light0.png')).convert_alpha(), pg.image.load(res(r'Effects\Light1.png')).convert_alpha(), pg.image.load(res(r'Effects\Light2.png')).convert_alpha(),
             pg.image.load(res(r'Effects\Light3.png')).convert_alpha(), pg.image.load(res(r'Effects\Light4.png')).convert_alpha(), pg.image.load(res(r'Effects\Light5.png')).convert_alpha(),
             pg.image.load(res(r'Effects\Light6.png')).convert_alpha(), pg.image.load(res(r'Effects\Light7.png')).convert_alpha(), pg.image.load(res(r'Effects\Light8.png')).convert_alpha(),
             pg.image.load(res(r'Effects\Light9.png')).convert_alpha(), pg.image.load(res(r'Effects\Light10.png')).convert_alpha(), ]
double_jump_img = pg.image.load(res(r'Effects\Emerald.png')).convert_alpha()
double_jump_img = pg.transform.scale(double_jump_img, (30,30))
cactus_shoot_img = pg.image.load(res(r'Effects\Ruby.png')).convert_alpha()
cactus_shoot_img = pg.transform.scale(cactus_shoot_img, (30,30))
