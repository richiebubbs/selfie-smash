#selfie smash
# I received a lot of help with the main game loop from: https://pythonprogramming.net/game-development-tutorials/


import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,255)

bright_red = (255,0,0)
bright_green = (0,255,0)

obstacle_color = (238,130,238) #I went with violet, NYU Pride!

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
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(count), True, black)
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
    largeText = pygame.font.Font("freesansbold.ttf", 96)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()
    #time.sleep(2)
    

def smash():
    largeText = pygame.font.Font("freesansbold.ttf", 72)
    TextSurf, TextRect = text_objects("YOU GOT SMASHED!", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("REPLAY!", 150,450,100,50, green, bright_green, "play" )
        button("EXIT", 550,450,100,50, red, bright_red, "quit")
        
        pygame.display.update()
        clock.tick(15)

# I got help with the following from the screencast https://youtu.be/P-UuVITG7Vg?list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO
def button(message,x,y,w,h,i,a,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, a, (x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
    else:    
        pygame.draw.rect(gameDisplay, i, (x,y,w,h))
    
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    TextSurf, TextRect = text_objects(message, smallText)
    TextRect.center = ( (x + (w/2)), (y + (h/2)))
    gameDisplay.blit(TextSurf, TextRect)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf", 96)
        TextSurf, TextRect = text_objects("SELFIE SMASH!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("PLAY!", 150,450,100,50, green, bright_green, "play" )
        button("EXIT", 550,450,100,50, red, bright_red, "quit")

        pygame.display.update()
        clock.tick(15)

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    #here we tell the computer where the objects will start in the game display:

    thing_startx = random.randrange(0, display_width) #the range is between 0 and the max of whatever our display width is
    thing_starty = -600 # this tells it to always start at the very top of the display
    thing_speed = 9 # i played around with speed, but anything slower is a bit boring
    thing_width = 100
    thing_height = 150

    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() # this basically quits the game loop if the user closes the game window

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5 #basically, if the user presses the left arrow key, move the selfie 5 pixels to the left
                if event.key == pygame.K_RIGHT:
                    x_change = 5 #if the user presses the right arrow key, move the selfie 5 pixels to the right
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0 # if the key is unpressed, the selfie stops

        x += x_change #this creates the movement of the selfie by changing the x corresponding to the left or right movement defined above
        gameDisplay.fill(white)
        #the following code calls the function 'things' i.e. the obstacles get drawn in the positions defined by thingx thingy, etc.: 
        things(thing_startx, thing_starty, thing_width, thing_height, obstacle_color)
    
        thing_starty += thing_speed
        selfie(x,y)
        things_dodged(dodged)
    
        #this is how the system knows if we have hit the object:
    
        if x > display_width - selfie_width or x < 0:
            smash()
    
        # here's where the real fun begins, the following says if you dodge the obstacle, the score will increase by one, and the obstacles will speed up and increase in size by 20% making it more difficult as you score more points
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)
    
        if y < thing_starty+thing_height:
            print("y crossover")

            if x > thing_startx and x < thing_startx + thing_width or x+selfie_width > thing_startx and x + selfie_width < thing_startx+thing_width:
                print("x crossover")
                smash()
    
        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()

