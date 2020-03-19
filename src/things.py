from pygame import sprite
from pygame.locals import *
from .helpers import *
from .parameters import *

class Thing(sprite.Sprite):
    def __init__(self, position):
        sprite.Sprite.__init__(self)
        self.speed = 10
        self.x = position[0]
        self.y = position[1]


    def move(self):
        self.y += self.speed

    def update(self, player):
        self.move()
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        if sprite.collide_rect(self, player):
            self.be_caught(player)
        elif self.y >= BOTTOM_LIMIT:
            self.kill()

    def be_caught(self, player):
        pass

class Soap(Thing):
    def __init__(self, position):
        super(Soap, self).__init__(position)
        self.image = load_image("assets/images/sprites/soap.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)


    def be_caught(self, player):
        player.score["soap"] += 1
        player.healt -= 1
        self.kill()

class Video(Thing):
    def __init__(self, position):
        super(Video, self).__init__(position)
        self.image = load_image("assets/images/sprites/video.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def be_caught(self, player):
        player.score["video"] += 1
        self.kill()