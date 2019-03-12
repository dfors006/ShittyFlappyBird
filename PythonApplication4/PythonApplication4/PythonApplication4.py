
#comment this shit 
import pygame
import random

pygame.init(); 

#colors 
black = (0, 0, 0) 
white = (123, 12, 123) 
green = (0, 255, 0) 
red = (255, 0, 0)

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

#we proceed to define our obstacle 
def obstacle(xloc, yloc,xsize,ysize): 
    pygame.draw.rect(screen,green, [xloc,yloc,xsize,ysize])
    pygame.draw.rect(screen,green, [xloc,int(yloc+ysize+space), xsize, ysize+500])

#define function to draw circle 
def ball(x,y):
    pygame.draw.circle(screen,black,(x,y),20)

def gameover(): 
    font = pygame.font.SysFont(None, 25) 
    text = font.render("game Over ", True, red) 
    screen.blit(text, [150,250])

#While logic to keep game running 
while not done: 
    #capture input events so we can act upon them 
    for event in pygame.event.get(): 
        #if user select 'ESC' key or presses windows 'X' top right button
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_speed = -10 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -5
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_UP: 
                y_speed = 10 
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_RIGHT: 
                x_speed = 5 
       

    #fill screen with color defined above
    screen.fill(white) 
    #Time to draw an obstacle 
    obstacle(xloc,yloc,xsize,ysize) 
    #call function to draw the ball
    ball(x,y)
    #time to redefine per refresh new x location 
    xloc -= obspeed
    #Adjust vertical y position 
    y+=y_speed 
    x+=x_speed

    if y > ground: 
        gameover()  
        y_speed = 0
        x_speed = 0
    if x > leftWall:
        x_speed = x_speed * -1 
    if x < rightWall:
        x_speed = x_speed * -1 
    

    #refresh screen by flipping like a flipbook new animation 
    pygame.display.flip()
    #define times per second this will happen vai clock defined above 
    clock.tick(60) 


    #once logic loop and exit game 
pygame.quit() 




