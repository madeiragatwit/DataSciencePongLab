import pygame
import random
#from random import seed
#from random import choice
from paddle import Paddle
from ball import Ball
from collections import namedtuple

def main():
    pygame.init()

    pygame.display.set_caption("Lab2")
    WIDTH = 800
    HEIGHT = 400
    BORDER = 20
    VELOCITY = 5
    FPS = 60
    #seed(1)

    myConstants = namedtuple("MyConstants", ["WIDTH", "HEIGHT", "BORDER", "VELOCITY", "FPS"])
    CONSTANTS = myConstants(WIDTH, HEIGHT, BORDER, VELOCITY, FPS)

    screen = pygame.display.set_mode((WIDTH,HEIGHT))


    #walls
    wall_color = pygame.Color("sky blue")
    #Top Wall
    pygame.draw.rect(screen, wall_color, ((0,0),(WIDTH, BORDER)))
    #Side Wall
    pygame.draw.rect(screen, wall_color, ((0,0),(BORDER, HEIGHT)))
    #Bottom Wall
    pygame.draw.rect(screen, wall_color, ((0,HEIGHT-BORDER),(WIDTH, BORDER)))

    #Ball init
    x0 = WIDTH - Ball.RADIUS
    y0 = HEIGHT // 2

    #TODO: +/- 45 degree/random
    directionY = random.choice((-1,1))
    
    vx0 = -VELOCITY
    vy0 = directionY * VELOCITY


    b0 = Ball(x0,y0, vx0,vy0, pygame.Color("blue"), screen, CONSTANTS)
    b0.show(pygame.Color("blue"))

    #Update Window
    pygame.display.update()
    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()    
    
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        pygame.display.update()
        clock.tick(FPS)
        #Ball
        b0.update()

if __name__=="__main__":
    # call the main function
    main()