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
pic1 = pygame.image.load("cannon-removebg-preview.png")
resized1 = pygame.transform.scale(pic1, (200, 150))
pic2 = pygame.image.load("rocketShip-removebg-preview.png")
resized2 = pygame.transform.scale(pic2, (100, 80))
resized3 = pygame.transform.scale(pic2, (50,50))
resized4 = pygame.transform.scale(pic2, (50,50))
resized5 = pygame.transform.scale(pic2, (50,50))

# Cannon position
cannonX = 270
spot = random.randint(50, 650) // CANNON_SPEED * CANNON_SPEED  # Ensure spot is a multiple of CANNON_SPEED

# Timer event
PAUSE_EVENT = pygame.USEREVENT + 1
paused = False  # To track if the cannon is paused

# Game loop
clock = pygame.time.Clock()
run = True

#colors
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
tokenY = random.randint(130,450)

balls = []
zoneX = 355
zoneY = 460
lives = 3
tick = 10

screen.blit(resized2, (zoneX,zoneY))
while (tokenX == zoneX) or (tokenY == zoneY):
    tokenX = random.randint(75, 720)
    tokenY = random.randint(130, 320)
token = pygame.draw.circle(screen, white, (tokenX,tokenY), 10, 5)


while run:
    screen.fill((0, 0, 0))
    screen.blit(resized1, (cannonX,5))
    if lives >= 1:
        screen.blit(resized3, (80,25))
    if lives >= 2:
        screen.blit(resized4, (115,25))
    if lives >= 3:
        screen.blit(resized5, (150, 25))
    pygame.draw.circle(screen, white, (tokenX,tokenY), 10, 5)
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

    image2_rect = resized2.get_rect(topleft=(zoneX,zoneY))
    screen.blit(resized2, image2_rect)
    token_rect = pygame.Rect(tokenX - 10, tokenY - 10, 20, 20)
    if image2_rect.colliderect(token_rect):
        num += 1
        tokenX = random.randint(75, 720)
        tokenY = random.randint(130, 320)
        while (tokenX == zoneX ) or (tokenY == zoneY):
            tokenX = random.randint(75, 720)
            tokenY = random.randint(130, 320)
        token = pygame.draw.circle(screen, white, (tokenX,tokenY), 10, 5)



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
        three = pygame.draw.rect(screen, (0, 0, 0), (100, 19, 15, 15))
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
    pygame.display.update()
    clock.tick(60)

pygame.quit()
