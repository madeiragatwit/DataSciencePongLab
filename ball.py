import pygame
from pygame import constants

class Ball:
    #class variables
    RADIUS = 12

    def __init__(self, x,y, vx,vy, color, screen, CONSTANTS):
        #instance variables
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.screen = screen
        self.CONSTANTS = CONSTANTS

    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x,self.y), self.RADIUS)

    def update(self):
        #new position = old postion + delta position
        #delete old ball
        self.show(pygame.Color("black"))

        #predicted movement
        px = self.x + self.vx
        py = self.y + self.vy

        #Change direction
        #Check if I'm colliding into wall:
            #flip velocity
            
        #Left Wall
        if px < (self.CONSTANTS.BORDER + self.RADIUS):
            self.vx = -self.vx

        #Top+Bottom Walls
        if py > (self.CONSTANTS.HEIGHT-self.RADIUS-self.CONSTANTS.BORDER):
            self.vy = -self.vy
        elif py < (self.CONSTANTS.BORDER+self.RADIUS):
            self.vy = -self.vy

        #Change position
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(self.color)

