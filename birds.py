import random
from sound import *
from bullet import *
from parameters import display
from images import *


class Bird:
    def __init__(self, away_y):
        self.x = random.randrange(550, 730)
        self.y = away_y
        self.width = 105
        self.height = 55
        self.ay = away_y
        self.speed = 3
        self.dest_y = self.speed * random.randrange(20, 70)
        self.img_counter = 0
        self.cooldown = 0
        self.come = True
        self.go_away = False
        self.cd_shoot = 0
        self.all_bullets = []
        self.ability = True

    def draw(self):
        if self.img_counter == 60:
            self.img_counter = 0

        display.blit(bird_img[self.img_counter//10], (self.x, self.y))
        self.img_counter += 1

        if self.come and self.cooldown == 0:
            return 1
                
        elif self.go_away:
            return 2

        elif self.cooldown > 0:
            self.cooldown -= 1
            
        return 0 

    def show(self):
        if self.y < self.dest_y:
            self.y += self.speed
        else:
            self.come = False
            #self.go_away = True
            self.dest_y = self.ay
            self.ability = True

    def hide(self):
        if self.y > self.dest_y:
            self.y -= self.speed
        else:
            self.come = True
            self.go_away = False
            self.x = random.randrange(400, 730)
            self.dest_y = self.speed * random.randrange(20, 70)
            self.cooldown = random.randrange(400, 1000)
            self.ability = False

    def check_damage(self, bullet):
        if self.x <= bullet.x <= self.x + self.width:
            if self.y <= bullet.y <= self.y + self.height:
                self.go_away = True
                return True

    def shoot(self):
        if not self.cd_shoot:
            new_bullet = Bullet(self.x, self.y)
            new_bullet.find_path(usr_x + usr_width//2, usr_y + usr_height//2)
            pg.mixer.Sound.play(bullet_sound)
            self.all_bullets.append(new_bullet)
            self.cd_shoot = 200
        else:
            self.cd_shoot -= 1

        for bullet in self.all_bullets:
            if not bullet.move_to(reverse=True):
                self.all_bullets.remove(bullet)
