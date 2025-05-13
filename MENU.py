





#sudo dpkg - configure -a
#sudo apt-get install python3-pygame

import math
import random
import pygame

from pygame import mixer

# inicio del juego
pygame.int()

#se crea el fondo de pantalla
screen = pygame.display.set_mode ((1000,800))

#fondo de pantalla
background = pygame.image.load('/home/pc19/Documentos/Juego/istockphoto-1354982067-612x612.jpg')

#sonido de fondo
mixer.music.load('/home/pc19/Documentos/Juego/WhatsApp Audio 2025-04-29 at 3.51.02 PM.aac')
mixer.music.play(-1)

#titulo y icono
pygame.display.set_caption("Perdidos en")
icon = pygame.image.load('/home/pc19/Documentos/Juego/1200px-2001_A_Space_Odyssey_movie_black_logo-removebg-preview.png')
pygame.display.set_icon(icon)

#jugador
playerimg=pygame.image.load('/home/pc19/Documentos/Juego/cohete.png')
playerX= 370
playerY= 480
playerX_change=0

#enemigos
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=5

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('/home/pc19/Documentos/Juego/bomba nuclear.png'))
    enemyX.append(random.randit(0,736))
    enemyX.append(random.randit(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

#disparo, proyector, bala
armaImg= pygame.image.load('/home/pc19/Documentos/Juego/images-removebg-preview(1).png')
armaX=0
armaY=480
armaX_change=0
armaY_change=10
arma_estado="ready"

#puntaje


score_value=0
font =pygame.font.Font('freesansbold.ttf',32)


textY=10
textX=10

#juego terminado
over_font =pygame.font.Font('freesansbold.ttf',64)

def show_puntaje(x,y):
    score=font.render("Score: "+str(score_value),True,(255,255,255))
    screen.blit(score(x,y))
def gameover_text():
    over_text= over_font.render("Game Over",True,255,255,255)
    screen.blit(over_text,(200,250))
def player(x, y):
     screen.blit(PlayerImg, (x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y))
def Iniciar_disparo(x,y):
    global bulletstate
    arma_estado = "Fire"
    screen.blit(armaImg,(x+16,y+10))
def iscollision(enemyX,enemyY,armaX,armaY):
    distance = math.sgrt(math.pow(enemyX-armaX)+(math.pow(enemyY-armaY,2)))
if distance<27:
    return True
else : return False

#ciclo de juego
running = True
while running:
    screen.fill((0,0))
    #imagen de fondo
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False


            #si presiona derecha o izquierda
            if event.type==pygame.KEYDOWN
              if playerX_change==pygame.K_LEFT
                 playerX_change=.5
            if event.key==pygame.K_RIGHT
                 playerX_change= 5

 