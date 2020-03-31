import pygame, os, random, time as tim
from pygame.locals import *
from src.helpers import *
from src.player import Player
from src.parameters import *

class Scene:
    """Representa un escena abstracta del videojuego.
 
    Una escena es una parte visible del juego, como una pantalla
    de presentación o menú de opciones. Tiene que crear un objeto
    derivado de esta clase para crear una escena utilizable."""
 
    def __init__(self):
        self.next = None
   
    def load(self, data):
        "Se llama antes de empezar la ejecución para configurarla según los datos de la partida."
        raise NotImplemented("Tiene que implementar el método on_event.")


    def on_event(self, time, event):
        "Se llama cuando llega un evento especifico al bucle."
        raise NotImplemented("Tiene que implementar el método on_event.")
    

    def on_update(self, time):
        "Actualización lógica que se llama automáticamente desde el director."
        raise NotImplemented("Tiene que implementar el método on_update.")
 
 
    def on_draw(self, screen):
        "Se llama cuando se quiere dibujar la pantalla."
        raise NotImplemented("Tiene que implementar el método on_draw.")

    def finish(self, data):
        "Se llama cuando se quiere pasar a la siguiente escena."
        raise NotImplemented("Tiene que implementar el método on_draw.")

class ChatScene(Scene):
    def __init__(self, level):
        Scene.__init__(self)
        self.level = level
        self.next = None
        self.music = "assets/music/Phillip_Gross_-_03_-_Optimistic_Bits.mp3"
        self.sound_notification = load_sound("assets/sounds/notification.wav")
        self.background = load_image("assets/images/scenes/background_chat.png")
        self.chat = []
        for i in range(6):
            self.chat.append(pygame.transform.scale(load_image("assets/images/scenes/{}-{}.png".format(level, i)), CHAT_SURFACE))
        self.current_chat = -1
        self.chat_rect = self.chat[0].get_rect()
        self.chat_rect.center = (int(WIDTH / 2) , int(HEIGHT / 2))

        # Next chat button
        self.next_chat_button = load_image("assets/images/buttons/next_chat_button.png")
        self.next_chat_button_rect = self.next_chat_button.get_rect()
        self.next_chat_button_rect.center = NEXT_CHAT_BUTTON

        self.mouse_state = 1 # Up


    def load(self, data):
        #self.__init__()
        if not pygame.mixer.music.get_busy():
            load_music(self.music)
            pygame.mixer.music.play(-1)        


    def on_event(self, time, event):
        mouse_press = pygame.mouse.get_pressed()[0]
        if (mouse_press and self.mouse_state == 1):
            self.mouse_state = 0
        if (not mouse_press and self.mouse_state == 0):
            self.current_chat += 1
            self.sound_notification.play()
            self.mouse_state = 1
            if self.current_chat == len(self.chat):
                self.next = "level_{}_1".format(self.level)


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
        



class PlayScene(Scene):
    def __init__(self, data, level):
        Scene.__init__(self)
        self.level = level
        self.music = "assets/music/{}".format(data["music"])
        self.sound_time_over = load_sound("assets/sounds/time_over.wav")
        self.sound_game_over = load_sound("assets/sounds/game_over.wav")
        self.sound_level_completed = load_sound("assets/sounds/level_completed.wav")
        self.background = load_image("assets/images/scenes/{}".format(data["background"]))

        # Things
        self.good_objets_data = data["good_objets"] # List of tuples (object, probability 0-1, needs)
        self.good_objets = []
        for ii in range(len(self.good_objets_data)):
            self.good_objets.append(self.good_objets_data[ii][0](ICON_LOCATIONS[ii]))
        self.bad_objects = data["bad_objets"]
        self.new_object_probability = data["new_object_probability"]
        self.probabilities = [self.good_objets_data[0][1] * self.new_object_probability]
        for ii in range(1, len(self.good_objets_data)):
            self.probabilities.append(self.probabilities[ii-1] + (self.good_objets_data[ii][1] * self.new_object_probability))

        # Variables
        self.things = pygame.sprite.Group()
        self.level_time = self.countdown = data["level_time"] * 1000
        self.start = False
        self.end_completed = False
        self.end_failed_time = False
        self.end_failed_health = False
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
        #self.__init__()
        load_music(self.music)
        pygame.mixer.music.play(-1)
        self.player.health = data["health_player"]
        self.countdown = self.level_time


    def is_completed(self):
        for ii in range(len(self.good_objets)):
            if self.player.score[self.good_objets[ii].name] < self.good_objets_data[ii][2]:
                return False
        return True

    
    def generates_thing(self):
        lottery = random.random()
        for ii in range(len(self.good_objets_data)):
            if lottery < self.probabilities[ii]:
                self.things.add(self.good_objets_data[ii][0]((random.randrange(LEFT_LIMIT, RIGHT_LIMIT), - 50)))
        if lottery < self.probabilities[-1]:
            self.things.add(random.choice(self.bad_objects)((random.randrange(LEFT_LIMIT, RIGHT_LIMIT), - 50)))


    def on_event(self, time, event):
        mouse_press = pygame.mouse.get_pressed()[0]
        if (mouse_press and self.mouse_state == 1):
            self.mouse_state = 0
        if (not mouse_press and self.mouse_state == 0):
            if not self.start:
                self.start = True
            elif self.end_completed == True:
                self.next = "level_{}_0".format(self.level)
            elif self.end_failed_time == True or self.end_failed_health == True:
                self.next = "main_menu"
            self.mouse_state = 1
        else:
            keys = pygame.key.get_pressed()

            # players controls
            self.player.actionKeyboard(keys, time)


    def on_update(self, time):
        if not self.start:
            return
        if pygame.mixer.music.get_busy():
            if self.countdown <= 0:
                self.end_failed_time = True
                self.sound_time_over.play()
                pygame.mixer.music.stop()
                return
            elif self.player.health <= 0:
                self.end_failed_health = True
                self.sound_game_over.play()
                pygame.mixer.music.stop()
                return
            elif self.is_completed():
                self.end_completed = True
                self.sound_level_completed.play()
                pygame.mixer.music.stop()
                return
        else:
            return
        self.countdown -= time

        self.generates_thing()
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
        for ii in range(len(self.good_objets)):
            screen.blit(self.good_objets[ii].image, self.good_objets[ii].rect)
            score, score_rect = draw_text("{}/{}".format(
                str(self.player.score[self.good_objets[ii].name]), str(self.good_objets_data[ii][2])
                ), COUNTER_LOCATIONS[ii][0], COUNTER_LOCATIONS[ii][1])
            screen.blit(score, score_rect)

        countdown_timmer, countdown_timmer_rect = draw_text(str(int(self.countdown / 1000)), TIMER_LOCATION[0], TIMER_LOCATION[1])
        screen.blit(countdown_timmer, countdown_timmer_rect)

        width_health_bar = INITIAL_HEALTH * HEALTH_BAR_PORTION_SIZE[0]
        health_bar = pygame.Surface((width_health_bar, HEALTH_BAR_PORTION_SIZE[1]))
        health_bar.fill((255,200,200))
        screen.blit(health_bar, (HEALTH_LOCATION[0] - int(width_health_bar / 2), HEALTH_LOCATION[1]))

        width_current_health_bar = max(0, self.player.health * HEALTH_BAR_PORTION_SIZE[0])
        current_health_bar = pygame.Surface((width_current_health_bar, HEALTH_BAR_PORTION_SIZE[1]))
        current_health_bar.fill((255,0,0))
        screen.blit(current_health_bar, (HEALTH_LOCATION[0] - int(width_current_health_bar / 2), HEALTH_LOCATION[1]))

        # Finished
        if self.end_failed_time:
            screen.blit(self.exit_button, self.exit_button_rect)
        elif self.end_failed_health:
            screen.blit(self.exit_button, self.exit_button_rect)
        elif self.end_completed:
            screen.blit(self.next_level_button, self.next_level_button_rect)


    def finish(self, data):
        data["health_player"] = self.player.health
        self.things.clear()