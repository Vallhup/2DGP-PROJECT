from pico2d import *

import game_framework
import game_world
import title_state
import play_state

image = None

def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:
            game_framework.change_state(title_state)

def enter():
    global image

    image = load_image("game_over.png")

    game_world.add_object(image, 0)

def exit():
    game_world.clear()

def update():
    pass

def draw():
    clear_canvas()
    image.draw(490, 280)
    update_canvas()

def pause():
    pass

def resume():
    pass

def test_self():
    import sys

    this_module = sys.modules['__main__']
    pico2d.open_canvas(980, 560)
    game_framework.run(this_module)
    pico2d.close_canvas()

if __name__ == '__main__':
    test_self()
