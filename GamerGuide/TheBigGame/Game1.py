import pygame
import random

pygame.init()
pygame.mixer.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = pygame.Rect((200, 125, 25, 25))
pygame.mixer.music.load("Unleashed.mp3")
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play(loops=-1, start=0.0)
# Ball settings
ball_X = random.choice((100, 700))
ball_Y = random.choice((100, 500))
sound = pygame.mixer.Sound("uh_oh.mp3")
sound.set_volume(0.25)
sound2 = pygame.mixer.Sound("sounds/Voice3.mp3")
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

# Colors
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)

run = True
font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()

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
                        reset()
                        waiting_for_input = False
                    elif event.key == pygame.K_n:
                        run = False
                        waiting_for_input = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
