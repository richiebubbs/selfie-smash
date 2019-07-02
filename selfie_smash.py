#selfie smash
# I received a lot of help with the main game loop from: https://pythonprogramming.net/game-development-tutorials/


import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0.0)
white = (255,255,255)
red = (255,0,0)

obstacle_color = (43,58,77)

selfie_width = 73

# setup the main display:
# here we use the variables created above instead of hard coding the game display w and h so if we need to change we can do it easily
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Selfie Smash!")
clock = pygame.time.Clock()
#load the image that the user saved in the main directory:
SelfieImg0 = pygame.image.load("Selfie.jpg")
# my image kept coming out sideways, so I use the following to rotate the image, hopefully this works for all users?
SelfieImg1 = pygame.transform.rotate(SelfieImg0, 270)
# here I scale the image, so that it is the appropriate size:
# I got help with this step from https://www.pygame.org/docs/ref/transform.html
SelfieImg = pygame.transform.smoothscale(SelfieImg1, (73,90))

