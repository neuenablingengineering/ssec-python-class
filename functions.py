import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')


pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (189, 252, 201)
RED = (255, 106, 106)
BLUE = (202, 225, 255)
GREY1 = (129, 129, 129)
GREY2 = (105, 105, 105)
GREY3 = (66, 66, 66)
PINK = (255, 181, 197)
PURPLE = (171, 130, 255)
colors = [GREY1, GREY2, GREY3]

# play around with the width and height of the screen!
width = 500
height = 300

######################################################################

#initialize screen and caption/mouse
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Cool Text!')
pygame.mouse.set_visible(0)

#make a background to work with
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(BLUE)

# update screen
screen.blit(background, (0, 0))
pygame.display.flip()

#initialize the game clock
clock = pygame.time.Clock()







'''
CHALLENGES:
    - Write a function that makes mathMessage = 17.5 with inputs 1.0 and 2.0
    - Write a function that makes mathmessage = 1000 with inputs -10.0 and 17.0
    - Write a function that changes the stringMessage!
    - Make more challenges and share them with us!
'''

#here's a simple example of a function that adds two given numbers
def add(number1, number2):
    return number1 + number2



#initialize default value for stringMessage
stringMessage = "I'm pretty cool"

#initialize default mathMessage -- play around with these inputs!
mathMessage = str(add(1.0, 2.0))








'''
No need to change the code below here (but you can if you want to play around with colors!)
Can you figure out how?
'''

#clock loop -- keep running the game
while 1:
    #keep cursor visible
    pygame.mouse.set_visible(True)
    #clock tick
    clock.tick(30)

    # declare and print text to the screen
    if pygame.font:
        font = pygame.font.Font(None, 48)
        textString = font.render(stringMessage, 1, PURPLE)
        textMath = font.render(mathMessage, 1, RED)
        textposString = textString.get_rect(center=(background.get_width()/2, background.get_height()/4))
        textposMath = textMath.get_rect(center=(background.get_width()/2, background.get_height()/2))
        background.fill(BLUE)
        background.blit(textString, textposString)
        background.blit(textMath, textposMath)

    # update screen
    screen.blit(background, (0, 0))
    pygame.display.flip()


    #handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
