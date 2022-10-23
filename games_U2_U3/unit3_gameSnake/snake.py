""" 
Adigma team
Brianna Ayelen Balam Velasco
Jesús Javier Can Noh
Damaris Yuselin Dzul Uc
Fátima Miranda Pestaña
"""

import pygame 
import time
import random
from pygame import mixer


#initializing pygame
pygame.init()
mixer.init()

#Defining colors
backgroundColor = (48, 191, 58)
snakeColor = (246, 249, 35 )
foodColor = (243, 87, 62 ) 
gameOverColor = (230, 41, 11 ) 
green = (72, 175, 23)
yellow = (240, 233, 17)
names = (108, 108, 83)

#loading the images
food = pygame.image.load('apple.png') 
background = pygame.image.load('background.jpg')

width, height = 600, 400 #Creating the game window

gameDisplay = pygame.display.set_mode((width, height)) #setting the screen
pygame.display.set_caption('Snake Game') #setting the caption

clock = pygame.time.Clock() #setting the clock

snakeSize = 10 #size of the snake
snakeSpeed = 13 #speed of the snake

messageFont = pygame.font.SysFont('windows', 30) #font for the message
scoreFont = pygame.font.SysFont('ubuntu', 25) #font for the score

#function to print the score
def print_score(score): 
    text = scoreFont.render('Score: '+str(score), True, foodColor) #text to be printed
    gameDisplay.blit(text, [0,0]) 
    
#function to draw the snake    
def draw_snake(snakeSize, snakePixels): 
    for XnY in snakePixels:
        pygame.draw.rect(gameDisplay, snakeColor, [XnY[0], XnY[1], snakeSize, snakeSize]) #drawing the snake
        
#function to draw the text        
def draw_text(text, font, surface, x, y, main_color, background_color=None): 
    textobj = font.render(text, True, main_color, background_color)
    textrect = textobj.get_rect()
    textrect.centerx = x
    textrect.centery = y
    surface.blit(textobj, textrect)
        
#function to display the start screen (menú)     
def start_screen():    
    while True:
        gameDisplay.blit(background, (0,0))
        title_font = pygame.font.Font('Snake_Chan.ttf', 100)
        big_font = pygame.font.Font(None, 36)
        draw_text('Snake', title_font, gameDisplay,
                  600/2, 400/4, yellow)
        draw_text('Use your keyboard rows to play', big_font, gameDisplay,
                  600 / 2, 400 / 2.2, green)
       # draw_text('Press any mouse button or S when you\'re ready',
        #          messageFont, gameDisplay, 600 / 2, 400 / 1.7, backgroundColor, black)
        draw_text('Brianna Ayelen Balam Velasco', messageFont, gameDisplay,
                  600 / 2, 400 / 1.5, names)
        draw_text('Jesús Javier Can Noh', messageFont, gameDisplay,
                  600 / 2, 400 / 1.34, names)
        draw_text('Damaris Yuselin Dzul Uc', messageFont, gameDisplay,
                  600 / 2, 400 / 1.2, names)
        draw_text('Fátima Miranda Pestaña', messageFont, gameDisplay,
                  600 / 2, 400 / 1.1, names)

        draw_text('Press C or touch the screen to start', messageFont, gameDisplay,
                  600 / 2, 400 / 1.7, green)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                return
        
 
            
#function to run the game
def run_game():
    
    mixer.music.load('snakeMusic.wav') #loading the music
    mixer.music.play(-1) #playing the music
    
    start_screen() #calling the start screen function
    
    gameOver = False 
    gameClose = False
    
    x = width/2
    y = height/2
    
    x_speed = 0 #speed in the x axis
    y_speed = 0 #speed in the y axis
    
    snakePixels = [] #snake pixels
    snakeLength = 1 #snake length
    
    #random position of the food
    food_x = round(random.randrange(0, width-snakeSize)/10.0)*10.0
    food_y = round(random.randrange(0, height-snakeSize)/10.0)*10.0 
    
    #game loop
    while not gameOver: 
        
        while gameClose: #game over screen
            gameDisplay.blit(background, (0,0))
            gameOverMessage = messageFont.render('Game Over! Press C to play again or Q to quit', True, gameOverColor)

            gameDisplay.blit(gameOverMessage, [width/7, height/3])
            print_score(snakeLength-1)
            
            pygame.display.update() #updating the display
            
            #getting the events
            for event in pygame.event.get(): 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_c:
                        run_game()
                if event.type == pygame.QUIT:
                    gameOver = True
                    gameClose = False
                    
        #controls
        for event in pygame.event.get(): 
            if event.type == pygame .QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snakeSize
                    y_speed = 0
                elif event.key == pygame.K_RIGHT:
                    x_speed = snakeSize
                    y_speed = 0
                elif event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snakeSize
                elif event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snakeSize
        
        #game over if snake hits the wall
        if x >= width or x < 0 or y >= height or y < 0: 
            gameClose = True
            if gameClose == True:
                uh = mixer.Sound('uh.wav') #loading the sound
                uh.play() #playing the sound
            
        x += x_speed #updating the x position
        y += y_speed #updating the y position
        
        
        gameDisplay.blit(background, (0,0)) #filling the screen with the background color
        gameDisplay.blit(food, (food_x, food_y))
        #pygame.draw.rect(gameDisplay, foodColor, [food_x, food_y, snakeSize, snakeSize]) #drawing the food
        
        snakePixels.append([x,y]) #adding the snake pixels
        
        if len(snakePixels) > snakeLength: #removing the snake pixels
            del snakePixels[0]
            
        
        draw_snake(snakeSize, snakePixels) #drawing the snake
        print_score(snakeLength-1)
        
        pygame.display.update() #updating the screen
        
         #if snake eats the food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width-snakeSize)/10.0)*10.0 #random position of the food
            food_y = round(random.randrange(0, height-snakeSize)/10.0)*10.0 #random position of the food
            snakeLength += 1 #increasing the snake length 
            eat = mixer.Sound('eat.wav') #loading the sound
            eat.play() #playing the sound
        
        clock.tick(snakeSpeed) #setting the speed of the snake
        
    pygame.quit() #quitting pygame
    quit() #quitting python
    
    
run_game() #calling the run game function