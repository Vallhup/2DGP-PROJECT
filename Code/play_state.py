from pico2d import *
import game_framework

from character import Character
from item import Item

character = None
heal_item = None

def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()

        else:
            character.handle_event(event)

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
