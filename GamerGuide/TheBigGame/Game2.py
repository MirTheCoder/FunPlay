import pygame
import random

def Game2():
    pygame.init()
    pygame.mixer.init()
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = pygame.Rect((0, 250, 25, 100))
    player2 = pygame.Rect((775, 250, 25, 100))
    line = pygame.Rect((387.5,0, 25, 600))
    pygame.mixer.music.load("../sounds/Unleashed.mp3")
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(loops=-1, start=0.0)
    font = pygame.font.Font(None, 64)
    pen = pygame.font.Font(None, 50)

    # Ball settings


    # Player setup


    # Colors
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    black = (0, 0, 0)

    run = True
    clock = pygame.time.Clock()

    ballX = random.choice((400,450))
    ballY = random.choice((300,350))
    speed = 3
    tap = 0

    ballXchange = speed * random.choice((1, -1))
    ballYChange = speed * random.choice((1,-1))
    num1 = 0
    num2 = 0

    def reset1():
        global ballX,ballY,speed,tap,ballXchange,ballYChange,num1,num2
        ballX = random.choice((400, 450))
        ballY = random.choice((300, 350))
        speed = 3
        tap = 0

        ballXchange = speed * random.choice((1, -1))
        ballYChange = speed * random.choice((1, -1))
        num1 = 0
        num2 = 0
    while run:
        pygame.display.set_caption('Ping Pong')
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen,white,player1)
        pygame.draw.rect(screen,white,player2)
        pygame.draw.rect(screen,white,line)
        ball = pygame.draw.circle(screen, white, [ballX,ballY], 10, 0)

        text = font.render(str(num1), True, white)
        textRect = text.get_rect()
        textRect.center = (200, 100)
        screen.blit(text, textRect)

        text = font.render(str(num2), True, white)
        textRect = text.get_rect()
        textRect.center = (600, 100)
        screen.blit(text, textRect)

        ballX += ballXchange
        ballY += ballYChange

        if player1.colliderect(pygame.Rect(ballX - 10, ballY - 10, 10 * 2, 10 * 2)):
            ballXchange *= -1
            tap += 1

        if player2.colliderect(pygame.Rect(ballX - 10, ballY - 10, 10 * 2, 10 * 2)):
            ballXchange *= -1
            tap += 1
              # New coin Y
        if tap == 5:
            ballXchange *= 1.05
            ballYChange *= 1.05
            tap = 0
        if ball.x <= 0:
            num2 +=1
            ballX = random.choice((400, 450))
            ballY = random.choice((300, 350))
        if ball.x >= SCREEN_WIDTH:
            num1 +=1
            ballX = random.choice((400, 450))
            ballY = random.choice((300, 350))

        if ballY - 10 <= 0 or ballY + 10 >= SCREEN_HEIGHT:
            ballYChange *= -1

        key = pygame.key.get_pressed()
        if key[pygame.K_s] and player1.bottom < SCREEN_HEIGHT:
            player1.move_ip(0, 5)
        if key[pygame.K_w] and player1.top > 0:
            player1.move_ip(0, -5)
        if key[pygame.K_DOWN] and player2.bottom < SCREEN_HEIGHT:
            player2.move_ip(0, 5)
        if key[pygame.K_UP] and player2.top > 0:
            player2.move_ip(0, -5)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if num1 == 7:
            text = font.render('Player 1 wins', True, blue)
            textRect = text.get_rect()
            textRect.center = (400, 270)
            screen.blit(text, textRect)
            pygame.display.update()

            text = pen.render('Press y to play again or n to quit', True, blue)
            textRect = text.get_rect()
            textRect.center = (400, 330)
            screen.blit(text, textRect)
            pygame.display.update()

            waiting_for_input = True
            while waiting_for_input:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        waiting_for_input = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            reset1()
                            waiting_for_input = False
                        elif event.key == pygame.K_n:
                            run = False
                            waiting_for_input = False
        if num2 == 7:
            text = font.render('Player 2 wins', True, blue)
            textRect = text.get_rect()
            textRect.center = (400, 270)
            screen.blit(text, textRect)
            pygame.display.update()

            text = font.render('Player 1 wins', True, blue)
            textRect = text.get_rect()
            textRect.center = (400, 270)
            screen.blit(text, textRect)
            pygame.display.update()

            text = pen.render('Press y to play again or n to quit', True, blue)
            textRect = text.get_rect()
            textRect.center = (400, 330)
            screen.blit(text, textRect)
            pygame.display.update()

            waiting_for_input = True
            while waiting_for_input:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        waiting_for_input = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            reset1()
                            waiting_for_input = False
                        elif event.key == pygame.K_n:
                            run = False
                            waiting_for_input = False



        pygame.display.update()
        clock.tick(60)