import pygame
import random
pygame.init()
pygame.mixer.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
ball_X = random.choice((100, 700))
ball_Y = random.choice((100, 500))
ball_XChange = 3 * random.choice((1, -1))
ball_YChange = 3
clock = pygame.time.Clock()
run = True
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255,0,0)

def Game1():
    global screen, SCREEN_WIDTH, SCREEN_HEIGHT,ball_X,ball_Y, ball_XChange, ball_YChange,run, white, green, blue,black, red


    player = pygame.Rect((200, 125, 25, 25))
    pygame.mixer.music.load(r"/Code Play/GamerGuide/sounds/Unleashed.mp3")
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(loops=-1, start=0.0)
    # Ball settings
    sound = pygame.mixer.Sound(r"/Code Play/GamerGuide/sounds/uh_oh.mp3")
    sound.set_volume(0.25)
    sound2 = pygame.mixer.Sound(r"/Code Play/GamerGuide/sounds/Voice3.mp3")
    sound2.set_volume(0.25)


    # Player setup
    while ball_X == player.x and ball_Y == player.y:
        ball_X = random.choice((100, 700))
        ball_Y = random.choice((100, 500))
    ball_XChange = 3 * random.choice((1, -1))
    ball_YChange = 3
    coinX = random.choice((46, 770))
    coinY = random.choice((60, 570))
    lives = 3
    num = 0
    count = 5


    run = True
    font = pygame.font.Font(None, 32)

    class Ball:
        def __init__(self, size, color, xBall, yBall, radius, ballXChange, ballYChange):
            self.size = size
            self.color = color
            self.xBall = xBall
            self.yBall = yBall
            self.ballXChange = ballXChange
            self.ballYChange = ballYChange
            self.radius = radius

        def update(self):
            """Update ball position and handle boundary collisions."""
            self.xBall += self.ballXChange
            self.yBall += self.ballYChange

            if self.xBall - self.radius <= 0 or self.xBall + self.radius >= SCREEN_WIDTH:
                self.ballXChange *= -1
            if self.yBall - self.radius <= 0 or self.yBall + self.radius >= SCREEN_HEIGHT:
                self.ballYChange *= -1

        def draw(self):
            """Draw the ball."""
            pygame.draw.circle(self.size, self.color, (self.xBall, self.yBall), self.radius)

        def get_rect(self):
            """Get the ball's rectangle for collision detection."""
            return pygame.Rect(self.xBall - self.radius, self.yBall - self.radius, self.radius * 2, self.radius * 2)

    first = Ball(screen, blue, ball_X, ball_Y, 25, ball_XChange, ball_YChange)
    balls = [first]

    def reset():
        global ball_X, ball_Y, player, ball_XChange, ball_YChange, coinX, coinY, lives, num, run, font, balls, first,count
        ball_X = random.choice((100, 700))
        ball_Y = random.choice((100, 500))
        while ball_X == player.x and ball_Y == player.y:
            ball_X = random.choice((100, 700))
            ball_Y = random.choice((100, 500))
        ball_XChange = 2 * random.choice((1, -1))
        ball_YChange = 2
        coinX = random.choice((46, 770))
        coinY = random.choice((60, 570))
        lives = 3
        num = 0
        count = 5

        # Ensure the coin doesn't spawn on the player
        while coinX == player.x and coinY == player.y:
            coinX = random.choice((46, 770))
            coinY = random.choice((60, 570))

        font = pygame.font.Font(None, 32)
        balls.clear()  # Clear existing balls
        first = Ball(screen, blue, ball_X, ball_Y, 25, ball_XChange, ball_YChange)
        balls.append(first)

    # Main game loop
    while run:
        pygame.display.set_caption('Collector')
        screen.fill((0, 0, 0))

        # Draw objects
        pygame.draw.rect(screen, (255, 0, 0), player)
        if lives == 3:
            one = pygame.draw.rect(screen, (255, 0, 0), (160, 19, 15, 15))
        if lives >= 2:
            two = pygame.draw.rect(screen, (255, 0, 0), (130, 19, 15, 15))
        if lives >= 1:
            three = pygame.draw.rect(screen, (255, 0, 0), (100, 19, 15, 15))
        pygame.draw.circle(screen, white, [coinX, coinY], 10, 0)
        for pic in balls:
            pic.draw()

        # Ball boundary check and movement
        for pic in balls:
            pic.update()

        # Player movement with keys
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and player.left > 0:
            player.move_ip(-7, 0)
        if key[pygame.K_d] and player.right < SCREEN_WIDTH:
            player.move_ip(7, 0)
        if key[pygame.K_s] and player.bottom < SCREEN_HEIGHT:
            player.move_ip(0, 7)
        if key[pygame.K_w] and player.top > 0:
            player.move_ip(0, -7)

        # Event handling
        if num == count:
            newBall = Ball(screen, blue, ball_X, ball_Y, 25, ball_XChange, ball_YChange)
            balls.append(newBall)
            count += 5

        for pic in balls:
            pic.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Display health
        text = font.render('Health: ', True, white)
        textRect = text.get_rect()
        textRect.center = (50, 25)
        screen.blit(text, textRect)

        # Display Score
        text = font.render(str(num), True, white)
        textRect = text.get_rect()
        textRect.center = (775, 25)
        screen.blit(text, textRect)
        # Coin collision detection
        if player.colliderect(pygame.Rect(coinX - 10, coinY - 10, 20, 20)):  # Check collision with coin
            num += 1  # Increase score
            coinX = random.choice((46, 770))  # New coin X
            coinY = random.choice((60, 570))  # New coin Y
            while (player.x - 10 <= coinX <= player.x + 35)  and (player.y - 10 <= coinY <= player.y + 35):
                coinX = random.choice((46, 770))
                coinY = random.choice((60, 570))

        # Ball collision detection
        for pic in balls:
            if player.colliderect(pic.get_rect()):
                sound.stop()
                sound.play()
                lives -= 1
                ball_X = random.choice((100, 600))
                ball_Y = random.choice((100, 400))
                while ball_X == player.x and ball_Y == player.y:
                    ball_X = random.choice((100, 600))
                    ball_Y = random.choice((100, 400))
                pic.xBall = ball_X
                pic.yBall = ball_Y

        if lives == 0:
            sound.stop()
            sound2.play()
            three = pygame.draw.rect(screen, (0, 0, 0), (100, 19, 15, 15))
            font = pygame.font.Font(None, 64)
            pen = pygame.font.Font(None, 40)
            text = font.render('GAME OVER', True, white)
            textRect = text.get_rect()
            textRect.center = (400, 200)
            screen.blit(text, textRect)

            text = pen.render('Click "y" to restart or "n" to quit', True, white)
            textRect = text.get_rect()
            textRect.center = (400, 270)
            screen.blit(text, textRect)
            pygame.display.update()

            # Wait for the player to either restart or quit
            waiting_for_input = True
            while waiting_for_input:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        waiting_for_input = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            sound.stop()
                            sound2.stop()
                            Game1()
                            waiting_for_input = False
                        elif event.key == pygame.K_n:
                            run = False
                            waiting_for_input = False
                            main()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def Game2():
    global screen, SCREEN_WIDTH, SCREEN_HEIGHT, ball_X, ball_Y, ball_XChange, ball_YChange, run, white, green, blue, black, red
    player1 = pygame.Rect((0, 250, 25, 100))
    player2 = pygame.Rect((775, 250, 25, 100))
    line = pygame.Rect((387.5,0, 25, 600))
    pygame.mixer.music.load(r"/Code Play/GamerGuide/sounds/Unleashed.mp3")
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
            ballXchange *= 1.15
            ballYChange *= 1.15
            tap = 0
        if ball.x <= 0:
            ballXchange = speed * random.choice((1, -1))
            ballYChange = speed * random.choice((1, -1))
            num2 +=1
            ballX = random.choice((400, 450))
            ballY = random.choice((300, 350))
        if ball.x >= SCREEN_WIDTH:
            ballXchange = speed * random.choice((1, -1))
            ballYChange = speed * random.choice((1, -1))
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
                            Game2()
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
                            Game2()
                            waiting_for_input = False
                        elif event.key == pygame.K_n:
                            run = False
                            waiting_for_input = False
                            main()



        pygame.display.update()
        clock.tick(60)

import pygame
import random

pygame.init()
pygame.mixer.init()

def Game3():
    global screen, SCREEN_WIDTH, SCREEN_HEIGHT, ball_X, ball_Y, ball_XChange, ball_YChange, run, white, green, blue, black, red
    import pygame
    import random

    pygame.init()
    pygame.mixer.init()

    # Constants
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    CANNON_SPEED = 10  # Speed should evenly divide the range to prevent overshooting
    PAUSE_TIME = 1000  # Pause time in milliseconds
    Ychange = 5
    # Initialize Pygame window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Load and scale image
    pic1 = pygame.image.load(
        r"/Code Play/GamerGuide/images/cannon-removebg-preview.png")
    resized1 = pygame.transform.scale(pic1, (200, 150))
    pic2 = pygame.image.load(
        r"/Code Play/GamerGuide/images/rocketShip-removebg-preview.png")
    resized2 = pygame.transform.scale(pic2, (100, 80))
    resized3 = pygame.transform.scale(pic2, (50, 50))
    resized4 = pygame.transform.scale(pic2, (50, 50))
    resized5 = pygame.transform.scale(pic2, (50, 50))

    # Cannon position
    cannonX = 270
    spot = random.randint(50, 650) // CANNON_SPEED * CANNON_SPEED  # Ensure spot is a multiple of CANNON_SPEED

    # Timer event
    PAUSE_EVENT = pygame.USEREVENT + 1
    paused = False  # To track if the cannon is paused

    # Game loop
    clock = pygame.time.Clock()
    run = True

    # colors
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    black = (0, 0, 0)
    num = 0
    font = pygame.font.Font(None, 32)
    text = font.render('Health: ', True, white)
    textRect = text.get_rect()
    textRect.center = (50, 51)

    word = font.render(str(num), True, white)
    wordRect = word.get_rect()
    wordRect.center = (775, 25)

    class Ball:
        def __init__(self, color, Ball_X, Ball_Y, radius, ballYChange):
            self.color = color
            self.xBall = Ball_X
            self.yBall = Ball_Y
            self.ballYChange = ballYChange
            self.radius = radius

        def update(self):
            """Update ball position and handle boundary collisions."""
            self.yBall += self.ballYChange

        def draw(self, screen):
            """Draw the ball."""
            pygame.draw.circle(screen, self.color, (self.xBall, self.yBall), self.radius)

        def get_rect(self):
            """Get the ball's rectangle for collision detection."""
            return pygame.Rect(self.xBall - self.radius, self.yBall - self.radius, self.radius * 2, self.radius * 2)

    tokenX = random.randint(75, 720)
    tokenY = random.randint(130, 450)

    balls = []
    zoneX = 355
    zoneY = 460
    lives = 3
    tick = 10

    screen.blit(resized2, (zoneX, zoneY))
    while (tokenX == zoneX) or (tokenY == zoneY):
        tokenX = random.randint(75, 720)
        tokenY = random.randint(130, 320)
    token = pygame.draw.circle(screen, white, (tokenX, tokenY), 10, 5)

    while run:
        screen.fill((0, 0, 0))
        screen.blit(resized1, (cannonX, 5))
        if lives >= 1:
            screen.blit(resized3, (80, 25))
        if lives >= 2:
            screen.blit(resized4, (115, 25))
        if lives >= 3:
            screen.blit(resized5, (150, 25))
        pygame.draw.circle(screen, white, (tokenX, tokenY), 10, 5)
        tokenY += 3

        token = pygame.draw.circle(screen, white, (tokenX, tokenY), 10)
        word = font.render(str(num), True, white)
        wordRect = word.get_rect()
        wordRect.center = (775, 25)
        screen.blit(text, textRect)
        screen.blit(word, wordRect)
        if len(balls) != 0:
            for x in balls:
                x.draw(screen)
                x.update()
        if token.y >= SCREEN_HEIGHT:
            tokenX = random.randint(75, 720)
            tokenY = random.randint(130, 320)
            while (tokenX == zoneX) or (tokenY == zoneY):
                tokenX = random.randint(75, 720)
                tokenY = random.randint(130, 320)
            token = pygame.draw.circle(screen, white, (tokenX, tokenY), 10, 5)

        if not paused:
            # Move cannon towards the target spot
            if cannonX < spot:
                cannonX += min(CANNON_SPEED, spot - cannonX)  # Prevent overshooting
            elif cannonX > spot:
                cannonX -= min(CANNON_SPEED, cannonX - spot)  # Prevent overshooting

            # If cannon reaches the spot, start a pause timer
            if cannonX == spot:
                paused = True
                pygame.time.set_timer(PAUSE_EVENT, PAUSE_TIME, loops=1)

        image2_rect = resized2.get_rect(topleft=(zoneX, zoneY))
        screen.blit(resized2, image2_rect)
        token_rect = pygame.Rect(tokenX - 10, tokenY - 10, 20, 20)
        if image2_rect.colliderect(token_rect):
            num += 1
            tokenX = random.randint(75, 720)
            tokenY = random.randint(130, 320)
            while (tokenX == zoneX) or (tokenY == zoneY):
                tokenX = random.randint(75, 720)
                tokenY = random.randint(130, 320)
            token = pygame.draw.circle(screen, white, (tokenX, tokenY), 10, 5)

        for box in balls:
            if image2_rect.colliderect(box.get_rect()):
                balls.remove(box)
                zoneX = 355
                zoneY = 460
                lives -= 1
                Ychange = 5
                CANNON_SPEED = 10

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and ((zoneX + 5) > 0):
            zoneX -= 10
        if key[pygame.K_RIGHT] and ((zoneX - 10) < SCREEN_WIDTH):
            zoneX += 10

        if num == tick:
            Ychange += 3
            tick += 10
            CANNON_SPEED += 10

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == PAUSE_EVENT:
                # Resume movement and select a new random spot different from the current position
                paused = False
                while True:
                    new_spot = random.randint(50, 650) // CANNON_SPEED * CANNON_SPEED  # Keep spot aligned to speed
                    if new_spot != cannonX:  # Ensure the spot is not the same
                        spot = new_spot
                        new_ball = Ball(green, cannonX + 100, 150, 10, Ychange)
                        balls.append(new_ball)
                        break  # Exit loop once a valid spot is found
        if lives < 1:
            font = pygame.font.Font(None, 64)
            pen = pygame.font.Font(None, 40)
            text1 = font.render('GAME OVER', True, white)
            text1Rect = text1.get_rect()
            text1Rect.center = (400, 200)
            screen.blit(text1, text1Rect)

            text2 = pen.render('Click "y" to restart or "n" to quit', True, white)
            text2Rect = text.get_rect()
            text2Rect.center = (220, 270)
            screen.blit(text2, text2Rect)
            pygame.display.update()

            # Wait for the player to either restart or quit
            waiting_for_input = True
            while waiting_for_input:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        waiting_for_input = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            waiting_for_input = False
                            run = False
                        elif event.key == pygame.K_n:
                            run = False
                            waiting_for_input = False
                            main()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()


def main():
    global screen, SCREEN_WIDTH, SCREEN_HEIGHT, ball_X, ball_Y, ball_XChange, ball_YChange, run, blue, white, black
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((0, 0, 0))

    font = pygame.font.Font(None, 32)
    mun = pygame.font.Font(None, 64)

    # Load and resize images
    image1 = pygame.image.load(r"/Code Play/GamerGuide/images/Game1_Image.png")
    resized1 = pygame.transform.scale(image1, (200, 150))

    image2 = pygame.image.load(r"/Code Play/GamerGuide/images/Game2_Image.png")
    resized2 = pygame.transform.scale(image2, (200, 150))

    image3 = pygame.image.load(r"/Code Play/GamerGuide/images/Game2_Image.png")
    resized3 = pygame.transform.scale(image3, (200,150))

    image4 = pygame.image.load(r"/Code Play/GamerGuide/images/Game_3_Image.png")
    resized4 = pygame.transform.scale(image4, (189,130))

    text = mun.render('RETRO WORLD', True, white)
    textRect = text.get_rect()
    textRect.center = (400, 100)
    screen.blit(text, textRect)

    # Display images
    image1_rect = resized1.get_rect(topleft=(30, 325))  # Set the top-left corner position
    image2_rect = resized2.get_rect(topleft=(290, 325))  # Same for the second image
    image3_rect = resized3.get_rect(topleft=(550,325))
    image4_rect = resized4.get_rect(topleft=(556,337))
    screen.blit(resized1, image1_rect)
    screen.blit(resized2, image2_rect)
    screen.blit(resized3, image3_rect)
    screen.blit(resized4, image4_rect)

    text = font.render('Game 1', True, white)
    textRect = text.get_rect()
    textRect.center = (125, 500)
    screen.blit(text, textRect)

    text = font.render('Game 2', True, white)
    textRect = text.get_rect()
    textRect.center = (390, 500)
    screen.blit(text, textRect)

    text = font.render('Game 3', True, white)
    textRect = text.get_rect()
    textRect.center = (655, 500)
    screen.blit(text, textRect)

    out = font.render('Exit', True, red)
    outRect = out.get_rect()
    outRect.center = (390, 570)
    screen.blit(out, outRect)


    text = font.render('Select a game to play or press exit to leave', True, white)
    textRect = text.get_rect()
    textRect.center = (400, 275)
    screen.blit(text, textRect)

    pygame.display.update()  # Make sure the screen is updated at this point

    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                wait = False

            if event.type == pygame.MOUSEBUTTONDOWN:  # Left mouse button
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if image1_rect.collidepoint(mouse_x, mouse_y):
                        print("Clicked inside resized1")
                        wait = False
                        Game1()  # Replace with actual Game1 function
                    elif image2_rect.collidepoint(mouse_x, mouse_y):
                        print("Clicked inside resized2")
                        wait = False
                        Game2()  # Replace with actual Game2 function
                    elif image3_rect.collidepoint(mouse_x,mouse_y):
                        print("Clicked inside resized3")
                        wait = False
                        Game3()
                    elif outRect.collidepoint(mouse_x,mouse_y):
                        wait = False

        pygame.display.update()


main()
