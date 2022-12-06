from pico2d import *

import game_framework
import game_world
import easy_state
import normal_state
import hard_state

image = None
select_level = 0

def handle_events():
    global select_level
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_RIGHT:
                    select_level += 1

                case pico2d.SDLK_LEFT:
                    select_level -= 1

                case pico2d.SDLK_RETURN:
                    match select_level:
                        case 0:
                            game_framework.change_state(easy_state)

                        case 1:
                            game_framework.change_state(normal_state)

                        case 2:
                            game_framework.change_state(hard_state)

            select_level = clamp(0, select_level, 2)


def enter():
    global image, select_level

    image = load_image("select_level.png")
    select_level = 0

    game_world.add_object(image, 0)

def exit():
    game_world.clear()

def update():
    pass

def draw():
    clear_canvas()
    image.draw(490, 280)
    draw_rectangle(44 + select_level * 318, 60, 308 + select_level * 318, 325)
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
