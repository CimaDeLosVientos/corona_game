import pygame, os, random, time as tim
from pygame.locals import *
from src.helpers import *
from src.things import Soap
from src.player import Player

#------------- Init -------------

# Constants
WIDTH = 1366
HEIGHT = 720

# Display
window = pygame.display.set_mode([WIDTH, HEIGHT])
image_scene_livingroom = load_image("assets/images/scenes/livingroom.png")
image_score_soap = Soap((WIDTH - 80, 51))

# Window name
pygame.display.set_caption("corona_game")

# Variables
things = pygame.sprite.Group()
clock = pygame.time.Clock()
countdown = 120 * 1000
## Scores
num_soap = 0

#Options
pygame.key.set_repeat(10)

#Characters
player = Player("keyboard", 700, 600)

#--------------------------------

#Game itself
def loop():
    quit_flag = False
    while not quit_flag:
        things.update(player)
        time = clock.tick(30)

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_flag = True

            # detect events
            on_event(time, event)

        # update scene (stuff)
        on_update(time)

        # redraw the screen
        on_draw(window)
        pygame.display.flip()


def on_event(time, event):
    if pygame.KEYDOWN:
        keys = pygame.key.get_pressed()

        # players controls
        player.actionKeyboard(keys, time)


def on_update(time):
    # Scene
    global countdown
    countdown -= time

    # Things
    if random.random() < 0.5:
        things.add(Soap(((random.randrange(WIDTH), -50))))
    things.update(player)

    # Character
    player.update()


def on_draw(window):
    # Clear the window
    window.fill((0, 0, 0)) ## Comprobar si lo puedo quitar porque es poner en blanco y en teoria lo voy a pintar todo

    # Scene
    window.blit(image_scene_livingroom, image_scene_livingroom.get_rect())

    # Things
    for thing in things:
        window.blit(thing.image, thing.rect)

    # Character
    window.blit(player.image, player.rect) 
    
    # Scores
    window.blit(image_score_soap.image, image_score_soap.rect)
    soap_score, soap_score_rect = draw_text(str(player.soap), WIDTH - 50, 50)
    window.blit(soap_score, soap_score_rect)
    countdown_score, countdown_score_rect = soap_score, soap_score_rect = draw_text(str(int(countdown / 1000)), WIDTH / 2, 20)
    window.blit(countdown_score, countdown_score_rect)


if __name__ == '__main__':
    pygame.init()
    loop()
