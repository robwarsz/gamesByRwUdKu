import pygame

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

#shoot
shootImg = pygame.image.load("assets/shoot.png")
shootX=400
shootY=400
shootSpeed=10
shootState = "ready"

def player(x,y):
    screen.blit(playerImg,(x,y))

def shootFromShip(x,y):
    global shootState
    shootState = "throw"
    screen.blit(shootImg,(x,y-40))

running = True
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
                print("SPACE")
                bulletY=playerY
                shootFromShip(playerX,bulletY)

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

    player(playerX,playerY)
    if shootState is "throw":
        shootFromShip(playerX,bulletY)
        bulletY-=shootSpeed

    pygame.display.flip()
    clock.tick(60)