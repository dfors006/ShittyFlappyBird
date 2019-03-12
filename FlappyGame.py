

import pygame
import random

pygame.init(); 

pygame.mixer.music.load('Afroman.mp3') 
pygame.mixer.music.set_volume(0.75) 
pygame.mixer.music.play(-1)

imageUp = pygame.image.load('Flappy_Up.jpg')
imageUp = pygame.transform.scale(imageUp,(40,40))

imageDown = pygame.image.load('Flappy_Up.jpg') 
imageDown = pygame.transform.scale(imageDown, (30,80))

imageDead = pygame.image.load('DeadFlappy.png') 
imageDead = pygame.transform.scale(imageDead,(25,23))

#background 
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (700,500))

#colors 
black = (0, 0, 0) 
white = (255, 255, 255) 
gren = (0,255,0)
red = (255,0,0)
skyBlue = (0,191,255)
orange = (255,215,0)
gray = (112, 138, 144)


#surface screen size 
size = (700, 500) 
screen = pygame.display.set_mode(size) 

#interface screen title 
pygame.display.set_caption('Flippy bird') 

#boolean T/F to control game logic 
done = False
#clock to control game refresh speed 
clock = pygame.time.Clock() 

x = 350
y = 250

#define global variables to control speed 
x_speed = 0 
y_speed = 0 

ground = 477 
leftWall = 0
rightWall = 700

#x location of obstacle
xloc = 700 
#y location of obstacle 
yloc = 0
#how wide we want obstacle 
xsize = 70 
#how rnadomly tall it is 
ysize = random.randint(0, 350)
#space between two block 
space = 150 
#the speed of the obstacle as they move across the screen 
#pixles per frame/flip 
obspeed = 2.5 
#global score 
score = 0 

#we proceed to define our obstacle 
def obstacle(xloc, yloc,xsize,ysize): 
    #pygame.draw.rect(screen,green, [xloc,yloc,xsize,ysize])
    #pygame.draw.rect(screen,green, [xloc,int(yloc+ysize+space), xsize, ysize+500])

    imgTop = pygame.image.load('pipe2.jpg')
    imgTop = pygame.transform.rotate(imgTop, 180)
    imgTop = pygame.transform.scale(imgTop, (xsize, ysize)) 
    imgBottom = pygame.image.load('pipe2.jpg')
    imgBottom = pygame.transform.scale(imgBottom, (xsize, 500 - ysize))
    screen.blit(imgTop, (xloc, yloc))
    screen.blit(imgBottom, (xloc, int(yloc +ysize + space)))

#define function to draw circle 
def ball(x,y, image):
   # pygame.draw.circle(screen,black,(x,y),20)
   screen.blit(image, (x,y))

def gameover(): 
    font = pygame.font.SysFont(None, 40) 
    text = font.render("game Over ", True, white) 
    screen.blit(text, [150,250])

#function to write score being kept
def Score(score): 
    font = pygame.font.SysFont(None, 75) 
    #we use str to convert score value to string for display 
    text = font.render("Score: "+str(score),True,white)
    #stop left center coordinates 
    screen.blit(text, [0,0]) 


image = imageUp

#While logic to keep game running 
while not done: 
    #capture input events so we can act upon them 
    for event in pygame.event.get(): 
        #if user select 'ESC' key or presses windows 'X' top right button
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                #change image up 
               # image = imageUp
                y_speed = -6

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -2

        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_UP: 
                #change image down 
                #image = imageDown
                y_speed = 6 

        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_RIGHT: 
                x_speed = 2 
     
    #Replace the whie sky with skyblue 
    screen.blit(background, (0,0)) 
    
    
    #fill screen with color defined above
    #screen.fill(white) 
    #Time to draw an obstacle 
    obstacle(xloc,yloc,xsize,ysize)
    #call function to draw the ball
    ball(x,y,image)
    #if the ball is between to obstacles
    Score(score)
    y+=y_speed 
    #time to redefine per refresh new x location 
    xloc -= obspeed
    #Adjust vertical y position 
    x+=x_speed

    if y > ground: 
        gameover()  
        image = imageDead
        y_speed = 0
        x_speed = 0
    if x > leftWall:
        x_speed = x_speed * -1 
    if x < rightWall:
        x_speed = x_speed * -1 


    #if we hit obstacles i the top block 
    if x+20 > xloc and y-20 < ysize and x-15 < xsize+xloc:
        gameover()
        image = imageDead
        obspeed = 0
        y_speed = 0

    #if we bit obstalces in the bottom block 
    if x+20 > xloc and y+20 > ysize+space and x-15 < xsize+xloc:
        gameover()
        image = imageDead
        obspeed = 0 
        y_speed = 0

    #if obstacle location x is 
    if xloc < -80:
        xloc = 700 
        ysize = random.randint(0,350)
        
    #Check if obstacle was passed adding to score 
    if x > xloc and x < xloc+3:
        score = (score + 1)  
     
    #refresh screen by flipping like a flipbook new animation 
    pygame.display.flip()
    #define times per second this will happen vai clock defined above 
    clock.tick(60) 


    #once logic loop and exit game 
pygame.quit() 




