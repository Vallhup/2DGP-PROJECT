from pico2d import *
import game_world
import game_framework
import background

class Heal_Item:
    image = None
    def __init__(self, x = 1500):
        if Heal_Item == None:
            Heal_Item.image = load_image("heal_item.png")
        self.x = x

    def update(self):
        self.x -= background.RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        self.image.draw_to_origin(self.x, 70, 120, 120)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x + 25, 100, self.x + 90, 160

    def handle_collision(self, other, group):
        print('character meets item')
        if group == 'character:heal_item':
            game_world.remove_object(self)