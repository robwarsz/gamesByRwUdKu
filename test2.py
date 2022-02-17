import pygame

pygame.init()

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

def player(x,y):
    screen.blit(playerImg,(x,y))

running = True
while running:
    screen.fill((60,100,60))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = -0.1
                #print(playerX,playerY)
            if event.key == pygame.K_RIGHT:
                speed = 0.1
                #print(playerX,playerY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speed = 0

    playerX+=speed

    if playerX <= 0:
       playerX=0
    if playerX >= 736:
       playerX=736

    player(playerX,playerY)
    pygame.display.update()