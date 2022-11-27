import pico2d
import game_framework
import title_state

pico2d.open_canvas(980, 560)
game_framework.run(title_state)
pico2d.close_canvas()