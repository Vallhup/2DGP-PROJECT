from pico2d import *
import game_framework

PIXEL_PER_METER = 10 / 0.3
RUN_SPEED_KPH = 20
RUN_SPEED_MPM = RUN_SPEED_KPH * 1000.0 / 60
RUN_SPEED_MPS = RUN_SPEED_MPM / 60
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

class Background:
    def __init__(self):
        self.image = load_image("spring.png")
        self.x = 0

    def update(self):
        self.x = (self.x + RUN_SPEED_PPS * game_framework.frame_time) % 980

    def draw(self):
        self.image.clip_draw(int(self.x), 0, 980 - int(self.x), 560, 490 - int(self.x) / 2.0, 280)
        self.image.clip_draw(0, 0, int(self.x), 560, 980 - int(self.x) / 2.0, 280)