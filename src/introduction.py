import pygame, os, random, time as tim
from pygame.locals import *
from .scene import Scene
from .helpers import *
from .things import Soap, Video
from .player import Player
from .parameters import *

class Introduction(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.next = None
        self.background = []
        self.current_text = -1
        for i in range():
        	self.background.append(load_image("assets/images/scenes/introduction_text_{}.png".format(i)))

        self.mouse_state = 1 # Up


    def load(self, data):
        pass


    def on_event(self, time, event):
        mouse_press = pygame.mouse.get_pressed()[0]
        if (mouse_press and self.button_state == 1):
            self.button_state = 0
        if (not mouse_press and self.button_state == 0):
			self.current_text += 1
			if (self.current_text == len(self.background)):
				self.next = "level_1_0"
        else:
        	self.button_state = 1


    def on_update(self, time):
        pass


    def on_draw(self, screen):
        # Clear the screen
        screen.fill((0, 0, 0)) ## Comprobar si lo puedo quitar porque es poner en blanco y en teoria lo voy a pintar todo

        # Scene
        if self.current_text >= 0:
        	screen.blit(self.background[self.current_text], self.background[self.current_text].get_rect())


    def finish(self, data):
        pass
