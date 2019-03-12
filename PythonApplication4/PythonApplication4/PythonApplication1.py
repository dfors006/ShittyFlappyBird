
#comment this shit 
import pygame

pygame.init(); 

#Loading Images

imageUp = pygame.image.load('Flappy_Background.png')
imageUp = pygame.transform.scale(imageUp, 40,40)

imageDown = pygame.image.load('Flappy_Up.png') 
imageDown = pygame.transform.scale(imageDown, (30,80))

#imageDead = pygame.image.load('deadBird.png') 
#imageDead = pygame.transform.scale(imageDead,(25,23))

 
#colors 
black = (0, 0, 0) 
white = (255, 255, 255) 
gren = (0,255,0)
red = (255,0,0)
skyBlue = (0,191,255)
orange = (255,215,0)
gray = (112, 138, 144)

#surface screen size 
size = (800, 700) 
screen = pygame.display.set_mode(size) 

#interface screen title 
pygame.display.set_caption('Flippy bird') 

#boolean T/F to control game logic 
done = False
#clock to control game refresh speed 
clock = pygame.time.Clock() 

#While logic to keep game running 
while not done: 
    #capture input events so we can act upon them 
    for event in pygame.event.get(): 
        #if user select 'ESC' key or presses windows 'X' top right button
        if event.type == pygame.QUIT:
            done = True
    #fill screen with color defined above
    screen.fill(white) 
    #refresh screen by flipping like a flipbook new animation 
    pygame.display.flip()
    #define times per second this will happen vai clock defined above 
    clock.tick(60) 






    #once logic loop and exit game 
pygame.quit() 




