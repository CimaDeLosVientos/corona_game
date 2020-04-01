import pygame, os, random, time as tim
from pygame.locals import *
from src.helpers import *
from src.things import *
from src.player import Player
from src.parameters import *
from src.main_menu import *
from src.introduction import *
from src.bobi_scene import *



class Director:
    """Representa el objeto principal del juego.

    El objeto Director mantiene en funcionamiento el juego, se
    encarga de actualizar, dibuja y propagar eventos.

    Tiene que utilizar este objeto en conjunto con objetos
    derivados de Scene."""

    def __init__(self, scenes, data):
        # Display
        #self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT], flags = pygame.FULLSCREEN)


        # Screen name
        pygame.display.set_caption("corona_game")

        # Icon
        icon = load_image("assets/images/bobi_icon.png")
        pygame.display.set_icon(icon)
        # Variables
        self.clock = pygame.time.Clock()
        self.quit_flag = False

        #Options
        pygame.key.set_repeat(10)
        pygame.mixer.music.set_volume(MASTER_VOLUMEN)

        self.scenes = scenes
        self.current_scene = self.scenes["init"]
        self.data = data

    def presentation_screen(self, path):
        screen_image = load_image(path)
        self.screen.blit(screen_image, screen_image.get_rect())
        pygame.display.flip()

    def run(self):
        self.current_scene = self.scenes["init"]
        self.current_scene.load(self.data) # Se le manda el diccionario de datos para que se configure.
        while not self.quit_flag:
            time = self.clock.tick(60) # Must be in loop
            # Eventos de Salida
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()

                # detecta eventos
                self.current_scene.on_event(time, event)
            # actualiza la escena
            self.current_scene.on_update(time)

            # dibuja la pantalla
            self.current_scene.on_draw(self.screen)
            pygame.display.flip()

            if self.current_scene.next:
                self.change_scene()

    def change_scene(self):
        self.current_scene.finish(self.data) # Se le manda el diccionario de datos para que lo actualice.
        self.current_scene = self.scenes[self.current_scene.next]
        self.current_scene.load(self.data) # Se le manda el diccionario de datos para que se configure.

    def quit(self):
        self.quit_flag = True

    #s = pygame.Surface((1000,750))  # the size of your rect
    #s.set_alpha(128)                # alpha level
    #s.fill((255,255,255))           # this fills the entire surface
    #screen.blit(s, (0,0))


if __name__ == '__main__':
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    pygame.init()

    scenes = {"init" : 1,}
    data = {}
    director = Director(scenes, data)
    director.presentation_screen("assets/images/presentation_screen.png")

    data = {
        "health_player" : INITIAL_HEALTH,
        "level_1" : {
            "music" : "Phillip_Gross_-_03_-_Die_Stadtmusikanten.mp3",
            "background" : "pizzeria.png",
            "good_objets" : [(Pizza, 0.2, 10), (Soap, 0.2, 10)],
            "bad_objets" : [HotDog],
            "new_object_probability" : 0.1,
            "level_time" : 100
        },
        "level_2" : {
            "music" : "Phillip_Gross_-_04_-_Silver_Danger.mp3",
            "background" : "supermarket.png",
            "good_objets" : [(Steak, 0.2, 10), (ToiletPaper, 0.2, 10)],
            "bad_objets" : [Chips],
            "new_object_probability" : 0.1,
            "level_time" : 100
        },
        "level_3" : {
            "music" : "Phillip_Gross_-_04_-_RaST.mp3",
            "background" : "livingroom.png",
            "good_objets" : [(Video, 0.2, 10), (Soap, 0.2, 10)],
            "bad_objets" : [LowBattery],
            "new_object_probability" : 0.1,
            "level_time" : 100
        },
        "level_4" : {
            "music" : "01_-_Man.mp3",
            "background" : "kitchen.png",
            "good_objets" : [(Salad, 0.2, 10), (Soap, 0.2, 10)],
            "bad_objets" : [SpoiledSteak],
            "new_object_probability" : 0.1,
            "level_time" : 100
        },
        "level_5" : {
            "music" : "Phillip_Gross_-_02_-_Der_Ton_Macht_Die_Musik.mp3",
            "background" : "supermarket.png",
            "good_objets" : [(Steak, 0.2, 10), (ToiletPaper, 0.2, 10)],
            "bad_objets" : [Chips],
            "new_object_probability" : 0.1,
            "level_time" : 100
        }
    }
    scenes = {
        "init" : MainMenu(),
        "main_menu" : MainMenu(),
        "play_menu" : PlayMenu(),
        "how_to_play" : HowPlay(),
        "credits" : Credits(),
        "story_init" : IntroductionScene(0),
        "level_1_0" : ChatScene(1),
        "level_1_1" : PlayScene(data["level_1"], 1),
        "level_2_0" : ChatScene(2),
        "level_2_1" : PlayScene(data["level_2"], 2),
        "level_3_0" : ChatScene(3),
        "level_3_1" : PlayScene(data["level_3"], 3),
        "level_4_0" : ChatScene(4),
        "level_4_1" : PlayScene(data["level_4"], 4),
        "level_5_0" : ChatScene(5),
        "level_5_1" : PlayScene(data["level_5"], 5),
        "level_6_0" : EpilogueScene(6),
    }
    
    director.data = data
    director.scenes = scenes
    director.run()