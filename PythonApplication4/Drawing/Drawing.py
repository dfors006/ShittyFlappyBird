
import pygame
from math import pi 

#initialize the game aengine 
pygame.init() 

#define the colors we wil use in the format 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255) 
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0 ,0) 

#Set the height and widthh of the screen 
size = [400,300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")

#Loop until the suser clicks the close button 
done = False

clock.tick(10) 
while not done: 
    for event in pygame.event():
        if event.type == pygame.QUIT:
            done = True 

    screen.fill(WHITE) 

pygame.quit() 

    
        