from pico2d import *

class Grass:
    def __init__(self, x = 400, y = 30):
        self.image = load_image('grass.png')
        self.x, self.y = x, y

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass