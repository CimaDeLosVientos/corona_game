from pygame import sprite
from pygame.locals import *
from .helpers import *
from .parameters import *

class Player(sprite.Sprite):
    def __init__(self, device, pos_x, pos_y):
        sprite.Sprite.__init__(self)
        self.device = device
        #self.sprites = self.load_sprites("assets/images/sprites/bobby.png", 64, 64)
        self.image = load_image("assets/images/sprites/bobby.png")
        self.x = pos_x         #X inicial
        self.y = pos_y         #Y inicial   
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.soap = 0
        self.keyMap = {}
        self.current_frame = 0
        self.state = "idle"
        self.setPlayer(device)
        self.restart(pos_x, pos_y)

    def restart(self, pos_x, pos_y):
        #Reiniciar atributos del personaje
        self.state = "idle"
        self.x = pos_x         #X inicial
        self.y = pos_y         #Y inicial   
        self.image = load_image("assets/images/sprites/bobby.png") 
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

    def load_sprites(self, filename, width, height):
        ficha = {}

        sprite_ficha = load_image(filename)
        ficha["front"] = []
        ficha["frontAttack"] = []
        ficha["back"] = []
        for i in range(0,3):
            ficha["front"].append(sprite_ficha.subsurface((i*64, 0*64, width, height)))
            ficha["frontAttack"].append(sprite_ficha.subsurface((i*64, 1*64, width, height)))
            ficha["back"].append(sprite_ficha.subsurface((i*64, 2*64, width, height)))

        ficha["sufferFront"] = sprite_ficha.subsurface((0, 3*64, width, height))
        ficha["sufferBack"] = sprite_ficha.subsurface((64, 3*64, width, height))

        for i in range(0,5):
            h = load_image("assets"+os.sep+"img"+os.sep+"sprites"+os.sep+"heart1.png")
            h_rect = h.get_rect()
            h_rect.centerx = 768+32
            if self.orientation == 1:
                h_rect.centery = 64*i + 32
            if self.orientation == -1:
                h_rect.centery = 768/2 + 64*i + 96
            self.heart.append([h, h_rect])

        return ficha

    def actionKeyboard(self, keys, time):
        if keys[self.keyMap["right"]]:
            self.move("right", time)
        if keys[self.keyMap["left"]]:
            self.move("left", time)

# Actions
    def move(self, direction, time): # se sale por los lados
        distance = 0.5
        if direction == "left":
            self.x -= time*distance
            if self.x <= LEFT_LIMIT:
                self.x = LEFT_LIMIT
        if direction == "right":
            self.x += time*distance
            if self.x >= RIGHT_LIMIT:
                self.x = RIGHT_LIMIT

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

