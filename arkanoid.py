import time
import pygame
from pygame import mixer
from brick import Brick

#Instantiate mixer
mixer.init()

#Load audio file
mixer.music.load('wish.mp3')

#Set preferred volume
mixer.music.set_volume(10)

#Play the music
mixer.music.play()

pygame.init()
ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Arkanoid")

ball = pygame.image.load("ball.png")
ball_rect = ball.get_rect()
ball_speed = 4
ball_dir = [1, 1]
ball_rect.move_ip(0,0)

# Crea el objeto bate, y obtengo su rectángulo
bate = pygame.image.load("bate.png")
bate_rect = bate.get_rect()
bate_speed = 3
bate_prev_dir = -1

gameover = pygame.image.load("gameover.png")
gameover_rect = gameover.get_rect()
gameover_rect.move_ip(0,0)

# Pongo el bate en la parte inferior de la pantalla
bate_rect.move_ip(240,400)

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    # Compruebo si se ha pulsado alguna tecla y si se ha pulsado previamente, para acelerar la barra
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and bate_rect.left > 0:
        if bate_prev_dir == -1:
            if bate_speed < 8:
                bate_speed = bate_speed + 0.2
        else:
            bate_speed = 3
        bate_prev_dir = -1
        bate_rect = bate_rect.move(-bate_speed,0)
    if keys[pygame.K_RIGHT] and bate_rect.right < ventana.get_width():
        if bate_prev_dir == 1:
            if bate_speed < 8:
                bate_speed = bate_speed + 0.2
        else:
            bate_speed = 3
        bate_prev_dir = 1
        bate_rect = bate_rect.move(bate_speed, 0)

    # Compruebo si hay colisión
    if bate_rect.colliderect(ball_rect):
        ball_dir[1] = -ball_dir[1]
        # Aumento velocidad de la bola
        if ball_speed < 10:
            ball_speed = ball_speed + 0.5

    # Muevo la bola
    ball_rect = ball_rect.move([ball_dir[0]*ball_speed, ball_dir[1]*ball_speed])
    if ball_rect.left < 0 or ball_rect.right > ventana.get_width():
        ball_dir[0] = -ball_dir[0]
    if ball_rect.top < 0:
        ball_dir[1] = -ball_dir[1]

    # Relleno el fondo de la ventana
    ventana.fill((180, 180, 207))

    # Dibujo la bola
    ventana.blit(ball, ball_rect)

    # Dibujo el bate
    ventana.blit(bate, bate_rect)

    # Compruebo si toca el fondo
    if ball_rect.bottom > ventana.get_height():
        ventana.blit(gameover, gameover_rect)
        mixer.music.load('gameover.mp3')
        mixer.music.set_volume(10)
        mixer.music.play()
        jugando = False

    pygame.display.flip()
    pygame.time.Clock().tick(60)

time.sleep(3)
pygame.quit()