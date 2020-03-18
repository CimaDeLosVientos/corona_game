import pygame, os, random, time as tim
from pygame.locals import *
from src.helpers import *
from src.things import Soap
from src.player import Player




#------------- Init -------------

# Constants
WIDTH = 1366
HEIGHT = 720

# Display a window of 1366x720
window = pygame.display.set_mode([WIDTH, HEIGHT])
image_scene_livingroom = load_image("assets/images/scenes/livingroom.png")

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
        time = clock.tick(30)
        print(len(things.sprites()))

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

# on_event function, 
def on_event(time, event):
    if pygame.KEYDOWN:
        keys = pygame.key.get_pressed()

        # players controls
        player.actionKeyboard(keys, time)


def on_update(time):
    # Scene
    global countdown
    countdown -= time
    #print(int(countdown / 1000))

    # Things
    if random.random() < 0.5:
        things.add(Soap(((random.randrange(WIDTH), 50))))
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
    player.update()

    # Scores


#Main function
if __name__ == '__main__':
    pygame.init()
    loop()
