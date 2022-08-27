from parameters import display
from parameters import clock
from bullet import *
from button import *
from birds import *
from object import *
from effect import *
from images import *
from states import *
from save import *


class Game():
    def __init__(self):

        pg.display.set_icon(icon)
        pg.display.set_caption('Run, Dino! Run!')

        self.cactus_options = [69, 449, 37, 410, 40, 420]
        self.img_counter = 0
        self.health = 2
        self.double_jump = 1#emeralds
        self.cactus_shoot = 1#ruby
        self.make_jump = False
        self.jump_counter = 30
        self.jump_num = 0#double jumps only
        self.scores = 0
        self.max_scores = 0
        self.max_above = 0
        self.cooldown = 0
        self.game_state = GameState()
        self.save_data = Save()
        self.land = 0
        self.dino = 1

    def start(self):
        while True:
            if self.game_state.check(State.MENU):
                self.save_data.add('max', max(self.save_data.get_scores('max'),self.max_scores))
                self.max_scores = self.save_data.get_scores('max')
                self.land = self.save_data.get_land('land')
                self.dino = self.save_data.get_hero('hero')
                self.show_menu()
            elif self.game_state.check(State.START):
                self.max_scores = 0
                self.save_data.add('max', self.max_scores)
                self.start_game()
            elif self.game_state.check(State.CONTINUE):
                self.start_game()
            elif self.game_state.check(State.CHOOSE_THEME):
                self.choose_theme()
            elif self.game_state.check(State.CHOOSE_HERO):
                self.choose_hero()
            elif self.game_state.check(State.HOW_TO_PLAY):
                self.how_to_play()
            elif self.game_state.check(State.QUIT):
                break

    def show_menu(self):
        start_button = Button(242, 70)
        continue_button = Button(222, 70)
        choose_theme_button = Button(342, 70)
        choose_hero_button = Button(315, 70)
        how_to_play_button = Button(325, 70)
        quit_button = Button(120, 70)

        pg.mixer.music.load(res(r'Sounds\Big_Slinker.mp3'))
        pg.mixer.music.set_volume(0.5)
        pg.mixer.music.play(-1)
        
        show = True
        while show:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    pg.quit()
                    quit()

            display.blit(menu_background, (0, 0))
            if start_button.draw(290, 200, 'new game', font_size=50):    
                self.game_state.change(State.START)
                return
            if continue_button.draw(300, 300, 'continue', font_size=50):
                self.game_state.change(State.CONTINUE)
                return
            if choose_theme_button.draw(50, 400, 'choose theme', font_size=50):
                self.game_state.change(State.CHOOSE_THEME)
                return
            if choose_hero_button.draw(450, 400, 'choose hero', font_size=50):
                self.game_state.change(State.CHOOSE_HERO)
                return
            if how_to_play_button.draw(450, 500, 'how to play', font_size=50):
                self.game_state.change(State.HOW_TO_PLAY)
                return
            if quit_button.draw(150, 500, 'quit', font_size=50):
                self.game_state.change(State.QUIT)
                return

            draw_mouse()

            pg.display.update()
            clock.tick(60)

    def start_game(self):
        #global scores, make_jump, jump_counter, usr_y, health, cooldown
        self.scores = 0
        self.make_jump = False
        self.jump_counter = 30
        self.jump_num = 0
        p.usr_y = p.display_height - p.usr_height - 97
        self.health = 2
        self.double_jump = 1
        self.cactus_shoot = 1
        self.cooldown = 0

        pg.mixer.music.load(res(r'Sounds\background.mp3'))
        pg.mixer.music.set_volume(0.25)
        
        while self.game_cycle():
            self.scores = 0
            self.make_jump = False
            self.jump_counter = 30
            self.jump_num = 0
            p.usr_y = p.display_height - p.usr_height - 97
            self.health = 2
            self.double_jump = 1
            self.cactus_shoot = 1
            self.cooldown = 0

    def choose_theme(self):
        theme_1 = Button(180, 70)
        theme_2 = Button(185, 70)
        theme_3 = Button(140, 70)
        back = Button(120, 70)
        end = False
        while not end:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
            display.blit(menu_background, (0, 0))
            if theme_1.draw(310, 200, 'Classic', font_size = 50):
                self.land = 0
                self.save_data.add('land', self.land)
                return
            if theme_2.draw(305, 300, 'Dessert', font_size = 50):
                self.land = 1
                self.save_data.add('land', self.land)
                return
            if theme_3.draw(330, 400, 'Night', font_size = 50):
                self.land = 2
                self.save_data.add('land', self.land)
                return
            if back.draw(340, 500, 'Back', font_size = 50):
                self.game_state.change(State.MENU)
                return

            draw_mouse()

            pg.display.update()
            clock.tick(60)

    
    def choose_hero(self):
        hero_1 = Button(310, 70)
        hero_2 = Button(285, 70)
        back = Button(120, 70)
        end = False
        while not end:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
            display.blit(menu_background, (0, 0))
            if hero_1.draw(245, 200, 'Orange dino', font_size = 50):
                self.dino = 1
                self.save_data.add('hero', self.dino)
                return
            if hero_2.draw(255, 300, 'purple dino', font_size = 50):
                self.dino = 2
                self.save_data.add('hero', self.dino)
                return
            if back.draw(340, 400, 'Back', font_size = 50):
                self.game_state.change(State.MENU)
                return

            draw_mouse()

            pg.display.update()
            clock.tick(60)

    def how_to_play(self):
        back = Button(120, 70)
        end = False
        while not end:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
            display.blit(menu_background, (0, 0))
            print_text('mouse - shoot the birds', 50, 200, font_size=40, font_color=(178,34,34))
            print_text('Collect emerald\'s for double jumps', 50, 250, font_size=40, font_color=(178,34,34))
            print_text('Collect ruby\'s for shooting cactuses', 50, 300, font_size=40, font_color=(178,34,34))
            print_text('"x" - shoot the cactus', 50, 350, font_size=40, font_color=(178,34,34))
            print_text('ESC - pause', 50, 400, font_size=40, font_color=(178,34,34))
            if back.draw(340, 500, 'Back', font_size = 50):
                self.game_state.change(State.MENU)
                return

            draw_mouse()

            pg.display.update()
            clock.tick(60)


    
                    
            

    def game_cycle(self):
        pg.mixer.music.play(-1)
        
        game = True
        cactus_arr = []
        self.create_cactus_arr(cactus_arr)

        stone, stone1, cloud = self.open_random_objects()
        heart = Object(display_width, 280, 30, health_img, 4)
        emerald = Object(display_width*5, 280, 30, double_jump_img, 4)
        ruby = Object(display_width*10, 270, 30, cactus_shoot_img, 4)
        
        all_bullets = []
        all_mouse_bullets = []

        bird1 = Bird(-90) 

        all_birds = [bird1]

        while game:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game = False  ###game/running!!!
                    pg.quit()

            keys = pg.key.get_pressed()
            mouse = pg.mouse.get_pos()
            click = pg.mouse.get_pressed()
            
            if keys[pg.K_SPACE]:
                self.make_jump = True
                if self.jump_counter < 24 and self.double_jump>0:
                    if self.jump_num < 2:
                        self.jump_num += 1
                        self.jump_counter = 30
                        if self.jump_num == 2:
                            self.double_jump -= 1

            elif keys[pg.K_ESCAPE]:
                self.pause()


            if self.make_jump:
                self.jump()

            self.count_scores(cactus_arr)

            display.blit(land[self.land], (0,0))
            
            self.draw_array(cactus_arr)
            self.move_objects(stone, stone1, cloud)

            self.draw_birds(all_birds)
            self.check_birds_damage(all_mouse_bullets, all_birds)
            self.check_cactus_shoot(all_bullets, cactus_arr)
            
            print_text(f'Score: {self.scores}', 600, 10)
            
            self.draw_dino()

            if not self.cooldown:
                if keys[pg.K_x] and self.cactus_shoot > 0:
                    pg.mixer.Sound.play(bullet_sound)
                    all_bullets.append(Bullet(p.usr_x + p.usr_width, p.usr_y + 26))
                    self.cooldown = 50
                    self.cactus_shoot -= 1
                elif click[0] and mouse[0]>=usr_x: ######
                    pg.mixer.Sound.play(bullet_sound)
                    add_bullet = Bullet(p.usr_x + p.usr_width, p.usr_y + 26)
                    add_bullet.find_path(mouse[0], mouse[1])
                    all_mouse_bullets.append(add_bullet)
                    self.cooldown = 50
            else:
                print_text(f'Cooldown time: {self.cooldown//10}', 482, 40) #delete if its not beauty (actually, it isn't)
                self.cooldown -= 1

            for bullet in all_bullets:
                if not bullet.move():
                    all_bullets.remove(bullet)

            for bullet in all_mouse_bullets:
                if not bullet.move_to():
                    all_mouse_bullets.remove(bullet)

            if self.check_collision(cactus_arr) or self.check_birds_attack(all_birds):
                pg.mixer.music.stop()
                game = False

            self.show_health()
            heart.move()
            self.hearts_plus(heart)

            self.show_emerald()
            emerald.move()
            self.emerald_plus(emerald)

            self.show_ruby()
            ruby.move()
            self.ruby_plus(ruby)

            draw_mouse()
            
            pg.display.update()
            clock.tick(60)
            
        return self.game_over()

    def jump(self):
        if self.jump_counter >= -30:
            if self.jump_counter == 30:
                pg.mixer.Sound.play(jump_sound)
            p.usr_y -= self.jump_counter / 2.5
            self.jump_counter -= 1
            if self.jump_counter == -30:
                pg.mixer.Sound.play(fall_sound)
        else:
            if p.usr_y < 403:
                p.usr_y = min(403, p.usr_y - self.jump_counter / 2.5)
                
                self.jump_counter -= 1
            else:
                self.jump_num = 0
                self.jump_counter = 30
                self.make_jump = False

    def create_cactus_arr(self, array):
        choice = random.randrange(0,3)
        img = cactus_img[choice]
        width = self.cactus_options[choice*2]
        height = self.cactus_options[choice*2+1]
        array.append(Object(p.display_width + 20, height, width, img, 4))

        choice = random.randrange(0,3)
        img = cactus_img[choice]
        width = self.cactus_options[choice*2]
        height = self.cactus_options[choice*2+1]
        array.append(Object(p.display_width + 300, height, width, img, 4))

        choice = random.randrange(0,3)
        img = cactus_img[choice]
        width = self.cactus_options[choice*2]
        height = self.cactus_options[choice*2+1]
        array.append(Object(p.display_width + 600, height, width, img, 4))

    @staticmethod ###???
    def find_radius(array):
        maximum = max(array[0].x, array[1].x, array[2].x)

        if maximum < p.display_width:
            radius = p.display_width
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

    def draw_array(self, array):
        for cactus in array:
            check = cactus.move()
            if not check:
                self.object_return(array, cactus)

    def object_return(self, objects, obj):
        radius = self.find_radius(objects)
        choice = random.randrange(0,3)
        img = cactus_img[choice]
        width = self.cactus_options[choice*2]
        height = self.cactus_options[choice*2+1] 
                
        obj.return_self(radius, height, width, img)

    @staticmethod
    def open_random_objects():
        choice = random.randrange(0,2)
        img_of_stone = stone_img[choice]
        
        choice = random.randrange(0,2)
        img_of_cloud = cloud_img[choice]

        stone = Object(p.display_width, p.display_height - 80, 10, img_of_stone, 4)
        stone1 = Object(p.display_width+300, p.display_height - 20, 10, img_of_stone, 4)
        cloud = Object(p.display_width, 80, 70, img_of_cloud, 2)

        return stone, stone1, cloud

    @staticmethod
    def move_objects(stone, stone1, cloud):
        check = stone.move()
        if not check:
            choice = random.randrange(0,2)
            img_of_stone = stone_img[choice]
            stone.return_self(p.display_width, 500+random.randrange(10,80), stone.width, img_of_stone)

        check = stone1.move()
        if not check:
            choice = random.randrange(0,2)
            img_of_stone = stone_img[choice]
            stone1.return_self(p.display_width+random.randrange(150,400), 500+random.randrange(10,80), stone.width, img_of_stone)
            
        check = cloud.move()
        if not check:
            choice = random.randrange(0,2)
            img_of_cloud = cloud_img[choice]
            cloud.return_self(p.display_width, random.randrange(10,200), cloud.width, img_of_cloud)

    def draw_dino(self):
        if self.img_counter == 25:
            self.img_counter = 0
        if self.dino == 1:
            dino = orange_dino_img
        elif self.dino == 2:
            dino = purple_dino_img
        display.blit(dino[self.img_counter//5], (p.usr_x, p.usr_y))
        self.img_counter += 1

    @staticmethod
    def pause():
        paused = True
        pg.mixer.music.pause()
        while paused:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game = False   ###game/running???
                    pg.quit()
                    quit()

            print_text('Paused, Press Enter to continue', 160, 300)

            keys = pg.key.get_pressed()
            if keys[pg.K_RETURN]:
                paused = False

            pg.display.update()
            clock.tick(15)
        pg.mixer.music.unpause()

    def check_collision(self, barriers):
        for barrier in barriers:
            if barrier.y == 449: #little cactus
                if not self.make_jump:
                    if barrier.x <= p.usr_x + p.usr_width - 30 <= barrier.x + barrier.width:
                        if self.check_health():
                            self.object_return(barriers, barrier)
                            return False
                        else:
                            return True
                elif self.jump_counter >= 0:
                    if p.usr_y + p.usr_height - 5 >= barrier.y:
                        if barrier.x <= p.usr_x + p.usr_width - 30 <= barrier.x + barrier.width:
                            if self.check_health():
                                self.object_return(barriers, barrier)
                                return False
                            else:
                                return True
                else:
                    if p.usr_y + p.usr_height - 10 >= barrier.y:
                        if barrier.x <= p.usr_x <= barrier.x + barrier.width:
                            if self.check_health():
                                self.object_return(barriers, barrier)
                                return False
                            else:
                                return True
            else:
                if not self.make_jump:
                    if barrier.x <= p.usr_x + p.usr_width - 5 <= barrier.x + barrier.width:
                        if self.check_health():
                            self.object_return(barriers, barrier)
                            return False
                        else:
                            return True
                elif self.jump_counter == 10:
                    if p.usr_y + p.usr_height - 5 >= barrier.y:
                        if barrier.x <= p.usr_x + p.usr_width - 5 <= barrier.x + barrier.width:
                            if self.check_health():
                                self.object_return(barriers, barrier)
                                return False
                            else:
                                return True
                elif self.jump_counter >= -1:
                    if p.usr_y + p.usr_height - 5 >= barrier.y:
                        if barrier.x <= p.usr_x + p.usr_width - 35 <= barrier.x + barrier.width:
                            if self.check_health():
                                self.object_return(barriers, barrier)
                                return False
                            else:
                                return True
                    else:
                        if p.usr_y + p.usr_height - 10 >= barrier.y :
                            if barrier.x <= p.usr_x <= barrier.x + barrier.width:
                                if self.check_health():
                                    self.object_return(barriers, barrier)
                                    return False
                                else:
                                    return True
                elif p.usr_y + p.usr_height >= barrier.y :
                    if barrier.x <= p.usr_x <= barrier.x + barrier.width:
                        if self.check_health():
                            self.object_return(barriers, barrier)
                            return False
                        else:
                            return True
        return False

    def count_scores(self, barriers):
        above_cactus = 0
        if -20 <= self.jump_counter < 25:
            for barrier in barriers:
                if p.usr_y + p.usr_height - 5 <= barrier.y:
                    if barrier.x <= p.usr_x <= barrier.x + barrier.width:
                        above_cactus += 1
                    elif barrier.x <= p.usr_x + p.usr_width <= barrier.x + barrier.width:
                        above_cactus += 1
            self.max_above = max(self.max_above, above_cactus)
        else:
            if self.jump_counter == -30:
                self.scores += self.max_above
                self.max_above = 0

    def game_over(self):
        if self.scores > self.max_scores:
            self.max_scores = self.scores
        
        stopped = True
        while stopped:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game = False
                    pg.quit()
                    quit()

            print_text('Game Over, Press enter to play again, esc to exit', 45, 300)
            print_text(f'Max score: {self.max_scores}', 300, 350)

            keys = pg.key.get_pressed()
            if keys[pg.K_RETURN]:
                pg.mixer.music.play(-1)
                return True
                
            if keys[pg.K_ESCAPE]:
                pg.mixer.music.load(res(r'Sounds\Big_Slinker.mp3'))
                pg.mixer.music.set_volume(0.5)
                pg.mixer.music.play(-1)
                self.game_state.change(State.MENU)
                return False
                
            pg.display.update()
            clock.tick(15)

    def show_health(self):
        show = 0
        x = 20
        while show != self.health:
            display.blit(health_img, (x ,20))
            x += 40
            show += 1

    def check_health(self):
        self.health -= 1
        if self.health == 0:
            pg.mixer.Sound.play(loss_sound)
            return False
        else:
            pg.mixer.Sound.play(fall_sound)
            return True

    def hearts_plus(self, heart):
        if heart.x <= -heart.width:
            radius = p.display_width + random.randrange(2000, 4000)
            heart.return_self(radius, random.randrange(260, 450), heart.width, health_img)
        
        if p.usr_x <= heart.x <= p.usr_x + p.usr_width or p.usr_x <= heart.x+30 <= p.usr_x + p.usr_width:
            if p.usr_y <= heart.y <= p.usr_y + p.usr_height or p.usr_y <= heart.y+30 <= p.usr_y + p.usr_height:
                pg.mixer.Sound.play(heart_plus_sound)
                if self.health < 5:
                    self.health += 1
                radius = p.display_width + random.randrange(4000, 6000)

                heart.return_self(radius, random.randrange(260, 450), heart.width, health_img)

    @staticmethod
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

    @staticmethod
    def check_birds_damage(bullets, birds):
        for bird in birds:
            for bullet in bullets:
                if bird.check_damage(bullet):
                    bullets.remove(bullet)

    def check_birds_attack(self, birds):
        for bird in birds:
            for bullet in bird.all_bullets:
                if p.usr_x <= bullet.x <= p.usr_x + p.usr_width:
                    if p.usr_y <= bullet.y <= p.usr_y + p.usr_height:
                        bird.all_bullets.remove(bullet)
                        if self.check_health():
                            return False
                        else:
                            return True

    def show_emerald(self):
        show = 0
        x = 20
        while show != self.double_jump:
            display.blit(double_jump_img, (x ,50))
            x += 40
            show += 1

    def emerald_plus(self, emerald):
        if emerald.x <= -emerald.width:
            radius = p.display_width + random.randrange(2000, 4000)
            emerald.return_self(radius, random.randrange(260, 450), emerald.width, double_jump_img)
            
        if p.usr_x <= emerald.x <= p.usr_x + p.usr_width or p.usr_x <= emerald.x+30 <= p.usr_x + p.usr_width:
            if p.usr_y <= emerald.y <= p.usr_y + p.usr_height or p.usr_y <= emerald.y+30 <= p.usr_y + p.usr_height:
                pg.mixer.Sound.play(heart_plus_sound)
                if self.double_jump < 3:
                    self.double_jump += 1
                radius = p.display_width + random.randrange(4000, 6000)

                emerald.return_self(radius, random.randrange(260, 450), emerald.width, double_jump_img)

    def show_ruby(self):
        show = 0
        x = 20
        while show != self.cactus_shoot:
            display.blit(cactus_shoot_img, (x ,80))
            x += 40
            show += 1

    def ruby_plus(self, ruby):
        if ruby.x <= -ruby.width:
            radius = p.display_width + random.randrange(2000, 4000)
            ruby.return_self(radius, random.randrange(260, 450), ruby.width, cactus_shoot_img)
            
        if p.usr_x <= ruby.x <= p.usr_x + p.usr_width or p.usr_x <= ruby.x+30 <= p.usr_x + p.usr_width:
            if p.usr_y <= ruby.y <= p.usr_y + p.usr_height or p.usr_y <= ruby.y+30 <= p.usr_y + p.usr_height:
                pg.mixer.Sound.play(heart_plus_sound)
                if self.cactus_shoot < 3:
                    self.cactus_shoot += 1
                radius = p.display_width + random.randrange(4000, 6000)

                ruby.return_self(radius, random.randrange(260, 450), ruby.width, cactus_shoot_img)

    def check_cactus_shoot(self, bullets, cactuses):
        for cactus in cactuses:
            for bullet in bullets:
                if cactus.y < bullet.y:
                    if cactus.x < bullet.x < cactus.x + cactus.width:
                        self.object_return(cactuses, cactus)
                        bullets.remove(bullet)
                        
                        



            



            



                            







            

            


    






    


    
