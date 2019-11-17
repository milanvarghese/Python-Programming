import pygame
import random
import math

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

#Enemy
enemyimage=[]
EnemyX=[]
EnemyY=[]
EnemyX_Change=[]
EnemyY_Change=[]
num_of_enemies=6


for i in range(num_of_enemies):
    enemyimage.append(pygame.image.load('icons/enemy.png'))
    EnemyX.append(random.randint(0,736))
    EnemyY.append(random.randint(50,150))
    EnemyX_Change.append(4)
    EnemyY_Change.append(40)

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

#Score
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)

TextX=10
TextY=10

def show_score(x,y):
    score=font.render("Score: "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def player(x,y):
    screen.blit(playerimage,(x,y))


def enemy(x,y,i):
    screen.blit(enemyimage[i],(x,y))

def fire_bullet(x,y):
    global Bullet_State
    Bullet_State="fire"
    screen.blit(bulletimage,(x+16,y+10))

def isCollision(EnemyX,EnemyY,BulletX,BulletY):
    distance=math.sqrt(math.pow(EnemyX-EnemyY,2) + math.pow(BulletX-BulletY,2))
    if distance<27:
        return True
    else:
        return False

#Game Loop / Making the Window stay and closing it when the close button is pressed
running=True
while running:
    #Changing the screen color. RGB
    screen.fill((0,0,0))
    
    #Adding Background Image
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        #Enabling Quit Button
        if event.type==pygame.QUIT:
            running=False

        #If keystroke is pressed check whether Its left or Right
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                PlayerX_Change=-5
            if event.key==pygame.K_RIGHT:
                PlayerX_Change=5
            if event.key==pygame.K_SPACE:
                if Bullet_State is "ready":
                    BulletX=PlayerX
                    fire_bullet(BulletX,BulletY)
                

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                PlayerX_Change=0
    
    #Calling Player and Checking its Boundary
    PlayerX+=PlayerX_Change
    if PlayerX<=0:
        PlayerX=0
    elif PlayerX>=736:
        PlayerX=736

    #Calling Enemy and Checking its Boundary
    for i in range(num_of_enemies):
        EnemyX[i]+=EnemyX_Change[i]

        if EnemyX[i]<=0:
           EnemyX_Change[i]=4
           EnemyY[i]+=EnemyY_Change[i]
        elif EnemyX[i]>=736:
           EnemyX_Change[i]=-4
           EnemyY[i]+=EnemyY_Change[i]
           
        #Collision
        collision=isCollision(EnemyX[i],EnemyY[i],BulletX,BulletY)
        if collision:
            BulletY=480
            Bullet_State="ready"
            score_value+=1
            EnemyX[i]=random.randint(0, 736)
            EnemyY[i]=random.randint(50, 150)

        enemy(EnemyX[i] ,EnemyY[i], i)

    #Bullet Movement
    if BulletY <= 0:
        BulletY=480
        Bullet_State="ready"

    if Bullet_State is "fire":
        fire_bullet(BulletX,BulletY)
        BulletY-=BulletY_Change
    
    player(PlayerX, PlayerY)
    show_score(TextX,TextY)
    pygame.display.update()
