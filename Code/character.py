from pico2d import *

# 1. 이벤트 정의
JD, SD, SU, TIMER = range(4)
event_name = ['JD', 'SD', 'SU', 'TIMER']

key_event_table = {
    (SDL_KEYDOWN, SDLK_UP): JD,
    (SDL_KEYDOWN, SDLK_DOWN): SD,
    (SDL_KEYUP, SDLK_DOWN): SU
}

# 2. 상태 정의
class RUN:
    @staticmethod
    def enter(self, event):
        print('ENTER RUN')

    @staticmethod
    def exit(self, event):
        print('EXIT RUN')

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 5
        pass

    @staticmethod
    def draw(self):
        self.image_main.clip_draw(self.frame * 84, 250, 50, 55, self.x, self.y, 100, 100)
        pass

class JUMP:
    @staticmethod
    def enter(self, event):
        print('ENTER JUMP')


    @staticmethod
    def exit(self, event):
        print('EXIT JUMP')

    @staticmethod
    def do(self):
        if self.jump_count < 8:
            self.jump += 20

        else:
            self.jump -= 20

        if self.jump_count == 15:
            self.add_event(TIMER)

        self.jump_frame = (self.jump_frame + 1) % 8
        self.jump_count = (self.jump_count + 1) % 16
        pass

    @staticmethod
    def draw(self):
        self.image_main.clip_draw(self.jump_frame * 70, 110, 60, 60, self.x, self.y + self.jump, 100, 100)
        pass

class SLIDE:
    @staticmethod
    def enter(self, event):
        print('ENTER SLIDE')

    @staticmethod
    def exit(self, event):
        print('EXIT SLIDE')

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
    def add_event(self, event):
        self.STATE_Q.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
    def __init__(self, x = 100, y = 90):
        self.x, self.y = x, y
        self.frame = 0
        self.life = 3
        self.image_main = load_image("character_sprite1.png")
        self.image_life = load_image("character_life.png")

        self.STATE_Q = []
        self.cur_state = RUN
        self.cur_state.enter(self, None)

        self.jump = 0
        self.jump_count = 0
        self.jump_frame = 0

    def update(self):
        self.cur_state.do(self)

        if self.STATE_Q:
            event = self.STATE_Q.pop()
            self.cur_state.exit(self, event)
            # try:
            #     self.cur_state = next_state[self.cur_state][event]
            #
            # except KeyError:
            #     print('ERROR : ', self.cur_state.__name__, ' ', event_name[event])
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)


        # match self.state:
        #     case 0:
        #         self.frame = (self.frame + 1) % 5
        #
        #     case 1:
        #         self.jump_frame = (self.jump_frame + 1) % 8

    def draw(self):
        self.cur_state.draw(self)

        for life in range(0, self.life):
            self.image_life.draw(life * 55 + 40, 550)

        # match self.state:
        #     # 달리는 상태
        #     case 0:
        #         self.image_main.clip_draw(self.frame * 84, 250, 50, 55, self.x, self.y, 100, 100)
        #
        #     # 점프 상태
        #     case 1:
        #         if self.jump_count < 8:
        #             self.jump += 20
        #
        #         else:
        #             self.jump -= 20
        #
        #         if self.jump_count == 15:
        #             self.state = 0
        #
        #         self.jump_count = (self.jump_count + 1) % 16
        #         self.image_main.clip_draw(self.jump_frame * 70, 110, 60, 60, self.x, self.y + self.jump, 100, 100)
        #
        #     # 슬라이드 상태
        #     case 2:
        #         self.jump = 0
        #         self.jump_count = 0
        #         self.image_main.clip_draw(0, 190, 60, 55, self.x, self.y, 100, 100)