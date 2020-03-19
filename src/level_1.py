import pygame, os, random, time as tim
from pygame.locals import *
from .scene import Scene
from .helpers import *
from .things import Soap, Video
from .player import Player
from .parameters import *

class Level1Livingroom(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.background = load_image("assets/images/scenes/livingroom.png")
        # image_score_soap = Soap((WIDTH - 80, 51))
        self.object_1_icon = Soap(OBJECT_1_ICON_LOCATION)
        self.object_2_icon = Video(OBJECT_2_ICON_LOCATION)

        # Variables
        self.things = pygame.sprite.Group()
        self.countdown = LEVEL_TIME * 1000

        #Characters
        self.player = Player("keyboard", int(HEIGHT/2), GROUND_LEVEL)


    def on_event(self, time, event):
        if pygame.KEYDOWN:
            keys = pygame.key.get_pressed()

            # players controls
            self.player.actionKeyboard(keys, time)


    def on_update(self, time):
        self.countdown -= time

        # Things
        if random.random() < 0.5:
            self.things.add(Soap(((random.randrange(LEFT_LIMIT, RIGHT_LIMIT), -50))))
        self.things.update(self.player)

        # Character
        self.player.update()


    def on_draw(self, screen):
        # Clear the screen
        screen.fill((0, 0, 0)) ## Comprobar si lo puedo quitar porque es poner en blanco y en teoria lo voy a pintar todo

        # Scene
        screen.blit(self.background, self.background.get_rect())

        # Things
        for thing in self.things:
            screen.blit(thing.image, thing.rect)

        # Character
        screen.blit(self.player.image, self.player.rect) 
        
        # Scores
        screen.blit(self.object_1_icon.image, self.object_1_icon.rect)
        object_1_score, object_1_score_rect = draw_text(str(self.player.score["soap"]), OBJECT_1_COUNTER_LOCATION[0], OBJECT_1_COUNTER_LOCATION[1])
        screen.blit(object_1_score, object_1_score_rect)

        screen.blit(self.object_2_icon.image, self.object_2_icon.rect)
        object_2_score, object_2_score_rect = draw_text(str(self.player.score["video"]), OBJECT_2_COUNTER_LOCATION[0], OBJECT_2_COUNTER_LOCATION[1])
        screen.blit(object_2_score, object_2_score_rect)

        countdown_timmer, countdown_timmer_rect = draw_text(str(int(self.countdown / 1000)), TIMER_LOCATION[0], TIMER_LOCATION[1])
        screen.blit(countdown_timmer, countdown_timmer_rect)

        width_healt_bar = INITIAL_HEALT * HEALT_BAR_PORTION_SIZE[0]
        healt_bar = pygame.Surface((width_healt_bar, HEALT_BAR_PORTION_SIZE[1]))
        healt_bar.fill((255,200,200))
        screen.blit(healt_bar, (HEALT_LOCATION[0] - int(width_healt_bar / 2), HEALT_LOCATION[1]))

        width_current_healt_bar = self.player.healt * HEALT_BAR_PORTION_SIZE[0]
        current_healt_bar = pygame.Surface((width_current_healt_bar, HEALT_BAR_PORTION_SIZE[1]))
        current_healt_bar.fill((255,0,0))
        screen.blit(current_healt_bar, (HEALT_LOCATION[0] - int(width_current_healt_bar / 2), HEALT_LOCATION[1]))
