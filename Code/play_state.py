from pico2d import *
import game_framework
import game_world

from character import Character
from item import Item
from background import Background

character = None
heal_item = None
background = None

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
    global character, heal_item, background

    character = Character()
    heal_item = Item()
    background = Background()

    game_world.add_object(background, 0)
    game_world.add_object(character, 1)
    game_world.add_object(heal_item, 1)

def exit():
    game_world.clear()

def update():
    delay(0.05)
    for game_object in game_world.all_objects():
        game_object.update()

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

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
