import random
import math
import pygame
from pygame import mixer
from django.utils.termcolors import background

pygame.init()
mixer.music.load(r"sounds/Cyberpunk.mp3")
mixer.music.play(-1)
bullet_Sound = pygame.mixer.Sound("sounds/Cartoon_Laser_Gunshot_Sound_Effect_#shorts.mp3")
collideSound = pygame.mixer.Sound("sounds/Arcade_Explosion_Sound_Effect.mp3")
#Used to create the screen that we will put the game on
screen = pygame.display.set_mode((800,600))


#Use to create a title for the game
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("images/spaceship.png")

#background
background = pygame.image.load("images/background1.png")
original_back = background.get_size();
new_back = (original_back[0] + 170, original_back[1] + 125)
newBackImg = pygame.transform.scale(background,new_back)
#Sets the icon of the pygame application in the dashboard
pygame.display.set_icon(icon)

#This initializes the player
playerImg = pygame.image.load('images/spaceship2.png')
original_size = playerImg.get_size();
new_size = (original_size[0]//7, original_size[1]//7)
newPlayerImg = pygame.transform.scale(playerImg,new_size)
playerX = 370
playerY = 480
playerX_change = 0

# for the enemy
newEnemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg = pygame.image.load('images/ufo.png')
    original_height = enemyImg.get_size();
    new_height = (original_size[0]//7, original_size[1]//7)
    newEnemyImg.append(pygame.transform.scale(enemyImg,new_height))
    enemyX.append(random.randint(0,748))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

#Bullet state
bulletImg = pygame.image.load('images/bullet.png')
original_bullet = bulletImg.get_size()
new_bullet = (original_bullet[0]//2, original_bullet[1]//2)
newBulletImg = pygame.transform.scale(bulletImg,new_bullet)
bulletX = 370
bulletY = 480
bulletX_change = 4
bulletY_change = 10
bullet_state = "ready"
#Score
score = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

#Game Over Text
over_font = pygame.font.Font('freesansbold.ttf',64)
textX = 10
textY = 10

def showScore(x,y):
    score_value = font.render("Score: " + str(score), True, (255,255,255))
    screen.blit(score_value, (x,y))
def game_over_text():
    game_over = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(game_over, (200,250))
def player(x,y):
    screen.blit(newPlayerImg,(x,y))
def enemy(x,y,i):
    screen.blit(newEnemyImg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(newBulletImg,(x + 20,y + 10))
def isCollide(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

#Used to keep the game looping until running is made false
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(newBackImg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #We will track when the usser presses the arrow keys in order to move th space ship accordingly
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_Sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                playerX_change = 0

    #Checking for boundaries of spaceship
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 730:
        playerX = 730

    #Movement of the enemy
    for i in range(num_of_enemies):

        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 730:
            enemyY[i] += enemyY_change[i]
            enemyX_change[i] = -4
        # Collision
        collision = isCollide(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bullet_Sound.stop()
            collideSound.play()
            bulletY = 480
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    player(playerX,playerY)
    showScore(textX, textY)
    pygame.display.update()