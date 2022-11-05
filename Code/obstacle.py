from pico2d import *

class Obstacle:
    def __init__(self):
        self.image = load_image("trash.png")

    def update(self):
        pass

    def draw(self):
        self.image.draw_to_origin(200, 90, 75, 130)
