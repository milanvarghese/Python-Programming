import pygame
import random
import math
from pygame import mixer
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

#Background Sound
mixer.music.load('background.wav')
mixer.music.play(-1)

#Player
playerimage=pygame.image.load('icons/space-invaders.png')
PlayerX=370
PlayerY=480
PlayerX_Change=0

#Enemy
enemyimage=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6


for i in range(num_of_enemies):
    enemyimage.append(pygame.image.load('icons/enemy.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

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

#Game Over Text
over_font=pygame.font.Font('freesansbold.ttf',64)

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


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

def isCollision(enemyX,enemyY,BulletX,BulletY):
    distance=math.sqrt(math.pow(enemyX-enemyY,2) + math.pow(BulletX-BulletY,2))
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
                    bullet_sound=mixer.Sound('laser.wav')
                    bullet_sound.play()
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

        #Enemy
        if enemyY[i]>440:
            for j in range(num_of_enemies):
                enemyY[j]=2000
            game_over_text()
            break

        enemyX[i]+=enemyX_change[i]

        if enemyX[i]<=0:
           enemyX_change[i]=4
           enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=736:
           enemyX_change[i]=-4
           enemyY[i]+=enemyY_change[i]
           
        #Collision
        collision=isCollision(enemyX[i],enemyY[i],BulletX,BulletY)
        if collision:
            explosion_sound=mixer.Sound('explosion.wav')
            explosion_sound.play()
            BulletY=480
            Bullet_State="ready"
            score_value+=1
            enemyX[i]=random.randint(0, 736)
            enemyY[i]=random.randint(50, 150)

        enemy(enemyX[i] ,enemyY[i], i)

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