import pygame
import random

#Initialize
pygame.init()

#Creating the Screen
screen=pygame.display.set_mode((800,600))


#Changing the Title and Icon
pygame.display.set_caption("Space Invaders")

#Changing the Icon
icon=pygame.image.load('icons/ufo.png')
pygame.display.set_icon(icon)

#Background Image
background=pygame.image.load('icons/background.png')

#Player
playerimage=pygame.image.load('icons/space-invaders.png')
PlayerX=370
PlayerY=480
PlayerX_Change=0

#Player_Bullets
bulletimage=pygame.image.load('icons/bullet.png')
BulletX=0
BulletY=480
BulletX_Change=0
BulletY_Change=10
Bullet_State="ready"
'''Ready - Can't See the bullet on Screen
Fire- Bullet is moving
'''

#Enemy
enemyimage=pygame.image.load('icons/enemy.png')
EnemyX=random.randint(0,800)
EnemyY=random.randint(0,150)
EnemyX_Change=4
EnemyY_Change=40

def player(x,y):
    screen.blit(playerimage,(x,y))

def enemy(x,y):
    screen.blit(enemyimage,(x,y))

def fire_bullet(x,y):
    global Bullet_State
    Bullet_State="fire"
    screen.blit(bulletimage,(x+16,y+10))

#Game Loop / Making the Window stay and closing it when the close button is pressed
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        #If keystroke is pressed check whether Its left or Right
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                PlayerX_Change+=5
            if event.key==pygame.K_RIGHT:
                PlayerX_Change-=5
            if event.key==pygame.K_SPACE:
                if Bullet_State is "ready":
                    BulletX=PlayerX
                    fire_bullet(BulletX,BulletY)
                

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                PlayerX_Change=0
    #Changing the screen color. RGB
    screen.fill((0,0,0))
    
    #Adding Background Image
    screen.blit(background,(0,0))
    #Calling Player and Checking its Boundary
    PlayerX-=PlayerX_Change
    if PlayerX<0:
        PlayerX=0
    if PlayerX>736:
        PlayerX=736
    player(PlayerX,PlayerY)

    #Calling Enemy and Checking its Boundary
    EnemyX+=EnemyX_Change
    if EnemyX<0:
       EnemyX_Change =4
       EnemyY+=EnemyY_Change
    if EnemyX>736:
       EnemyX_Change=-4
       EnemyY+=EnemyY_Change
    
    #Bullet State
    if BulletY <= 0:
        BulletY=480
        Bullet_State="ready"

    if Bullet_State is "fire":
        fire_bullet(BulletX,BulletY)
        BulletY-=BulletY_Change
    
    enemy(EnemyX,EnemyY)
    pygame.display.update()
