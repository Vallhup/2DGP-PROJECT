from pico2d import *
import game_framework
import game_world

from item import *
from background import Background
from obstacle import *

character = None
heal_item = []
star_item = None
background = None
obstacle = []
bird = []

bgm = None

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
    global character, heal_item, star_item, background, obstacle, bird, bgm

    from character import Character

    game_world.load("normal_state.pickle")

    for o in game_world.all_objects():
        if isinstance(o, Character):
            if type(o) is Character:
                character = o

        elif isinstance(o, Background):
            if type(o) is Background:
                background = o

        elif isinstance(o, Heal_Item):
            if type(o) is Heal_Item:
                heal_item = o

        elif isinstance(o, Obstacle):
            if type(o) is Obstacle:
                obstacle = o

        elif isinstance(o, Bird):
            if type(o) is Bird:
                bird = o

        elif isinstance(o, Star_Item):
            if type(o) is Star_Item:
                star_item = o

    bgm = load_music("normal_sound.mp3")
    bgm.set_volume(30)
    bgm.repeat_play()

    # character = Character(100, 130, 1)
    # heal_item.append(Heal_Item(4470))
    # background = Background(1)
    # obstacle = [ Obstacle(i) for i in range(650, 3500 + 1, 650) ]
    # bird.append(Bird(900))
    # bird += [ Bird(i) for i in range(3700, 4600 + 1, 300) ]
    # obstacle.append(Obstacle(5300))
    # bird.append(Bird(5700))
    # bird.append(Bird(5900))
    # obstacle.append(Obstacle(6250))
    # bird.append(Bird(6500))
    # star_item = Star_Item(6750, 230)
    # obstacle.append(Obstacle(6900))
    # bird.append(Bird(7000))
    # heal_item.append(Heal_Item(7150))
    # obstacle += [ Obstacle(i) for i in range(7300, 8600 + 1, 650) ]
    #
    # game_world.add_object(background, 0)
    # game_world.add_object(character, 1)
    # game_world.add_objects(heal_item, 1)
    # game_world.add_objects(obstacle, 1)
    # game_world.add_objects(bird, 1)
    # game_world.add_object(star_item, 1)
    #
    # # character와 heal_item 충돌 그룹 추가
    # game_world.add_collision_group(character, heal_item, 'character:heal_item')
    #
    # # character와 obstacle, bird 충돌 그룹 추가
    # game_world.add_collision_group(character, obstacle, 'character:obstacle')
    # game_world.add_collision_group(character, bird, 'character:obstacle')
    #
    # # character와 star_item 충돌 그룹 추가
    # game_world.add_collision_group(character, star_item, 'character:star_item')
    #
    # game_world.save("normal_state.pickle")


def exit():
    global bgm
    del bgm

    game_world.clear()

def update():
    # delay(0.05)
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            a.handle_collision(b, group)
            b.handle_collision(a, group)

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

def collide(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    return True

def test_self():
    import sys

    this_module = sys.modules['__main__']
    pico2d.open_canvas(980, 560)
    game_framework.run(this_module)
    pico2d.close_canvas()


if __name__ == '__main__':
    test_self()
