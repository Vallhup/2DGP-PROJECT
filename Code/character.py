from pico2d import *

import game_framework
import game_world
import background
import game_over_state
import easy_end_state
import normal_end_state
import hard_end_state

# 1. 이벤트 정의
JD, SD, SU, TIMER = range(4)
event_name = ['JD', 'SD', 'SU', 'TIMER']

key_event_table = {
    (SDL_KEYDOWN, SDLK_UP): JD,
    (SDL_KEYDOWN, SDLK_DOWN): SD,
    (SDL_KEYUP, SDLK_DOWN): SU
}

# Run Action Speed
TIME_PER_RUN_ACTION = 0.3
RUN_ACTION_PER_TIME = 1.0 / TIME_PER_RUN_ACTION
FRAMES_PER_RUN_ACTION = 5

# Jump Action Speed
TIME_PER_JUMP_ACTION = 1.6
JUMP_ACTION_PER_TIME = 1.0 / TIME_PER_JUMP_ACTION
FRAMES_PER_JUMP_ACTION = 8

# 2. 상태 정의
class RUN:
    @staticmethod
    def enter(self, event):
        pass

    @staticmethod
    def exit(self, event):
        pass

    @staticmethod
    def do(self):
        # self.frame = (self.frame + 1) % 5
        # print(f'{self.star}')
        self.frame = (self.frame + FRAMES_PER_RUN_ACTION * RUN_ACTION_PER_TIME * game_framework.frame_time) % 5


        pass

    @staticmethod
    def draw(self):
        self.image_main.clip_draw(int(self.frame) * 84, 250, 50, 55, self.x, self.y, 100, 100)
        pass


class JUMP:
    @staticmethod
    def enter(self, event):
        pass

    @staticmethod
    def exit(self, event):
        pass

    @staticmethod
    def do(self):
        if self.jump_count == 1:
            self.y -= 280 * game_framework.frame_time

        else:
            self.y += 280 * game_framework.frame_time

        if self.y > 280:
            self.jump_count = 1

        if self.y < 130:
            self.y = 130
            self.jump_count = 0
            self.add_event(TIMER)

        self.jump_frame = (self.jump_frame + FRAMES_PER_JUMP_ACTION * JUMP_ACTION_PER_TIME * game_framework.frame_time) % 8
        pass

    @staticmethod
    def draw(self):
        self.image_main.clip_draw(int(self.jump_frame) * 70, 110, 60, 60, self.x, self.y, 100, 100)
        pass

class SLIDE:
    @staticmethod
    def enter(self, event):
        pass

    @staticmethod
    def exit(self, event):
        pass

    @staticmethod
    def do(self):
        pass

    @staticmethod
    def draw(self):
        self.image_main.clip_draw(0, 190, 60, 55, self.x, self.y, 100, 100)
        pass

# 3. 상태 변환 구현
next_state = {
    RUN  : {JD: JUMP, SD: SLIDE, SU: RUN},
    JUMP : {JD: JUMP, SD: JUMP, SU: JUMP, TIMER: RUN},
    SLIDE: {JD: JUMP, SD: SLIDE, SU: RUN}
}

class Character:
    image_main = None
    image_life = None
    image_star_life = None

    def add_event(self, event):
        self.STATE_Q.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def __init__(self, x = 100, y = 130, map = 0):
        self.x, self.y = x, y
        self.sx = x
        self.frame = 0
        self.life = 3
        self.map = map
        self.map_size = 0

        if self.map == 0:
            self.map_size = 6200

        if self.map == 1:
            self.map_size = 9000

        if self.map == 2:
            self.map_size = 12000

        if Character.image_main == None:
            self.image_main = load_image("character_sprite.png")

        if Character.image_life == None:
            self.image_life = load_image("character_life.png")

        if Character.image_star_life == None:
            self.image_star_life = load_image("character_star_life.png")

        self.STATE_Q = []
        self.cur_state = RUN
        self.cur_state.enter(self, None)

        self.jump = 0
        self.jump_count = 0
        self.jump_frame = 0

        self.star = False
        self.star_count = 0

    def __getstate__(self):
        state = { 'x': self.x, 'y': self.y, 'sx': self.sx, 'map': self.map, 'map_size': self.map_size }
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def update(self):
        if self.life <= 0:
            game_framework.change_state(game_over_state)

        self.cur_state.do(self)

        self.sx += background.RUN_SPEED_PPS * game_framework.frame_time

        if self.sx > self.map_size:
            self.x += background.RUN_SPEED_PPS * game_framework.frame_time

        if self.x > 1100:
            if self.map == 0:
                game_framework.change_state(easy_end_state)

            elif self.map == 1:
                game_framework.change_state(normal_end_state)

            elif self.map == 2:
                game_framework.change_state(hard_end_state)

        if self.star == True:
            self.star_count += game_framework.frame_time

        if self.star_count > 5:
            self.star = False
            self.star_count = 0

        if self.STATE_Q:
            event = self.STATE_Q.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]

            except KeyError:
                print('ERROR : ', self.cur_state.__name__, ' ', event_name[event])

            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

        for life in range(0, self.life):
            if self.star == False:
                self.image_life.draw(life * 55 + 50, 500)

            else:
                self.image_star_life.draw(life * 55 + 50, 500)

    def get_bb(self):
        if self.cur_state == SLIDE:
            return self.x - 35, self.y - 40, self.x + 45, self.y + 15

        return self.x - 25, self.y - 40, self.x + 35, self.y + 40

    def handle_collision(self, other, group):
        if group == 'character:heal_item':
            if self.life < 3:
                self.life += 1

        if group == 'character:obstacle':
            if self.star == False and other.damage == True:
                self.life -= 1

        if group == 'character:die':
            if self.star == False and other.damage == True:
                self.life -= 3

        if group == 'character:star_item':
            self.star = True

