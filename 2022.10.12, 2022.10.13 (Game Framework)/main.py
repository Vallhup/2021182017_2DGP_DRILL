import pico2d
import play_state
import logo_state

states = [logo_state, play_state] # 모듈을 변수로 취급

pico2d.open_canvas()

for state in states:
    state.enter()

    # game main loop code
    while state.running:
        state.handle_events()
        state.update()

        state.draw()
        pico2d.delay(0.05)

    state.exit()

# finalization code
pico2d.close_canvas()
