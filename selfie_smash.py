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

# for the next section I got a lot of help from https://pythonprogramming.net/game-development-tutorials/ and https://inventwithpython.com/invent4thed/
# I also played around with fonts here with help from https://stackoverflow.com/questions/38001898/what-fonts-can-i-use-with-pygame-font-font
def things_dodged(count):
    font = pygame.font.chalkboardttc(None, 25)
    text = font.render("Score: " + str(count), True, black)
    gameDisplay.blit(text, (0,0))

#I experimented with other shapes, but the rectangle is easiest to use as an obstacle.  So I went with that
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color,[thingx, thingy, thingw, thingh])

#this next bit of code defines the selfie's position

def selfie(x,y):
    gameDisplay.blit(SelfieImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("optimattc", 96)
    TextSurf, TextRect = text_objects(text, largeText)
    TexRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

pygame.display.update()
