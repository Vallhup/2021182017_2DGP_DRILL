from pico2d import *

import game_framework
import game_world

# Bird Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

draw_y = 0

#2 : 상태의 정의
class FLY:
    @staticmethod
    def enter(self,event):
        print('ENTER FLY')
        self.dir = 1

    @staticmethod
    def exit(self, event):
        print('EXIT FLY')

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 1600)

        global draw_y

        if int(self.frame) < 5:
            draw_y = 0

        elif int(self.frame) < 10:
            draw_y = 170

        else:
            draw_y = 340

        if self.x >= 1600:
            self.dir = -1

        elif self.x <= 0:
            self.dir = 1

    @staticmethod
    def draw(self):
        if self.dir == 1:
            self.image.clip_draw((int(self.frame) % 5) * 180, draw_y, 180, 160, self.x, self.y, 110, 100)
        else:
            self.image.clip_composite_draw((int(self.frame) % 5) * 180, draw_y, 180, 160, 0, 'h', self.x, self.y, 110, 100)


PIXEL_PER_METER = 10 / 0.3
RUN_SPEED_KPH = 30 # km/h
RUN_SPEED_MPM = RUN_SPEED_KPH * 1000.0 / 60
RUN_SPEED_MPS = RUN_SPEED_MPM / 60
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

next_state = {
    FLY: {FLY}
}

class Bird:
    image = None

    def __init__(self, x = 100, y = 300):
        self.x, self.y = x, y
        self.frame = 0
        self.dir = 0
        if self.image == None:
            self.image = load_image('bird_animation.png')

        self.timer = 100

        self.event_que = []
        self.cur_state = FLY
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}    Event')
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        pass