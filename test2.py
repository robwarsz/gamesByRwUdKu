import random

import pygame
import math

pygame.init()
clock = pygame.time.Clock()
print(clock)

screen = pygame.display.set_mode((800,600))

# nazwa gry
pygame.display.set_caption('Bum bum bach bach!')

#icon
icon = pygame.image.load("assets/space.png")
pygame.display.set_icon(icon)

#gracz
playerImg = pygame.image.load("assets/space.png")
playerX = 368
playerY = 480
speed = 0

#enemy
enemyImg = pygame.image.load("assets/spaceship.png")
enemyX = random.randint(0,730)
enemyY = 0
enemySpeedX = 2
enemySpeedY = 0

#shoot
shootImg = pygame.image.load("assets/shoot.png")
bulletX=0
bulletY=0
shootSpeed=5
shootState = "ready"

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg, (x, y))

def shootFromShip(x,y):
    global shootState
    shootState = "throw"
    screen.blit(shootImg,(x,y-40))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + math.pow(enemyY-bulletY,2))


running = True

#przebieg gry
while running:
    screen.fill((60,100,60))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         speed = -0.1
        #         #print(playerX,playerY)
        #     if event.key == pygame.K_RIGHT:
        #         speed = 0.1
        #         #print(playerX,playerY)

        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #         speed = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if shootState is 'ready':
                    print("SPACE")
                    bulletX = playerX
                    bulletY = playerY
                    shootFromShip(bulletX,bulletY)

        keys = pygame.key.get_pressed()

        speed=0
        if keys[pygame.K_LEFT]:
            speed = -1
        elif keys[pygame.K_RIGHT]:
            speed = 1



    playerX+=speed

    if playerX <= 0:
       playerX=0
    if playerX >= 736:
       playerX=736

    if enemyX<=0 or enemyX>736:
        enemySpeedX*=-1
        enemySpeedY += 32

    enemyX += enemySpeedX
    enemyY = enemySpeedY
    print(enemySpeedY)

    player(playerX,playerY)
    enemy(enemyX,enemyY)

    if bulletY<=-40:
        bulletY=-50
        shootState = 'ready'


    if shootState is "throw":
        shootFromShip(bulletX,bulletY)
        bulletY-=shootSpeed

    pygame.display.flip()
    clock.tick(60)