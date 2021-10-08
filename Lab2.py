import pygame

def main():
    pygame.init()

    pygame.display.set_caption("Lab2")
    WIDTH = 800
    HEIGHT = 400
    screen = pygame.display.set_mode((WIDTH,HEIGHT))


    #walls
    wall_color = pygame.Color("sky blue")
    L_WIDTH = 20
    #Top Wall
    pygame.draw.rect(screen, wall_color, ((0,0),(WIDTH, L_WIDTH)))
    #Side Wall
    pygame.draw.rect(screen, wall_color, ((0,0),(L_WIDTH, HEIGHT)))
    #Bottom Wall
    pygame.draw.rect(screen, wall_color, ((0,HEIGHT-L_WIDTH),(WIDTH, L_WIDTH)))

    #Update Window
    pygame.display.update()
    # define a variable to control the main loop
    running = True
        
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

if __name__=="__main__":
    # call the main function
    main()