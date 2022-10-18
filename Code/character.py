from pico2d import *


class Character:
    def __init__(self):
        self.x, self.y = 100, 90
        self.jump = 0
        self.jump_count = 0
        self.frame = 0
        self.state = 0
        self.image = load_image("character_sprite1.png")

    def update(self):
        self.frame = (self.frame + 1) % 5

    def draw(self):
        match self.state:
            # 달리는 상태
            case 0:
                self.image.clip_draw(self.frame * 84, 250, 50, 55, self.x, self.y)

            # 점프 상태
            case 1:
                if self.jump_count < 5:
                    self.jump += 10

                else:
                    self.jump -= 10

                if self.jump_count == 9:
                    self.state = 0

                self.jump_count = (self.jump_count + 1) % 10
                self.image.clip_draw(self.frame * 84, 250, 50, 55, self.x, self.y + self.jump)

            # 슬라이드 상태
            case 2:
                self.image.clip_draw(0, 190, 60, 55, self.x, self.y)


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