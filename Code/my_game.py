import pico2d
import game_framework
import play_state

pico2d.open_canvas(980, 560)
game_framework.run(play_state)
pico2d.close_canvas()