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

#initialize default value for stringMessage
stringMessage = "SSEC is awesome!"

#initialize default values for firstNumber and secondNumber
firstNumber = 1.0
secondNumber = 5.0

#initialize default mathMessage
mathMessage = str(firstNumber * secondNumber)

#clock loop -- keep running the game
while 1:
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



    '''
    Have fun playing around with this code!
    '''



    ##############################
    decider = input("Type S to change the String, type T to change the number, \
        type B to change both, or type Q to quit: ")
    if decider == "S":
        stringMessage = input("What string do you want to display? ")
    elif decider == "T":
        firstNumber = float(input("First number? "))
        secondNumber = float(input("Second number? "))
    elif decider == "B":
        stringMessage = input("What string do you want to display? ")
        firstNumber = float(input("First number? "))
        secondNumber = float(input("Second number? "))
    elif decider == "Q":
        sys.exit()
    else:
        print("\n" + "Oh no -- your input isn't quite right! Restart the program and try again :) ")
        break
    #####################################

    # Change this to try different math operations!
    mathMessage = str(round(firstNumber * secondNumber, 3))



    '''
    No need to change the code below here
    '''


    #handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
            sys.exit()
