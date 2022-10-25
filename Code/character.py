from pico2d import *
import game_framework


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
                self.image_main.clip_draw(self.frame * 84, 250, 50, 55, self.x, self.y, 100, 100)

            # 점프 상태
            case 1:
                if self.jump_count < 8:
                    self.jump += 20

                else:
                    self.jump -= 20

                if self.jump_count == 15:
                    self.state = 0

                self.jump_count = (self.jump_count + 1) % 16
                self.image_main.clip_draw(self.jump_frame * 70, 110, 60, 60, self.x, self.y + self.jump, 100, 100)

            # 슬라이드 상태
            case 2:
                self.jump = 0
                self.jump_count = 0
                self.image_main.clip_draw(0, 190, 60, 55, self.x, self.y, 100, 100)

        for life in range(0, self.life):
            self.image_life.draw(life * 55 + 40, 550)


class Item:
    def __init__(self):
        self.image = load_image("heal_item.png")

    def draw(self):
        self.image.draw_to_origin(400, 30, 150, 150)

def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()

                case pico2d.SDLK_UP:
                    character.state = 1

                case pico2d.SDLK_DOWN:
                    character.state = 2

        elif event.type == SDL_KEYUP:
            match event.key:
                case pico2d.SDLK_DOWN:
                    character.state = 0


character = None
heal_item = None

def enter():
    global character, heal_item

    character = Character()
    heal_item = Item()

def exit():
    global character, heal_item

    del character
    del heal_item

def update():
    delay(0.05)
    character.update()

def draw_world():
    character.draw()
    heal_item.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass

def test_self():
    import sys

    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()


if __name__ == '__main__':
    test_self()

# open_canvas()
# character.start()
# heal_item.start()
#
# while running:
#     handle_events()
#
#     character.update()
#
#     clear_canvas()
#     character.draw()
#     heal_item.draw()
#     update_canvas()
#
#     delay(0.05)
#
# close_canvas()