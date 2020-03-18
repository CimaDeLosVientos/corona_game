import pygame, os, random, time as tim
from pygame.locals import *
from src.helpers import *
from src.things import Soap

# Init
things = pygame.sprite.Group()
things.add(Soap((50,50)))

# Init objets and player
#player = Survival()


#Game itself
def loop():
    #------------- Init -------------
    # Display a window of 1366x720
    window = pygame.display.set_mode([1366,720])

    # Window name
    pygame.display.set_caption("corona_game")

    # Variables
    quit_flag = False
    clock = pygame.time.Clock()

    #Options
    pygame.key.set_repeat(10)

    #Characters

    #--------------------------------

    while not quit_flag:
        time = clock.tick(30)

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_flag = True

            # detect events
            #on_event(time, event)

        # update scene (stuff)
        on_update(time)

        # redraw the screen
        on_draw(window, "sd")
        pygame.display.flip()

#on_event function, 
#def on_event(time, event):
#    if pygame.KEYDOWN:
#        keys = pygame.key.get_pressed()
#
#        # Controles Player1
#        player1.actionKeyboard(keys, time)
#
#        # Controles Player2
#        player2.actionKeyboard(keys, time)

def on_update(time):
    pass
    #global countdown

    #if countdown > 0:

        #player1.update()
        #player2.update()

        #countdown -= time/1000

       # if player1.bang:
       #     bullets.add(Bullet(player1.bang[0], player1.bang[1]))
       #     player1.bang = None


        #bullets.update("player1")


#    #The game ends when the timmer count to 0 or some player's life goes to 0
#    if countdown <= 0 or len(player1.heart) == 0 or len(player2.heart) == 0:
#        tim.sleep(5)
#        sys.exit(0)

def on_draw(window, tileMap):
    # Clear the window
    window.fill((0, 0, 0)) ## Comprobar si lo puedo quitar porque es poner en blanco y en teoria lo voy a pintar todo

    # Draw the map
    

    # Draw things
    for thing in things:
        thing.update("ww")
        window.blit(thing.image, thing.rect)

    #Draw the timmer
    #timeCD, time_rect = draw_text(str(int(countdown)), 768+32, 768/2, 30)
    #window.blit(timeCD, time_rect)
    #Draw the characters
    #window.blit(player1.image, player1.rect)
    #window.blit(player2.image, player2.rect)
    #Draw lifes
    #for heart in player1.heart:
    #    window.blit(heart[0], heart[1])
    #for heart in player2.heart:
    #    window.blit(heart[0], heart[1])

#Main function
if __name__ == '__main__':
    pygame.init()
    loop()
