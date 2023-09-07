import os
import random
import pygame
from pygame.locals import *
from words import random_words
from functions import *

# select random word from list
word = random.choice(random_words)
# print(word)

if __name__ == "__main__":

    pygame.init()
    pygame.font.init()

    # COLORS
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # FONT
    font = pygame.font.SysFont(None, 70)
    
    # PATH
    path = os.getcwd()

    # IMAGES
    IMAGE_1 = os.path.join(path, "images/1.png")
    IMAGE_2 = os.path.join(path, "images/2.png")
    IMAGE_3 = os.path.join(path, "images/3.png")
    IMAGE_4 = os.path.join(path, "images/4.png")
    IMAGE_5 = os.path.join(path, "images/5.png")
    IMAGE_6 = os.path.join(path, "images/6.png")
    IMAGE_7 = os.path.join(path, "images/7.png")

    HEART_PATH = os.path.join(path, "images/heart.png")
    HEART_IMAGE = pygame.image.load(HEART_PATH)
    HEART_IMAGE = pygame.transform.scale(HEART_IMAGE, (50, 50))
    
    BROKEN_HEART_PATH = os.path.join(path, "images/heart broken.png")
    BROKEN_HEART_IMAGE = pygame.image.load(BROKEN_HEART_PATH)
    BROKEN_HEART_IMAGE = pygame.transform.scale(BROKEN_HEART_IMAGE, (50, 50))

    # SCREEN
    WINDOWHEIGHT = 650
    WINDOWWIDTH = 650
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('HANGMAN GAME')
    FPS = 60
    mainClock = pygame.time.Clock()

    windowSurface.fill(WHITE)

    draw_text("HANGMAN GAME", font, windowSurface, WINDOWWIDTH / 2 - 200, WINDOWHEIGHT / 2 - 100, BLACK)

    draw_text("press a key to continue", font, windowSurface, WINDOWWIDTH / 2 - 250, WINDOWHEIGHT / 2 + 50, BLACK)


    pygame.display.update()

    waiting = True    
    
    while waiting:
        
        for event in pygame.event.get():

            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                waiting = False

    while True:

        # chose random word
        random_word = random.choice(random_words)
        print(random_word)
        # random_word = "apple"
        secreat_word = "".join(["_" for letter in random_word])
        # convert secreat_word into list and then add spaces
        # secreat_word = " ".join(list(secreat_word))

        print(secreat_word)

        lifes = 6
        HEARTS = [HEART_IMAGE] * lifes
        print(random_word)


        while True:
            windowSurface.fill(WHITE)

            windowSurface.blit(pygame.image.load(IMAGE_1), (0, 0))

            if lifes == 5:
                windowSurface.blit(pygame.image.load(IMAGE_2), (0, 0))
            elif lifes == 4:
                windowSurface.blit(pygame.image.load(IMAGE_3), (0, 0))
            elif lifes == 3:
                windowSurface.blit(pygame.image.load(IMAGE_4), (0, 0))
            elif lifes == 2:
                windowSurface.blit(pygame.image.load(IMAGE_5), (0, 0))
            elif lifes == 1:
                windowSurface.blit(pygame.image.load(IMAGE_6), (0, 0))
            elif lifes == 0:
                windowSurface.blit(pygame.image.load(IMAGE_7), (0, 0))
            elif lifes == -1:
                break

            if secreat_word == random_word:
                break


            for i, heart in enumerate(HEARTS):
                windowSurface.blit(heart, (i * 55 + 10, 15))


            for event in pygame.event.get():

                if event.type == QUIT:
                    terminate()
                
                if event.type == KEYDOWN:
                    if event.key in range(pygame.K_a, pygame.K_z + 1):
                        # Get the key name
                        key_name = pygame.key.name(event.key)
           
                        if key_name in random_word:
                            for i, letter in enumerate(random_word):
                                if letter == key_name:
                                    secreat_word = secreat_word[:i] + letter + secreat_word[i + 1:]
                        else:
                            lifes -= 1
                            HEARTS[lifes] = BROKEN_HEART_IMAGE
            


            draw_text(secreat_word, font, windowSurface, WINDOWWIDTH / 2 - 100 , WINDOWHEIGHT / 2 + 250, BLACK)

            pygame.display.update()

            mainClock.tick(FPS)

        
        windowSurface.fill(WHITE)        
        
        if lifes == -1:
            draw_text("YOU LOSE", font, windowSurface, WINDOWWIDTH / 2 - 200, WINDOWHEIGHT / 2 - 100, BLACK)
        else:
            draw_text("YOU WIN", font, windowSurface, WINDOWWIDTH / 2 - 200, WINDOWHEIGHT / 2 - 100, BLACK)


        draw_text("press a key to continue", font, windowSurface, WINDOWWIDTH / 2 - 250, WINDOWHEIGHT / 2 + 50, BLACK)
        
        pygame.display.update()
        
        waiting = True    
        
        while waiting:
            
            for event in pygame.event.get():

                if event.type == QUIT:
                    terminate()

                if event.type == KEYDOWN:
                    waiting = False

