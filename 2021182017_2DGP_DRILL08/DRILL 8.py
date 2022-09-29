from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x_dir, y_dir
    global sprite_num

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x_dir += 1
                y_dir = 0
                sprite_num = 1

            elif event.key == SDLK_LEFT:
                x_dir -= 1
                y_dir = 0
                sprite_num = 0

            elif event.key == SDLK_UP:
                x_dir = 0
                y_dir += 1

            elif event.key == SDLK_DOWN:
                x_dir = 0
                y_dir -= 1

            elif event.key == SDLK_ESCAPE:
                running = False

            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    x_dir -= 1

                elif event.key == SDLK_LEFT:
                    x_dir += 1

                elif event.key == SDLK_UP:
                    y_dir -= 1

                elif event.key == SDLK_DOWN:
                    y_dir += 1


open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2
frame = 0
x_dir = 0
y_dir = 0
sprite_num = 1

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * sprite_num, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += x_dir * 5
    y += y_dir * 5

    if x <= 20:
        x = 20

    elif x >= 1250:
        x = 1250

    elif y <= 20:
        y = 20

    elif y >= 1000:
        y = 1000

    delay(0.01)

close_canvas()
