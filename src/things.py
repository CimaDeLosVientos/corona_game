from pygame import sprite, transform
from pygame.locals import *
from .helpers import *
from .parameters import *

class Thing(sprite.Sprite):
    def __init__(self, position):
        sprite.Sprite.__init__(self)
        self.speed = FALL_SPEED
        self.x = position[0]
        self.y = position[1]


    def move(self, time):
        self.y += self.speed * time

    def update(self, time, player):
        self.move(time)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        if sprite.collide_rect(self, player):
            self.be_caught(player)
        elif self.y >= BOTTOM_LIMIT:
            self.kill()

    def be_caught(self, player):
        pass



# Bad Things
class BadThing(Thing):
    def __init__(self, position):
        super(BadThing, self).__init__(position)
        self.sound = load_sound("assets/sounds/catch_bad_object.wav")

    def be_caught(self, player):
        self.sound.play()
        player.health -= 1
        self.kill()


class Beer(BadThing):
    def __init__(self, position):
        super(Beer, self).__init__(position)
        self.image = transform.scale(load_image("assets/images/sprites/beer.png"), OBJECT_SURFACE)
        self.rect.center = (self.x, self.y)
        self.rect = self.image.get_rect()

class BadNews(BadThing):
    def __init__(self, position):
        super(BadNews, self).__init__(position)
        self.image = transform.scale(load_image("assets/images/sprites/bad_news.png"), OBJECT_SURFACE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

class Chips(BadThing):
    def __init__(self, position):
        super(Chips, self).__init__(position)
        self.image = transform.scale(load_image("assets/images/sprites/chips.png"), OBJECT_SURFACE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

class FishScraps(BadThing):
    def __init__(self, position):
        super(FishScraps, self).__init__(position)
        self.image = transform.scale(load_image("assets/images/sprites/fish_scraps.png"), OBJECT_SURFACE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

class HotDog(BadThing):
    def __init__(self, position):
        super(HotDog, self).__init__(position)
        self.image = transform.scale(load_image("assets/images/sprites/hotdog.png"), OBJECT_SURFACE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

class LowBattery(BadThing):
    def __init__(self, position):
        super(LowBattery, self).__init__(position)
        self.image = transform.scale(load_image("assets/images/sprites/low_battery.png"), OBJECT_SURFACE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

class Popcorn(BadThing):
    def __init__(self, position):
        super(Popcorn, self).__init__(position)
        self.image = transform.scale(load_image("assets/images/sprites/popcorn.png"), OBJECT_SURFACE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

class RottenApple(BadThing):
    def __init__(self, position):
        super(RottenApple, self).__init__(position)
        self.image = transform.scale(load_image("assets/images/sprites/rotten_apple.png"), OBJECT_SURFACE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)       

class SpoiledSteak(BadThing):
    def __init__(self, position):
        super(SpoiledSteak, self).__init__(position)
        self.image = transform.scale(load_image("assets/images/sprites/spoiled_steak.png"), OBJECT_SURFACE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)


# Good Things
class GoodThing(Thing):
    def __init__(self, position):
        super(GoodThing, self).__init__(position)
        self.sound = load_sound("assets/sounds/catch_good_object.wav")

class ChickenThigh(GoodThing):
    def __init__(self, position):
        super(ChickenThigh, self).__init__(position)
        self.name = "chicken_thigh"
        self.image = transform.scale(load_image("assets/images/sprites/chicken_thigh.png"), OBJECT_SURFACE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def be_caught(self, player):
        self.sound.play()
        player.score["chicken_thigh"] += 1
        self.kill()


class Laptop(GoodThing):
    def __init__(self, position):
        super(Laptop, self).__init__(position)
        self.name = "laptop"
        self.image = transform.scale(load_image("assets/images/sprites/laptop.png"), OBJECT_SURFACE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def be_caught(self, player):
        self.sound.play()
        player.score["laptop"] += 1
        self.kill()


class Mouse(GoodThing):
    def __init__(self, position):
        super(Mouse, self).__init__(position)
        self.name = "mouse"
        self.image = transform.scale(load_image("assets/images/sprites/mouse.png"), OBJECT_SURFACE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def be_caught(self, player):
        self.sound.play()
        player.score["mouse"] += 1
        self.kill()


class Pizza(GoodThing):
    def __init__(self, position):
        super(Pizza, self).__init__(position)
        self.name = "pizza"
        self.image = transform.scale(load_image("assets/images/sprites/pizza.png"), OBJECT_SURFACE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def be_caught(self, player):
        self.sound.play()
        player.score["pizza"] += 1
        self.kill()


class Salad(GoodThing):
    def __init__(self, position):
        super(Salad, self).__init__(position)
        self.name = "salad"
        self.image = transform.scale(load_image("assets/images/sprites/salad.png"), OBJECT_SURFACE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def be_caught(self, player):
        self.sound.play()
        player.score["salad"] += 1
        self.kill()


class Soap(GoodThing):
    def __init__(self, position):
        super(Soap, self).__init__(position)
        self.name = "soap"
        self.image = transform.scale(load_image("assets/images/sprites/soap.png"), OBJECT_SURFACE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def be_caught(self, player):
        self.sound.play()
        player.score["soap"] += 1
        self.kill()


class Steak(GoodThing):
    def __init__(self, position):
        super(Steak, self).__init__(position)
        self.name = "steak"
        self.image = transform.scale(load_image("assets/images/sprites/steak.png"), OBJECT_SURFACE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def be_caught(self, player):
        self.sound.play()
        player.score["steak"] += 1
        self.kill()

class ToiletPaper(GoodThing):
    def __init__(self, position):
        super(ToiletPaper, self).__init__(position)
        self.name = "toilet_paper"
        self.image = transform.scale(load_image("assets/images/sprites/toilet_paper.png"), OBJECT_SURFACE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def be_caught(self, player):
        self.sound.play()
        player.score["toilet_paper"] += 1
        self.kill()


class Video(GoodThing):
    def __init__(self, position):
        super(Video, self).__init__(position)
        self.name = "video"
        self.image = transform.scale(load_image("assets/images/sprites/video.png"), OBJECT_SURFACE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def be_caught(self, player):
        self.sound.play()
        player.score["video"] += 1
        self.kill()