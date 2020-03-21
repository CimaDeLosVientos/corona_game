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
        self.music = "assets/music/Phillip_Gross_-_03_-_Optimistic_Bits.mp3"
        self.sound_notification = load_sound("assets/sounds/notification.wav")
        self.background = load_image("assets/images/scenes/livingroom.png")
        self.chat = []
        self.chat.append(pygame.transform.scale(load_image("assets/images/scenes/0-0.png"), CHAT_SURFACE))
        self.current_chat = -1
        self.chat_rect = self.chat[0].get_rect()
        self.chat_rect.center = (int(WIDTH / 2) , int(HEIGHT / 2))

        # Next chat button
        self.next_chat_button = load_image("assets/images/buttons/next_chat_button.png")
        self.next_chat_button_rect = self.next_chat_button.get_rect()
        self.next_chat_button_rect.center = NEXT_CHAT_BUTTON

        self.mouse_state = 1 # Up


    def load(self, data):
        self.__init__()
        load_music(self.music)
        pygame.mixer.music.play(-1)
        for i in range(1, 6):
            self.chat.append(pygame.transform.scale(load_image("assets/images/scenes/0-{}.png".format(i)), CHAT_SURFACE))

    def on_event(self, time, event):
        mouse_press = pygame.mouse.get_pressed()[0]
        if (mouse_press and self.mouse_state == 1):
            self.mouse_state = 0
        if (not mouse_press and self.mouse_state == 0):
            self.current_chat += 1
            self.sound_notification.play()
            self.mouse_state = 1
            if self.current_chat == len(self.chat):
                self.next = "level_1_0"


    def on_update(self, time):
        pass


    def on_draw(self, screen):
        # Clear the screen
        screen.fill((0, 0, 0)) ## Comprobar si lo puedo quitar porque es poner en blanco y en teoria lo voy a pintar todo

        # Scene
        if self.current_chat >= 0 and self.current_chat < len(self.chat):
            screen.blit(self.chat[self.current_chat], self.chat_rect)

        # Buttons
        screen.blit(self.next_chat_button, self.next_chat_button_rect)

    def finish(self, data):
        pass
