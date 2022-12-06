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
        self.damage = True

    def __getstate__(self):
        state = {'x': self.x, 'damage': self.damage}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def update(self):
        self.x -= background.RUN_SPEED_PPS * game_framework.frame_time

        if self.x < -50:
            game_world.remove_object(self)
        pass

    def draw(self):
        self.image.draw_to_origin(self.x, 90, 50, 80)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x, 90, self.x + 50, 170

    def handle_collision(self, other, group):
        if group == 'character:obstacle':
            self.damage = False
        pass

class Bird(Obstacle):
    image = None

    def __init__(self, x = 1000):
        if Bird.image == None:
            Bird.image = load_image("bird.png")

        self.x = x
        self.damage = True

    def update(self):
        self.x -= background.RUN_SPEED_PPS * game_framework.frame_time

        if self.x < -160:
            game_world.remove_object(self)
        pass

    def draw(self):
        self.image.draw_to_origin(self.x, 150, 160, 120)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x, 150, self.x + 160, 270

class Die(Obstacle):
    image = None
    def __init__(self, x = 1000):
        if Die.image == None:
            Die.image = load_image("die.png")

        self.x = x
        self.damage = True

    def handle_collision(self, other, group):
        if group == 'character:die':
            self.damage = False
