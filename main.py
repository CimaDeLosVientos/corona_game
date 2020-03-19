import pygame, os, random, time as tim
from pygame.locals import *
from src.helpers import *
from src.things import Soap, Video
from src.player import Player
from src.parameters import *

#------------- Init -------------
# Display
window = pygame.display.set_mode([WIDTH, HEIGHT])
image_scene_livingroom = load_image("assets/images/scenes/livingroom.png")
# image_score_soap = Soap((WIDTH - 80, 51))
object_1_icon = Soap(OBJECT_1_ICON_LOCATION)
object_2_icon = Video(OBJECT_2_ICON_LOCATION)

# Window name
pygame.display.set_caption("corona_game")

# Variables
things = pygame.sprite.Group()
clock = pygame.time.Clock()
countdown = LEVEL_TIME * 1000
## Scores
num_soap = 0

#Options
pygame.key.set_repeat(10)

#Characters
player = Player("keyboard", int(HEIGHT/2), GROUND_LEVEL)

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
        things.add(Soap(((random.randrange(LEFT_LIMIT, RIGHT_LIMIT), -50))))
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
    window.blit(object_1_icon.image, object_1_icon.rect)
    object_1_score, object_1_score_rect = draw_text(str(player.score["soap"]), OBJECT_1_COUNTER_LOCATION[0], OBJECT_1_COUNTER_LOCATION[1])
    window.blit(object_1_score, object_1_score_rect)

    window.blit(object_2_icon.image, object_2_icon.rect)
    object_2_score, object_2_score_rect = draw_text(str(player.score["video"]), OBJECT_2_COUNTER_LOCATION[0], OBJECT_2_COUNTER_LOCATION[1])
    window.blit(object_2_score, object_2_score_rect)

    countdown_timmer, countdown_timmer_rect = draw_text(str(int(countdown / 1000)), TIMER_LOCATION[0], TIMER_LOCATION[1])
    window.blit(countdown_timmer, countdown_timmer_rect)

    width_healt_bar = INITIAL_HEALT * HEALT_BAR_PORTION_SIZE[0]
    healt_bar = pygame.Surface((width_healt_bar, HEALT_BAR_PORTION_SIZE[1]))
    healt_bar.fill((255,200,200))
    window.blit(healt_bar, (HEALT_LOCATION[0] - int(width_healt_bar / 2), HEALT_LOCATION[1]))

    width_current_healt_bar = player.healt * HEALT_BAR_PORTION_SIZE[0]
    current_healt_bar = pygame.Surface((width_current_healt_bar, HEALT_BAR_PORTION_SIZE[1]))
    current_healt_bar.fill((255,0,0))
    window.blit(current_healt_bar, (HEALT_LOCATION[0] - int(width_current_healt_bar / 2), HEALT_LOCATION[1]))


    #s = pygame.Surface((1000,750))  # the size of your rect
    #s.set_alpha(128)                # alpha level
    #s.fill((255,255,255))           # this fills the entire surface
    #window.blit(s, (0,0))


if __name__ == '__main__':
    pygame.init()
    loop()
