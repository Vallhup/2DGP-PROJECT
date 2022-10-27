from pico2d import *
import game_framework

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

