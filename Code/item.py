from pico2d import *
import game_world
import game_framework
import background

class Heal_Item:
    image = None
    def __init__(self, x = 1500):
        if Heal_Item.image == None:
            Heal_Item.image = load_image("heal_item.png")
        self.x = x
        self.y = 130

    def __getstate__(self):
        state = {'x': self.x, 'y': self.y}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def update(self):
        self.x -= background.RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        self.image.draw_to_origin(self.x, self.y, 120, 120)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x + 25, self.y + 30, self.x + 90, self.y + 30 + 60

    def handle_collision(self, other, group):
        print('character meets item')
        if group == 'character:heal_item':
            game_world.remove_object(self)

class Star_Item:
    image = None
    def __init__(self, x = 800, y = 230):
        if Star_Item.image == None:
            Star_Item.image = load_image("star_item.png")
        self.x = x
        self.y = y

    def __getstate__(self):
        state = {'x': self.x, 'y': self.y}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def update(self):
        self.x -= background.RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        self.image.draw_to_origin(self.x, self.y, 60, 60)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x, self.y, self.x + 60, self.y + 60

    def handle_collision(self, other, group):
        print('character meets item')
        if group == 'character:star_item':
            game_world.remove_object(self)