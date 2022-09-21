from pico2d import *
import math

open_canvas()

grass = load_image("grass.png")
character = load_image("character.png")

x = 400
y = 90

r = 200
rad = -90
pi = 3.141592

while (True):
    while (x < 780):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 4
        delay(0.01)

    while (y < 560):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 4
        delay(0.01)

    while (x > 10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 4
        delay(0.01)

    while(y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y -= 4
        delay(0.01)

    while (x < 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 4
        delay(0.01)
        
    while(rad < 270):
        x = r * math.cos(rad * pi / 180) + 400
        y = r * math.sin(rad * pi / 180) + 290
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
       
        rad  = rad + 10
        delay(0.01)

    rad = -90
    
close_canvas()
