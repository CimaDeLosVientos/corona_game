import pygame, os, random, time as tim
from pygame.locals import *
from .scene import Scene
from .helpers import *
from .things import Steak, Salad, SpoiledSteak
from .player import Player
from .parameters import *

class Level4Introduction(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.next = None
        self.background = load_image("assets/images/scenes/kitchen.png")
        self.chat = []
        self.current_chat = -1
        for i in range(6):
            self.chat.append(pygame.transform.scale(load_image("assets/images/scenes/4-{}.png".format(i)), CHAT_SURFACE))
        self.chat_rect = self.chat[0].get_rect()
        self.chat_rect.center = (int(WIDTH / 2) , int(HEIGHT / 2))

        # Next chat button
        self.next_chat_button = load_image("assets/images/buttons/next_chat_button.png")
        self.next_chat_button_rect = self.next_chat_button.get_rect()
        self.next_chat_button_rect.center = NEXT_CHAT_BUTTON

        self.mouse_state = 1 # Up


    def load(self, data):
        self.__init__()


    def on_event(self, time, event):
        mouse_press = pygame.mouse.get_pressed()[0]
        if (mouse_press and self.mouse_state == 1):
            self.mouse_state = 0
        if (not mouse_press and self.mouse_state == 0):
            self.current_chat += 1
            self.mouse_state = 1
            if self.current_chat == len(self.chat):
                self.next = "level_4_1"


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



class Level4Play(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.background = load_image("assets/images/scenes/kitchen.png")
        self.object_1_icon = Steak(OBJECT_1_ICON_LOCATION)
        self.object_2_icon = Salad(OBJECT_2_ICON_LOCATION)
        self.bad_objects = [SpoiledSteak] # Class pointers

        # Variables
        self.things = pygame.sprite.Group()
        self.countdown = LEVEL_TIME * 1000
        self.start = False
        self.end_completed = False
        self.end_failed_time = False
        self.end_failed_healt = False
        self.mouse_state = 1 # Up

        #Characters
        self.player = Player("keyboard", int(WIDTH / 2), GROUND_LEVEL)

        # Buttons
        ## Start level button
        self.start_level_button = load_image("assets/images/buttons/start_level_button.png")
        self.start_level_button_rect = self.start_level_button.get_rect()
        self.start_level_button_rect.center = START_LEVEL_BUTTON

        ## Next level button
        self.next_level_button = load_image("assets/images/buttons/next_level_button.png")
        self.next_level_button_rect = self.next_level_button.get_rect()
        self.next_level_button_rect.center = NEXT_LEVEL_BUTTON

        ## Exit button
        self.exit_button = load_image("assets/images/buttons/exit_button.png")
        self.exit_button_rect = self.exit_button.get_rect()
        self.exit_button_rect.center = EXIT_BUTTON


    def load(self, data):
        self.__init__()
        self.player.healt = data["healt_player"]


    def on_event(self, time, event):
        mouse_press = pygame.mouse.get_pressed()[0]
        if (mouse_press and self.mouse_state == 1):
            self.mouse_state = 0
        if (not mouse_press and self.mouse_state == 0):
            if not self.start:
                self.start = True
            elif self.end_completed == True:
                self.next = "level_5_0"
            elif self.end_failed_time == True or self.end_failed_healt == True:
                self.next = "main_menu"
            self.mouse_state = 1
        else:
            keys = pygame.key.get_pressed()

            # players controls
            self.player.actionKeyboard(keys, time)


    def on_update(self, time):
        if not self.start:
            return
        elif self.countdown <= 0:
            self.end_failed_time = True
            return
        elif self.player.healt <= 0:
            self.end_failed_healt = True
            return
        elif (self.player.score["steak"] >= OBJECT_1_NEEDS_LEVEL_1
            and self.player.score["salad"] >= OBJECT_2_NEEDS_LEVEL_1):
            self.end_completed = True
            return
        self.countdown -= time

        # Things generation
        lottery = random.random()
        if lottery < RATIO_OBJECT_1_LEVEL_1:
            self.things.add(Steak(((random.randrange(LEFT_LIMIT, RIGHT_LIMIT), -50))))
        elif lottery < RATIO_OBJECT_2_LEVEL_1:
            self.things.add(Salad(((random.randrange(LEFT_LIMIT, RIGHT_LIMIT), -50))))
        elif lottery < RATIO_BAD_OBJECT_LEVEL_1:
            self.things.add(random.choice(self.bad_objects)(((random.randrange(LEFT_LIMIT, RIGHT_LIMIT), -50))))

        self.things.update(time, self.player)

        # Character
        self.player.update()


    def on_draw(self, screen):
        # Clear the screen
        screen.fill((0, 0, 0)) ## Comprobar si lo puedo quitar porque es poner en blanco y en teoria lo voy a pintar todo

        # Scene
        screen.blit(self.background, self.background.get_rect())
        if not self.start:
            screen.blit(self.start_level_button, self.start_level_button_rect)

        # Things
        for thing in self.things:
            screen.blit(thing.image, thing.rect)

        # Character
        screen.blit(self.player.image, self.player.rect) 
        
        # Scores
        screen.blit(self.object_1_icon.image, self.object_1_icon.rect)
        object_1_score, object_1_score_rect = draw_text(str(self.player.score["steak"]), OBJECT_1_COUNTER_LOCATION[0], OBJECT_1_COUNTER_LOCATION[1])
        screen.blit(object_1_score, object_1_score_rect)

        screen.blit(self.object_2_icon.image, self.object_2_icon.rect)
        object_2_score, object_2_score_rect = draw_text(str(self.player.score["salad"]), OBJECT_2_COUNTER_LOCATION[0], OBJECT_2_COUNTER_LOCATION[1])
        screen.blit(object_2_score, object_2_score_rect)

        countdown_timmer, countdown_timmer_rect = draw_text(str(int(self.countdown / 1000)), TIMER_LOCATION[0], TIMER_LOCATION[1])
        screen.blit(countdown_timmer, countdown_timmer_rect)

        width_healt_bar = INITIAL_HEALT * HEALT_BAR_PORTION_SIZE[0]
        healt_bar = pygame.Surface((width_healt_bar, HEALT_BAR_PORTION_SIZE[1]))
        healt_bar.fill((255,200,200))
        screen.blit(healt_bar, (HEALT_LOCATION[0] - int(width_healt_bar / 2), HEALT_LOCATION[1]))

        width_current_healt_bar = max(0, self.player.healt * HEALT_BAR_PORTION_SIZE[0])
        current_healt_bar = pygame.Surface((width_current_healt_bar, HEALT_BAR_PORTION_SIZE[1]))
        current_healt_bar.fill((255,0,0))
        screen.blit(current_healt_bar, (HEALT_LOCATION[0] - int(width_current_healt_bar / 2), HEALT_LOCATION[1]))

        # Finished
        if self.end_failed_time:
            screen.blit(self.exit_button, self.exit_button_rect)
        elif self.end_failed_healt:
            screen.blit(self.exit_button, self.exit_button_rect)
        elif self.end_completed:
            screen.blit(self.next_level_button, self.next_level_button_rect)


    def finish(self, data):
        data["healt_player"] = self.player.healt
