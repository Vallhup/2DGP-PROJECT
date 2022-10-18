from pico2d import *


class Character:
    def __init__(self):
        self.x, self.y = 100, 90
        self.jump = 0
        self.jump_count = 0
        self.jump_frame = 0
        self.frame = 0
        self.state = 0
        self.life = 3
        self.image_main = load_image("character_sprite1.png")
        self.image_life = load_image("character_life.png")

    def update(self):
        match self.state:
            case 0:
                self.frame = (self.frame + 1) % 5

            case 1:
                self.jump_frame = (self.jump_frame + 1) % 8

    def draw(self):
        match self.state:
            # 달리는 상태
            case 0:
                self.image_main.clip_draw(self.frame * 84, 250, 50, 55, self.x, self.y)

            # 점프 상태
            case 1:
                if self.jump_count < 4:
                    self.jump += 20

                else:
                    self.jump -= 20

                if self.jump_count == 7:
                    self.state = 0

                self.jump_count = (self.jump_count + 1) % 8
                self.image_main.clip_draw(self.jump_frame * 70, 110, 60, 60, self.x, self.y + self.jump)

            # 슬라이드 상태
            case 2:
                self.jump = 0
                self.jump_count = 0
                self.image_main.clip_draw(0, 190, 60, 55, self.x, self.y)

        for life in range(0, self.life):
            self.image_life.draw(life * 55 + 40, 550)


def handle_events():
    global running

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    running = False

                case pico2d.SDLK_UP:
                    character.state = 1

                case pico2d.SDLK_DOWN:
                    character.state = 2

        elif event.type == SDL_KEYUP:
            match event.key:
                case pico2d.SDLK_DOWN:
                    character.state = 0


open_canvas()

character = Character()
running = True

while running:
    handle_events()

    character.update()

    clear_canvas()
    character.draw()
    update_canvas()

    delay(0.05)

close_canvas()