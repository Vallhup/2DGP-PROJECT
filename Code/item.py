from pico2d import *
import game_framework
import background

class Item:
    def __init__(self, x = 1050):
        self.image = load_image("heal_item.png")
        self.x = x

    def update(self):
        self.x -= background.RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        self.image.draw_to_origin(self.x, 70, 120, 120)