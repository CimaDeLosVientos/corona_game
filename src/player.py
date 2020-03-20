from pygame import sprite, transform
from pygame.locals import *
from .helpers import *
from .parameters import *

class Player(sprite.Sprite):
    def __init__(self, device, pos_x, pos_y):
        sprite.Sprite.__init__(self)
        self.device = device
        self.sprites = self.load_sprites()
        self.image = self.sprites["front"]
        self.x = pos_x         #X inicial
        self.y = pos_y         #Y inicial   
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.keyMap = {}
        self.current_frame = -1
        #self.state = "idle"
        self.score = {}
        self.healt = INITIAL_HEALT
        self.setPlayer(device)
        self.restart(pos_x, pos_y)

    def restart(self, pos_x, pos_y):
        #Reiniciar atributos del personaje
        self.state = "idle"
        self.score = {"soap": 0, "video": 0}
        self.x = pos_x         #X inicial
        self.y = pos_y         #Y inicial   
        self.image = self.sprites["front"]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)


    def setPlayer(self, device):
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
            "left"  : transform.scale(load_image("assets/images/sprites/bobby_left.png"), PLAYER_SURFACE),
            "front" : transform.scale(load_image("assets/images/sprites/bobby_front.png"), PLAYER_SURFACE),
            "right" : transform.scale(load_image("assets/images/sprites/bobby_right.png"), PLAYER_SURFACE)
        }
        return ficha

    def actionKeyboard(self, keys, time):
        if keys[self.keyMap["right"]]:
            self.move("right", time)
            if self.current_frame == -1:
                self.current_frame = 0
        if keys[self.keyMap["left"]]:
            self.move("left", time)
            if self.current_frame == -1:
                self.current_frame = 0
    

    def getFrame(self):
        if self.current_frame == -1:
            return self.sprites["front"]
        self.current_frame += 1
        if self.current_frame == FRAME_PER_SPRITE * 4:
            self.current_frame = 0

        if True:#self.orientation == -1:
            #if self.cdHurt > 0:
            #    self.cdHurt -= 1
            #    return self.sprites["sufferBack"]
            if self.current_frame < FRAME_PER_SPRITE:
                return self.sprites["left"]
            elif ((self.current_frame >= FRAME_PER_SPRITE and self.current_frame <= FRAME_PER_SPRITE * 2) 
                or (self.current_frame >= FRAME_PER_SPRITE * 3 and self.current_frame < FRAME_PER_SPRITE * 4)):
                return self.sprites["front"]
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

