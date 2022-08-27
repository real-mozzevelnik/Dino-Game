import pygame as pg
import random

pg.mixer.pre_init(44100, -16, 1, 512)
pg.init()

display_width = 800
display_height = 600

display = pg.display.set_mode((display_width, display_height))
pg.display.set_caption('Run, Dino! Run!')


jump_sound = pg.mixer.Sound(r'Sounds\Rrr.wav')
fall_sound = pg.mixer.Sound(r'Sounds\Bdish.wav')
loss_sound = pg.mixer.Sound(r'Sounds\loss.wav')
heart_plus_sound = pg.mixer.Sound(r'Sounds\hp+.wav')
button_sound = pg.mixer.Sound(r'Sounds\button.wav')
bullet_sound = pg.mixer.Sound(r'Sounds\shot.wav')
pg.mixer.Sound.set_volume(jump_sound, 0.6)
pg.mixer.Sound.set_volume(fall_sound, 1)
pg.mixer.Sound.set_volume(loss_sound, 0.6)
pg.mixer.Sound.set_volume(heart_plus_sound, 0.5)
pg.mixer.Sound.set_volume(button_sound, 1)
pg.mixer.Sound.set_volume(bullet_sound, 1)


icon = pg.image.load('Backgrounds\icon.png').convert_alpha()
pg.display.set_icon(icon)

menu_background = pg.image.load(r'Backgrounds\Menu.jpg').convert()
land = pg.image.load(r'Backgrounds\LandMy.png').convert()
cactus_img = [pg.image.load(r'Objects\Cactus0.png').convert_alpha(), pg.image.load(r'Objects\Cactus1.png').convert_alpha(), pg.image.load(r'Objects\Cactus2.png').convert_alpha()]
cactus_options = [69, 449, 37, 410, 40, 420]

stone_img = [pg.image.load(r'Objects\Stone0.png').convert_alpha(), pg.image.load(r'Objects\Stone1.png').convert_alpha()]
cloud_img = [pg.image.load(r'Objects\Cloud0.png').convert_alpha(), pg.image.load(r'Objects\Cloud1.png').convert_alpha()]

dino_img = [pg.image.load(r'Dino\Dino0.png').convert_alpha(), pg.image.load(r'Dino\Dino1.png').convert_alpha(),
            pg.image.load(r'Dino\Dino2.png').convert_alpha(), pg.image.load(r'Dino\Dino3.png').convert_alpha(), pg.image.load(r'Dino\Dino4.png').convert_alpha()]

health_img = pg.image.load(r'Effects\heart.png').convert_alpha()

bullet_img = pg.image.load(r'Effects\shot.png').convert_alpha()
bullet_img = pg.transform.scale(bullet_img, (30, 9))

health_img = pg.transform.scale(health_img, (30,30))

bird_img = [pg.image.load(r'Bird\Bird0.png').convert_alpha(), pg.image.load(r'Bird\Bird1.png').convert_alpha(), pg.image.load(r'Bird\Bird2.png').convert_alpha(),
            pg.image.load(r'Bird\Bird3.png').convert_alpha(),pg.image.load(r'Bird\Bird4.png').convert_alpha(), pg.image.load(r'Bird\Bird5.png').convert_alpha()]

light_img = [pg.image.load(r'Effects\Light0.png').convert_alpha(), pg.image.load(r'Effects\Light1.png').convert_alpha(), pg.image.load(r'Effects\Light2.png').convert_alpha(),
             pg.image.load(r'Effects\Light3.png').convert_alpha(), pg.image.load(r'Effects\Light4.png').convert_alpha(), pg.image.load(r'Effects\Light5.png').convert_alpha(),
             pg.image.load(r'Effects\Light6.png').convert_alpha(), pg.image.load(r'Effects\Light7.png').convert_alpha(), pg.image.load(r'Effects\Light8.png').convert_alpha(),
             pg.image.load(r'Effects\Light9.png').convert_alpha(), pg.image.load(r'Effects\Light10.png').convert_alpha(), ]


img_counter = 0
health = 2


class Object:
    def __init__(self, x, y, width, image, speed):
        self.x = x
        self.y = y
        self.width = width
        self.image = image
        self.speed = speed

    def move(self):
        if self.x >= -self.width:
            display.blit(self.image, (self.x, self.y))
            self.x -= self.speed
            return True
        else:
            return False

    def return_self(self, radius, y, width, image):
        self.x = radius
        self.y = y
        self.width = width
        self.image = image
        display.blit(self.image, (self.x, self.y))


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.active_color = (23, 204, 58)
        self.inactive_color = (13, 162, 58)
        self.draw_effects = False
        self.clear_effects = False
        self.rect_h = 10
        self.rect_w = width

    def draw(self, x, y, message, action=None, font_size=30):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            if click[0] == 1 and action is not None:
                if action==quit:
                    pg.mixer.Sound.play(button_sound)
                    pg.time.delay(300)
                    pg.quit()
                    exit()
                else:
                    pg.mixer.Sound.play(button_sound)
                    pg.time.delay(300)
                    action()                  

        self.draw_beautiful_rect(mouse[0],mouse[1],x,y)
        print_text(message=message, x=x+10, y=y+10, font_size=font_size, font_color=(178, 34, 34))

    def draw_beautiful_rect(self, ms_x, ms_y, x, y):
        if x <= ms_x <= x+self.width and y <= ms_y <= y+self.height:
            self.draw_effects = True
        if self.draw_effects:
            if ms_x <x or ms_x > x + self.width or ms_y < y or ms_y > y + self.height:
                    self.clear_effects = True
                    self.draw_effects = False
            if self.rect_h < self.height:
                self.rect_h += (self.height - 10)/40
        if self.clear_effects and not self.draw_effects:
            if self.rect_h > 10:
                self.rect_h -= (self.height - 10)/40
            else:
                self.clear_effects = False
            
        draw_y = y + self.height - self.rect_h
        pg.draw.rect(display, self.active_color, (x, draw_y, self.rect_w, self.rect_h))
            


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 8
        self.speed_y = 8
        self.desr_x = 0
        self.dest_y = 0

    def move(self):
        self.x += self.speed_x
        if self.x <= display_width:
            display.blit(bullet_img, (self.x, self.y))
            return True
        else:
            return False

    def find_path(self, dest_x, dest_y):
        self.dest_x = dest_x
        self.dest_y = dest_y

        delta_x = dest_x - self.x
        count_up = delta_x // self.speed_x
        
        if count_up == 0:
            count_up = 1
        if self.y >= dest_y:
            delta_y = self.y - dest_y
            self.speed_y = delta_y / count_up 
        else:
            delta_y = dest_y - self.y
            self.speed_y = -(delta_y / count_up)
            
        

    def move_to(self, reverse=False):
        if not reverse:
            self.x += self.speed_x
            self.y -= self.speed_y
        else:
            self.x -= self.speed_x
            self.y += self.speed_y
        if self.x <= display_width and self.y >= 0 and self.y <= display_height and self.dest_x >= usr_x and not reverse: ######
            display.blit(bullet_img, (self.x, self.y))
            return True
        elif self.x >= 0 and reverse:
            display.blit(bullet_img, (self.x, self.y))
            return True
        else:
            return False

        
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
            self.cooldown = random.randrange(400, 3000)
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
            
        

usr_width = 60
usr_height = 100
usr_x = display_width//3
usr_y = display_height - usr_height - 97

cactus_width = 20
cactus_height  = 70
cactus_x = display_width - 50
cactus_y = display_height - cactus_height - 100

clock = pg.time.Clock()

make_jump = False
jump_counter = 30

scores = 0
max_scores = 0
max_above = 0

cooldown = 0

mouse_counter = 0
need_draw_click = False


def show_menu():

    start_button = Button(288, 70)
    quit_button = Button(120, 70)

    pg.mixer.music.load(r'Sounds\Big_Slinker.mp3')
    pg.mixer.music.set_volume(0.5)
    pg.mixer.music.play(-1)
    
    show = True
    while show:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()

        display.blit(menu_background, (0, 0))
        start_button.draw(270, 200, 'start game', start_game, font_size=50)
        quit_button.draw(358, 300, 'quit', quit, 50)

        draw_mouse()

        pg.display.update()
        clock.tick(60)


def start_game():
    global scores, make_jump, jump_counter, usr_y, health, cooldown
    scores = 0
    make_jump = False
    jump_counter = 30
    usr_y = display_height - usr_height - 97
    health = 2
    cooldown = 0

    pg.mixer.music.load(r'Sounds\background.mp3')
    pg.mixer.music.set_volume(0.25)
    
    while game_cycle():
        scores = 0
        make_jump = False
        jump_counter = 30
        usr_y = display_height - usr_height - 97
        health = 2
        cooldown = 0
        


def game_cycle():
    global make_jump, cooldown

    pg.mixer.music.play(-1)
    
    game = True
    cactus_arr = []
    create_cactus_arr(cactus_arr)

    stone, stone1, cloud = open_random_objects()
    heart = Object(display_width, 280, 30, health_img, 4)
    all_bullets = []
    all_mouse_bullets = []

    bird1 = Bird(-90) ######
    bird2 = Bird(-100)

    all_birds = [bird1, bird2]

    while game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()

        keys = pg.key.get_pressed()
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        
        if keys[pg.K_SPACE]:
            make_jump = True

        elif keys[pg.K_ESCAPE]:
            pause()


        if make_jump:
            jump()

        count_scores(cactus_arr)

        display.blit(land, (0,0))
        
        draw_array(cactus_arr)
        move_objects(stone, stone1, cloud)

        draw_birds(all_birds)
        check_birds_damage(all_mouse_bullets, all_birds)
        
        print_text(f'Score: {scores}', 600, 10)
        draw_dino()

        if not cooldown:
            if keys[pg.K_x]:
                pg.mixer.Sound.play(bullet_sound)
                all_bullets.append(Bullet(usr_x + usr_width, usr_y + 26))
                cooldown = 50
            elif click[0] and mouse[0]>=usr_x: ######
                pg.mixer.Sound.play(bullet_sound)
                add_bullet = Bullet(usr_x + usr_width, usr_y + 26)
                add_bullet.find_path(mouse[0], mouse[1])
                all_mouse_bullets.append(add_bullet)
                cooldown = 50
        else:
            print_text(f'Cooldown time: {cooldown//10}', 482, 40) #delete if its not beauty (actually, it isn't)
            cooldown -= 1

        for bullet in all_bullets:
            if not bullet.move():
                all_bullets.remove(bullet)

        for bullet in all_mouse_bullets:
            if not bullet.move_to():
                all_mouse_bullets.remove(bullet)

        if check_collision(cactus_arr) or check_birds_attack(all_birds):
            pg.mixer.music.stop()
            game = False

        show_health()
        heart.move()
        hearts_plus(heart)

        draw_mouse()
        
        pg.display.update()
        clock.tick(60)
    return game_over()


def jump():
    global usr_y, make_jump, jump_counter
    
    if jump_counter >= -30:
        if jump_counter == 30:
            pg.mixer.Sound.play(jump_sound)
        usr_y -= jump_counter / 2.5
        jump_counter -= 1
        if jump_counter == -30:
            pg.mixer.Sound.play(fall_sound)
    else:
        jump_counter = 30
        make_jump = False

        
def create_cactus_arr(array):

    choice = random.randrange(0,3)
    img = cactus_img[choice]
    width = cactus_options[choice*2]
    height = cactus_options[choice*2+1]
    array.append(Object(display_width + 20, height, width, img, 4))

    choice = random.randrange(0,3)
    img = cactus_img[choice]
    width = cactus_options[choice*2]
    height = cactus_options[choice*2+1]
    array.append(Object(display_width + 300, height, width, img, 4))

    choice = random.randrange(0,3)
    img = cactus_img[choice]
    width = cactus_options[choice*2]
    height = cactus_options[choice*2+1]
    array.append(Object(display_width + 600, height, width, img, 4))

    

def find_radius(array):
    maximum = max(array[0].x, array[1].x, array[2].x)

    if maximum <display_width:
        radius = display_width
        if radius - maximum < 50:
            radius += 280
    else:
        radius = maximum

    choice = random.randrange(0, 5)
    if choice == 0:
        radius += random.randrange(35,36)
    else:
        radius += random.randrange(250, 400)
    return radius
    

def draw_array(array):
    for cactus in array:
        check = cactus.move()
        if not check:
            object_return(array, cactus)


def object_return(objects, obj):
    radius = find_radius(objects)
    choice = random.randrange(0,3)
    img = cactus_img[choice]
    width = cactus_options[choice*2]
    height = cactus_options[choice*2+1] 
            
    obj.return_self(radius, height, width, img)


def open_random_objects():
    choice = random.randrange(0,2)
    img_of_stone = stone_img[choice]
    
    choice = random.randrange(0,2)
    img_of_cloud = cloud_img[choice]

    stone = Object(display_width, display_height - 80, 10, img_of_stone, 4)
    stone1 = Object(display_width+300, display_height - 20, 10, img_of_stone, 4)
    cloud = Object(display_width, 80, 70, img_of_cloud, 2)

    return stone, stone1, cloud
    

def move_objects(stone, stone1, cloud):
    check = stone.move()
    if not check:
        choice = random.randrange(0,2)
        img_of_stone = stone_img[choice]
        stone.return_self(display_width, 500+random.randrange(10,80), stone.width, img_of_stone)

    check = stone1.move()
    if not check:
        choice = random.randrange(0,2)
        img_of_stone = stone_img[choice]
        stone1.return_self(display_width+random.randrange(150,400), 500+random.randrange(10,80), stone.width, img_of_stone)
        
    check = cloud.move()
    if not check:
        choice = random.randrange(0,2)
        img_of_cloud = cloud_img[choice]
        cloud.return_self(display_width, random.randrange(10,200), cloud.width, img_of_cloud)


def draw_dino():
    global img_counter
    if img_counter == 25:
        img_counter = 0
    display.blit(dino_img[img_counter//5], (usr_x, usr_y))
    img_counter += 1


def print_text(message, x, y, font_color = (0,0,0), font_type = 'Effects\PingPong.ttf', font_size = 30):
    font = pg.font.Font(font_type,font_size)
    text = font.render(message, True, font_color)
    display.blit(text, (x,y))

        
def pause():
    paused = True
    pg.mixer.music.pause()
    while paused:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()

        print_text('Paused, Press Enter to continue', 160, 300)

        keys = pg.key.get_pressed()
        if keys[pg.K_RETURN]:
            paused = False

        pg.display.update()
        clock.tick(15)
    pg.mixer.music.unpause()


def check_collision(barriers):
    for barrier in barriers:
        if barrier.y == 449: #little cactus
            if not make_jump:
                if barrier.x <= usr_x + usr_width - 30 <= barrier.x + barrier.width:
                    if check_health():
                        object_return(barriers, barrier)
                        return False
                    else:
                        return True
            elif jump_counter >= 0:
                if usr_y + usr_height - 5 >= barrier.y:
                    if barrier.x <= usr_x + usr_width - 30 <= barrier.x + barrier.width:
                        if check_health():
                            object_return(barriers, barrier)
                            return False
                        else:
                            return True
            else:
                if usr_y + usr_height - 10 >= barrier.y:
                    if barrier.x <= usr_x <= barrier.x + barrier.width:
                        if check_health():
                            object_return(barriers, barrier)
                            return False
                        else:
                            return True
        else:
            if not make_jump:
                if barrier.x <= usr_x + usr_width - 5 <= barrier.x + barrier.width:
                    if check_health():
                        object_return(barriers, barrier)
                        return False
                    else:
                        return True
            elif jump_counter == 10:
                if usr_y + usr_height - 5 >= barrier.y:
                    if barrier.x <= usr_x + usr_width - 5 <= barrier.x + barrier.width:
                        if check_health():
                            object_return(barriers, barrier)
                            return False
                        else:
                            return True
            elif jump_counter >= -1:
                if usr_y + usr_height - 5 >= barrier.y:
                    if barrier.x <= usr_x +usr_width - 35 <= barrier.x + barrier.width:
                        if check_health():
                            object_return(barriers, barrier)
                            return False
                        else:
                            return True
                else:
                    if usr_y + usr_height - 10 >= barrier.y :
                        if barrier.x <= usr_x <= barrier.x + barrier.width:
                            if check_health():
                                object_return(barriers, barrier)
                                return False
                            else:
                                return True
            elif usr_y + usr_height >= barrier.y :
                if barrier.x <= usr_x <= barrier.x + barrier.width:
                    if check_health():
                        object_return(barriers, barrier)
                        return False
                    else:
                        return True
    return False


def count_scores(barriers):
    global scores, max_above
    above_cactus = 0
    if -20 <= jump_counter < 25:
        for barrier in barriers:
            if usr_y + usr_height - 5 <= barrier.y:
                if barrier.x <= usr_x <= barrier.x + barrier.width:
                    above_cactus += 1
                elif barrier.x <= usr_x + usr_width <= barrier.x + barrier.width:
                    above_cactus += 1
        max_above = max(max_above, above_cactus)
    else:
        if jump_counter == -30:
            scores += max_above
            max_above = 0
        
def game_over():
    global max_scores
    if scores > max_scores:
        max_scores = scores
    
    stopped = True
    while stopped:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()

        print_text('Game Over, Press enter to play again, esc to exit', 45, 300)
        print_text(f'Max score: {max_scores}', 300, 350)

        keys = pg.key.get_pressed()
        if keys[pg.K_RETURN]:
            pg.mixer.music.play(-1)
            return True
            


        if keys[pg.K_ESCAPE]:
            pg.mixer.music.load(r'Sounds\Big_Slinker.mp3')
            pg.mixer.music.set_volume(0.5)
            pg.mixer.music.play(-1)
            return False
            

        pg.display.update()
        clock.tick(15)
    

def show_health():
    global health
    show = 0
    x = 20
    while show != health:
        display.blit(health_img, (x ,20))
        x += 40
        show += 1


def check_health():
    global health
    health -= 1
    if health == 0:
        pg.mixer.Sound.play(loss_sound)
        return False
    else:
        pg.mixer.Sound.play(fall_sound)
        return True

def hearts_plus(heart):
    global health

    if heart.x <= -heart.width:
        radius = display_width + random.randrange(1000, 2000)
        heart.return_self(radius, random.randrange(260, 450), heart.width, health_img)
    
    if usr_x <= heart.x <= usr_x + usr_width:
        if usr_y <= heart.y <= usr_y + usr_height:
            pg.mixer.Sound.play(heart_plus_sound)
            if health < 5:
                health += 1
            radius = display_width + random.randrange(1000, 2000)

            heart.return_self(radius, random.randrange(260, 450), heart.width, health_img)


def draw_birds(birds):
    for bird in birds:
        action = bird.draw()
        if action == 1:
            bird.show()
        elif action == 2:
            bird.hide()
        else:
            if bird.y >= 0 and bird.ability:
                bird.shoot()


def check_birds_damage(bullets, birds):
    for bird in birds:
        for bullet in bullets:
            if bird.check_damage(bullet):
                bullets.remove(bullet)


def check_birds_attack(birds):
    for bird in birds:
        for bullet in bird.all_bullets:
            if usr_x <= bullet.x <= usr_x + usr_width:
                if usr_y <= bullet.y <= usr_y + usr_height:
                    bird.all_bullets.remove(bullet)
                    if check_health():
                        return False
                    else:
                        return True
                    
def draw_mouse():
    global mouse_counter, need_draw_click
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    mouse_size = [10,12,16,20,28,34,40,45,48,54,58]
    
    if click[0] or click[1]:
        need_draw_click = True
    if need_draw_click:
        draw_x = mouse[0] - mouse_size[mouse_counter]//2
        draw_y = mouse[1] - mouse_size[mouse_counter]//2
        display.blit(light_img[mouse_counter], (draw_x, draw_y))
        mouse_counter += 1
        if mouse_counter == 10:
            mouse_counter = 0
            need_draw_click = False


show_menu()
pg.quit()

