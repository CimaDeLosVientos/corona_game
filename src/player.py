from pygame import sprite, transform
from pygame.locals import *
from .helpers import *
from .parameters import *

class Player(sprite.Sprite):
    def __init__(self, device, pos_x, pos_y):
        sprite.Sprite.__init__(self)
        self.device = device
        self.sprites = self.load_sprites()
        self.image = self.sprites["normal"]
        self.x = self.x_initial = pos_x         #X inicial
        self.y = pos_y         #Y inicial   
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.keyMap = {}
        self.current_frame = -1
        self.state = "idle"
        self.score = {}
        self.health = INITIAL_HEALTH
        self.setPlayer(device)
        self.restart()

    def restart(self):
        #Reiniciar atributos del personaje
        self.state = "idle"
        self.score = {
            "chicken_thigh" : 0,
            "laptop" : 0,
            "mouse" : 0,
            "pizza" : 0,
            "salad" : 0,
            "soap" : 0,
            "steak" : 0,
            "toilet_paper" : 0,
            "video" : 0
        }
        self.x = self.x_initial
        self.image = self.sprites["normal"]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)


    def setPlayer(self, device):
        return
        if device == "keyboard":
            self.keyMap["left"] = K_a
            self.keyMap["right"] = K_d
        #elif device == "pad":
        #    self.keyMap["up"] = (0,1)
        #    self.keyMap["down"] = (0,-1)
        #    self.keyMap["left"] = (-1,0)
        #    self.keyMap["right"] = (0,1)
        #    self.keyMap["weakAttack"] = 2       #Number of the button (X on Xbox controller)
        #    self.keyMap["strongAttack"] = 3     #Number of the button (Y on Xbox controller)

    def load_sprites(self):
        ficha = {
            "normal": load_image("assets/images/sprites/bobi_normal.png"),
            "left"  : load_image("assets/images/sprites/bobi_left.png"),
            "front" : load_image("assets/images/sprites/bobi_front.png"),
            "right" : load_image("assets/images/sprites/bobi_right.png")
            #"left"  : transform.scale(load_image("assets/images/sprites/bobi_left.png"), PLAYER_SURFACE),
            #"front" : transform.scale(load_image("assets/images/sprites/bobi_front.png"), PLAYER_SURFACE),
            #"right" : transform.scale(load_image("assets/images/sprites/bobi_right.png"), PLAYER_SURFACE)
        }
        return ficha

    def actionKeyboard(self, keys, time):
        if keys[K_a] or keys[K_LEFT]:
            self.move("left", time)
            if self.state != "left":
                self.current_frame = 0
                self.state = "left"
        elif keys[K_d] or keys[K_RIGHT]:
            self.move("right", time)
            if self.state != "right":
                self.current_frame = FRAME_PER_SPRITE
                self.state = "right"
        else:
            self.state = "idle"


    def getFrame(self):
        if self.current_frame == -1:
            return self.sprites["normal"]
        if self.state == "idle":
            return self.sprites["front"]

        self.current_frame += 1
        if self.current_frame == FRAME_PER_SPRITE * 2 + 1:
            self.current_frame = 0
        if True:#self.orientation == -1:
            #if self.cdHurt > 0:
            #    self.cdHurt -= 1
            #    return self.sprites["sufferBack"]
            if self.current_frame <= FRAME_PER_SPRITE:
                return self.sprites["left"]
            else:
                return self.sprites["right"]



        # if self.cdHurt > 0:
        #     self.cdHurt -= 1
        #     return self.sprites["sufferFront"]

        # if self.cdShoot > 3:
        #     if self.current_frame < 5:
        #         sprite = self.sprites["frontAttack"][0]
        #     if (self.current_frame >= 5 and self.current_frame <= 10) or (self.current_frame >= 15 and self.current_frame < 20):
        #         sprite = self.sprites["frontAttack"][1]
        #     if self.current_frame >= 10 and self.current_frame < 15:
        #         sprite = self.sprites["frontAttack"][2]
        # else:
        #     if self.current_frame < 5:
        #         sprite = self.sprites["front"][0]
        #     if (self.current_frame >= 5 and self.current_frame < 10) or (self.current_frame >= 15 and self.current_frame < 20):
        #         sprite = self.sprites["front"][1]
        #     if self.current_frame >= 10 and self.current_frame < 15:
        #         sprite = self.sprites["front"][2]
        # return sprite
# Actions
    def move(self, direction, time):
        speed = PLAYER_SPEED
        if direction == "left":
            self.x -= time * speed
            if self.x <= LEFT_LIMIT:
                self.x = LEFT_LIMIT
        if direction == "right":
            self.x += time * speed
            if self.x >= RIGHT_LIMIT:
                self.x = RIGHT_LIMIT

    def update(self):
        self.image = self.getFrame()
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

