from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def run_circle():
    print('CIRCLE')

    clear_canvas_now()
    boy.draw_now(400, 300)
    delay(0.1)
    pass

def run_rectangle():
    print('RECTANGLE')
    pass

while True:
    run_circle()
    run_rectangle()

close_canvas()
