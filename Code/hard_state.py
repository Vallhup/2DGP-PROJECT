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
die = None

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
    global character, heal_item, star_item, background, obstacle, bird, die

    from character import Character

    game_world.load("hard_state.pickle")

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

        elif isinstance(o, Die):
            if type(o) is Die:
                die = o


    # character = Character(100, 130, 2)
    # background = Background(2)
    #
    # obstacle += [ Obstacle(i) for i in range(600, 3400 + 1, 700) ]
    # bird += [ Bird(i) for i in range(950, 3750 + 1, 700) ]
    # star_item = Star_Item(3930, 150)
    # bird.append(Bird(4000))
    # obstacle += [ Obstacle(i) for i in range(4200, 4500 + 1, 100) ]
    # heal_item.append(Heal_Item(4600))
    # obstacle.append(Obstacle(5400))
    # obstacle.append(Obstacle(6100))
    # bird.append(Bird(6400))
    # obstacle += [ Obstacle(i) for i in range(6800, 8300 + 1, 500) ]
    # bird += [Bird(i) for i in range(8600, 9000 + 1, 200) ]
    # obstacle += [Obstacle(i) for i in range(9600, 11000 + 1, 700)]
    # bird += [Bird(i) for i in range(9950, 11350 + 1, 700)]
    # die = Die(11700)
    #
    # game_world.add_object(background, 0)
    # game_world.add_object(character, 1)
    # game_world.add_objects(heal_item, 1)
    # game_world.add_objects(obstacle, 1)
    # game_world.add_objects(bird, 1)
    # game_world.add_object(star_item, 1)
    # game_world.add_object(die, 1)
    #
    # # character와 heal_item 충돌 그룹 추가
    # game_world.add_collision_group(character, heal_item, 'character:heal_item')
    #
    # # character와 obstacle, bird, die 충돌 그룹 추가
    # game_world.add_collision_group(character, obstacle, 'character:obstacle')
    # game_world.add_collision_group(character, bird, 'character:obstacle')
    # game_world.add_collision_group(character, die, 'character:die')
    #
    # # character와 star_item 충돌 그룹 추가
    # game_world.add_collision_group(character, star_item, 'character:star_item')
    #
    # game_world.save("hard_state.pickle")


def exit():
    game_world.clear()

def update():
    # delay(0.05)
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('COLLISION by', group)
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