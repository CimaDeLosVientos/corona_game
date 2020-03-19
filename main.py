import pygame, os, random, time as tim
from pygame.locals import *
from src.helpers import *
from src.things import Soap, Video
from src.player import Player
from src.parameters import *
from src.level_1 import *



class Director:
    """Representa el objeto principal del juego.

    El objeto Director mantiene en funcionamiento el juego, se
    encarga de actualizar, dibuja y propagar eventos.

    Tiene que utilizar este objeto en conjunto con objetos
    derivados de Scene."""

    def __init__(self, scenes, data):
        # Display
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])

        # screen name
        pygame.display.set_caption("corona_game")

        # Variables
        self.clock = pygame.time.Clock()
        self.quit_flag = False

        #Options
        pygame.key.set_repeat(10)

        self.scenes = scenes
        self.current_scene = self.scenes["init"]
        self.data = data

    def run(self):
        while not self.quit_flag:
            time = self.clock.tick(60)

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
    pygame.init()
    data = {}
    scenes = {
        "init" : Level1Introduction()#Level1Livingroom()
    }
    director = Director(scenes, data)
    director.run()

