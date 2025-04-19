import pygame
import random
pygame.init()
pygame.mixer.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255,0,0)
board = pygame.Rect((140 , 150 , 550, 300))
square1 = pygame.Rect((170, 180, 50, 50))
square2 = pygame.Rect((260, 180, 50, 50))
square3 = pygame.Rect((350, 180, 50, 50))
square4 = pygame.Rect((440, 180, 50, 50))
square5 = pygame.Rect((530, 180, 50, 50))
square = pygame.Rect((620,180,50,50))
square6 = pygame.Rect((170, 270, 50, 50))
square7 = pygame.Rect((260, 270, 50, 50))
square8 = pygame.Rect((350, 270, 50, 50))
square9 = pygame.Rect((440, 270, 50, 50))
square10 = pygame.Rect((530, 270, 50, 50))
square11 = pygame.Rect((620, 270, 50, 50))
square12 = pygame.Rect((170, 360, 50, 50))
square13 = pygame.Rect((260, 360, 50, 50))
square14 = pygame.Rect((350, 360, 50, 50))
square15 = pygame.Rect((440, 360, 50, 50))
square16 = pygame.Rect((530, 360, 50, 50))
square17 = pygame.Rect((620, 360, 50, 50))
sound1 = pygame.mixer.Sound(r"soundEffects/Voice1.mp3")
sound2 = pygame.mixer.Sound(r"soundEffects/Voice2.mp3")
sound3 = pygame.mixer.Sound(r"soundEffects/Voice3.mp3")
sound4 = pygame.mixer.Sound(r"soundEffects/Voice4.mp3")
sound5 = pygame.mixer.Sound(r"soundEffects/Voice5.mp3")
sound6 = pygame.mixer.Sound(r"soundEffects/voice6.mp3")
sound7 = pygame.mixer.Sound(r"soundEffects/voice7.mp3")
sound8 = pygame.mixer.Sound(r"soundEffects/voice8.mp3")
run = True

while run:
    pygame.draw.rect(screen, (128, 128, 128), board)
    pygame.draw.rect(screen,red,square1)
    pygame.draw.rect(screen, red, square2)
    pygame.draw.rect(screen, red, square3)
    pygame.draw.rect(screen, red, square4)
    pygame.draw.rect(screen, red, square5)
    pygame.draw.rect(screen, red, square6)
    pygame.draw.rect(screen, red, square7)
    pygame.draw.rect(screen, red, square8)
    pygame.draw.rect(screen, red, square)
    pygame.draw.rect(screen, red, square9)
    pygame.draw.rect(screen, red, square10)
    pygame.draw.rect(screen, red, square11)
    pygame.draw.rect(screen, red, square12)
    pygame.draw.rect(screen, red, square13)
    pygame.draw.rect(screen, red, square14)
    pygame.draw.rect(screen, red, square15)
    pygame.draw.rect(screen, red, square16)
    pygame.draw.rect(screen, red, square17)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if square1.collidepoint(mouse_x,mouse_y):
                pygame.mixer.stop()
                sound1.play()
            if square2.collidepoint(mouse_x,mouse_y):
                pygame.mixer.stop()
                sound2.play()
            if square3.collidepoint(mouse_x,mouse_y):
                pygame.mixer.stop()
                sound3.play()
            if square4.collidepoint(mouse_x,mouse_y):
                pygame.mixer.stop()
                sound4.play()
            if square5.collidepoint(mouse_x,mouse_y):
                pygame.mixer.stop()
                sound5.play()
            if square.collidepoint(mouse_x,mouse_y):
                pygame.mixer.stop()
                sound6.play()
            if square6.collidepoint(mouse_x,mouse_y):
                pygame.mixer.stop()
                sound7.play()
            if square7.collidepoint(mouse_x,mouse_y):
                pygame.mixer.stop()
                sound8.play()


    pygame.display.update()