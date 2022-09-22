from pico2d import *

open_canvas()
character = load_image("drill 6 sprite.jpg")

def Idle(x, y):
    start_x, start_y = 200, 385

    for frame in range(0, 4):
        clear_canvas()
        character.clip_draw(start_x + (frame * 70), start_y, 35, 65, x, y)
        update_canvas()
        delay(0.1)
        get_events()

def Walk(x, y):
    start_x, start_y = 200, 315

    for frame in range(0, 6):
        clear_canvas()
        character.clip_draw(start_x + (frame * 70), start_y, 35, 65, x, y)
        update_canvas()
        delay(0.1)
        get_events()

def Run(x, y):
    start_x, start_y = 195, 240

    for frame in range(0, 6):
        clear_canvas()
        character.clip_draw(start_x + (frame * 70), start_y, 50, 65, x, y)
        update_canvas()
        delay(0.1)
        get_events()

def Push(x, y):
    start_x, start_y = 200, 170

    for frame in range(0, 6):
        clear_canvas()
        character.clip_draw(start_x + (frame * 70), start_y, 50, 65, x, y)
        update_canvas()
        delay(0.1)
        get_events()

def Jump(x, y):
    start_x, start_y = 200, 104

    for frame in range(0, 6):
        clear_canvas()
        character.clip_draw(start_x + (frame * 70), start_y, 50, 65, x, y)
        update_canvas()
        delay(0.1)
        get_events()

def Hurt(x, y):
    start_x, start_y = 195, 30

    for frame in range(0, 3):
        clear_canvas()
        character.clip_draw(start_x + (frame * 70), start_y, 45, 65, x, y)
        update_canvas()
        delay(0.1)
        get_events()

while True:
    Idle(400, 300)
    Walk(400, 300)
    Run(400, 300)
    Push(400, 300)
    Jump(400, 300)
    Hurt(400, 300)
    break

close_canvas()