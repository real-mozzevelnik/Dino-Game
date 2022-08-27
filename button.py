from sound import *
from effect import *
from parameters import display


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
            if click[0] == 1:
                pg.mixer.Sound.play(button_sound)
                pg.time.delay(300)
                if action is not None:
                    if action==quit:
                        pg.mixer.Sound.play(button_sound)
                        pg.time.delay(300)
                        pg.quit()
                        exit()
                    else:
                        pg.mixer.Sound.play(button_sound)
                        pg.time.delay(300)
                        action()
                else:#
                    return True#

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
