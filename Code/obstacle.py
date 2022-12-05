from pico2d import *
import game_world
import game_framework
import background

class Obstacle:
    image = None
    def __init__(self, x = 1000):
        if Obstacle.image == None:
            Obstacle.image = load_image("trash.png")

        self.x = x

    def update(self):
        self.x -= background.RUN_SPEED_PPS * game_framework.frame_time
        pass

    def draw(self):
        self.image.draw_to_origin(self.x, 90, 50, 80)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x, 90, self.x + 50, 170

    def handle_collision(self, other, group):
        pass