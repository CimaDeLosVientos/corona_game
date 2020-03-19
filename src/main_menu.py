import pygame, os, random, time as tim
from pygame.locals import *
from .scene import Scene
from .helpers import *
from .things import Soap, Video
from .player import Player
from .parameters import *

class MainMenu(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.next = None
        self.background = load_image("assets/images/scenes/main_menu.png")

        # Play button
        self.play_button = pygame.Surface((100, 50))
        self.play_button.fill((255,255,0))
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.center = (700, 200)
        
        # How to play button
        self.how_play_button = pygame.Surface((100, 50))
        self.how_play_button.fill((255,255,0))
        self.how_play_button_rect = self.how_play_button.get_rect()
        self.how_play_button_rect.center = (700, 200)

        # Credits button
        self.credits_button = pygame.Surface((100, 50))
        self.credits_button.fill((255,255,0))
        self.credits_button_rect = self.credits_button.get_rect()
        self.credits_button_rect.center = (700, 200)
        
        # Exit button
        #self.exit_button = pygame.Surface((100, 50))
        #self.exit_button.fill((255,255,0))
        #self.exit_button_rect = self.exit_button.get_rect()
        #self.exit_button_rect.center = (700, 200)

        self.mouse_state = 1 # Up


    def load(self, data):
        pass


    def on_event(self, time, event):
        mouse_press = pygame.mouse.get_pressed()[0]
        if (mouse_press and self.button_state == 1):
            self.button_state = 0
        if (not mouse_press and self.button_state == 0):
			if self.play_button_rect.collidepoint(pygame.mouse.get_pos()):
				self.next = "play_menu"
			if self.how_play_button_rect.collidepoint(pygame.mouse.get_pos()):
				self.next = "how_to_play"
			if self.credits_button_rect.collidepoint(pygame.mouse.get_pos()):
				self.next = "credits"
			#if self.exit_button_rect.collidepoint(pygame.mouse.get_pos()):
			#	self.next = ""
        else:
        	self.button_state = 1


    def on_update(self, time):
        pass


    def on_draw(self, screen):
        # Clear the screen
        screen.fill((0, 0, 0)) ## Comprobar si lo puedo quitar porque es poner en blanco y en teoria lo voy a pintar todo

        # Scene
        screen.blit(self.background, self.background.get_rect())
        
        # # Scores
        # screen.blit(self.object_1_icon.image, self.object_1_icon.rect)
        # object_1_score, object_1_score_rect = draw_text(str(self.player.score["soap"]), OBJECT_1_COUNTER_LOCATION[0], OBJECT_1_COUNTER_LOCATION[1])
        # screen.blit(object_1_score, object_1_score_rect)

        # screen.blit(self.object_2_icon.image, self.object_2_icon.rect)
        # object_2_score, object_2_score_rect = draw_text(str(self.player.score["video"]), OBJECT_2_COUNTER_LOCATION[0], OBJECT_2_COUNTER_LOCATION[1])
        # screen.blit(object_2_score, object_2_score_rect)

        # countdown_timmer, countdown_timmer_rect = draw_text(str(int(self.countdown / 1000)), TIMER_LOCATION[0], TIMER_LOCATION[1])
        # screen.blit(countdown_timmer, countdown_timmer_rect)

        # width_healt_bar = INITIAL_HEALT * HEALT_BAR_PORTION_SIZE[0]
        # healt_bar = pygame.Surface((width_healt_bar, HEALT_BAR_PORTION_SIZE[1]))
        # healt_bar.fill((255,200,200))
        # screen.blit(healt_bar, (HEALT_LOCATION[0] - int(width_healt_bar / 2), HEALT_LOCATION[1]))

        # width_current_healt_bar = self.player.healt * HEALT_BAR_PORTION_SIZE[0]
        # current_healt_bar = pygame.Surface((width_current_healt_bar, HEALT_BAR_PORTION_SIZE[1]))
        # current_healt_bar.fill((255,0,0))
        # screen.blit(current_healt_bar, (HEALT_LOCATION[0] - int(width_current_healt_bar / 2), HEALT_LOCATION[1]))


        screen.blit(self.button, self.button_rect)


    def finish(self, data):
        pass


class PlayMenu(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.next = None
        self.background = load_image("assets/images/scenes/play_menu.png")

        # Story button
        self.story_button = pygame.Surface((100, 50))
        self.story_button.fill((255,255,0))
        self.story_button_rect = self.story_button.get_rect()
        self.story_button_rect.center = (700, 200)
        
        # Survival button
        self.survival_button = pygame.Surface((100, 50))
        self.survival_button.fill((255,255,0))
        self.survival_button_rect = self.survival_button.get_rect()
        self.survival_button_rect.center = (700, 200)

        # Back button
        self.back_button = pygame.Surface((100, 50))
        self.back_button.fill((255,255,0))
        self.back_button_rect = self.back_button.get_rect()
        self.back_button_rect.center = (700, 200)

        self.mouse_state = 1 # Up

    def load(self, data):
        pass


    def on_event(self, time, event):
        mouse_press = pygame.mouse.get_pressed()[0]
        if (mouse_press and self.button_state == 1):
            self.button_state = 0
        if (not mouse_press and self.button_state == 0):
			if self.story_button_rect.collidepoint(pygame.mouse.get_pos()):
				self.next = "story_init"
			if self.survival_button_rect.collidepoint(pygame.mouse.get_pos()):
				pass
				#self.next = "survival_init"
			if self.back_button_rect.collidepoint(pygame.mouse.get_pos()):
				self.next = "main_menu"
        else:
        	self.button_state = 1


    def on_update(self, time):
        pass


    def on_draw(self, screen):
        # Clear the screen
        screen.fill((0, 0, 0)) ## Comprobar si lo puedo quitar porque es poner en blanco y en teoria lo voy a pintar todo

        # Scene
        screen.blit(self.background, self.background.get_rect())


    def finish(self, data):
        pass


class Credits(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.next = None
        self.background = load_image("assets/images/scenes/credits.png")

        # Back button
        self.back_button = pygame.Surface((100, 50))
        self.back_button.fill((255,255,0))
        self.back_button_rect = self.back_button.get_rect()
        self.back_button_rect.center = (700, 200)

        self.mouse_state = 1 # Up

    def load(self, data):
        pass


    def on_event(self, time, event):
        mouse_press = pygame.mouse.get_pressed()[0]
        if (mouse_press and self.button_state == 1):
            self.button_state = 0
        if (not mouse_press and self.button_state == 0):
			if self.back_button_rect.collidepoint(pygame.mouse.get_pos()):
				self.next = "main_menu"
        else:
        	self.button_state = 1


    def on_update(self, time):
        pass


    def on_draw(self, screen):
        # Clear the screen
        screen.fill((0, 0, 0)) ## Comprobar si lo puedo quitar porque es poner en blanco y en teoria lo voy a pintar todo

        # Scene
        screen.blit(self.background, self.background.get_rect())


    def finish(self, data):
        pass
