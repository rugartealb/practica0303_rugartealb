import time
import pygame
from pygame import mixer
from sprites import Ball, Bate, Brick, Rock


# Inicializo theme music
mixer.init()
theme_sound = mixer.music.load('wish.mp3')
theme_sound = mixer.music.set_volume(10)
theme_sound = mixer.music.play()

pygame.init()
ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Arkanoid")

# Crea el objeto ball, y obtengo su rectángulo
ball = Ball(8, "ball.png")

# Crea el objeto bate, y obtengo su rectángulo
bate = Bate(6, "bate.png")

# Creo los ladrillos y los posiciono en cuadrícula
lista_ladrillos = []
for posx in range(16):
    for posy in range(3):
        lista_ladrillos.append(Brick(40*posx, 45*posy, "brick.png"))

# Creo las rocas y las posiciono
lista_rocas = []
lista_rocas.append(Rock(0, 135, "rock.png"))
lista_rocas.append(Rock(40, 135, "rock.png"))
lista_rocas.append(Rock(560, 135, "rock.png"))
lista_rocas.append(Rock(600, 135, "rock.png"))

# Cargo imagen y sonido de gameover
gameover = pygame.image.load("gameover.png")
gameover_rect = gameover.get_rect()
gameover_rect.move_ip(0, 0)
gameover_sound = mixer.Sound('gameover.mp3')

# Cargo imagen y sonido de winner
winner = pygame.image.load("winner.png")
winner_rect = winner.get_rect()
winner_rect.move_ip(0, 0)
winner_sound = mixer.Sound('winner.mp3')

# Cargo sonido de rebote
rebote_sound = mixer.Sound("shot.mp3")

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    # Compruebo si se ha pulsado alguna tecla y si se ha pulsado previamente, acelero el bate
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and bate.rect.left > 0:
        if bate.prev_dir == -1:
            if bate.speed < 16:
                bate.speed = bate.speed + 0.4
        else:
            bate.speed = 6
        bate.prev_dir = -1
        bate.rect = bate.rect.move(-bate.speed, 0)
    if keys[pygame.K_RIGHT] and bate.rect.right < ventana.get_width():
        if bate.prev_dir == 1:
            if bate.speed < 16:
                bate.speed = bate.speed + 0.4
        else:
            bate.speed = 6
        bate.prev_dir = 1
        bate.rect = bate.rect.move(bate.speed, 0)

    # Compruebo si hay colisión
    if bate.rect.colliderect(ball.rect):
        #rebote_sound.play()
        ball.diry = -ball.diry
        # Aumento velocidad de la bola
        if ball.speed < 20:
            ball.speed = ball.speed + 1

    # Compruebo si hay colisión con ladrillos
    for ladrillo in lista_ladrillos:
        if ball.rect.colliderect(ladrillo.rect):
            ball.diry = -ball.diry
            lista_ladrillos.remove(ladrillo)

    # Compruebo si hay colisión con rocas
    for roca in lista_rocas:
        if ball.rect.colliderect(roca.rect):
            ball.diry = -ball.diry

    # Muevo la bola
    ball.rect = ball.rect.move([ball.dirx*ball.speed, ball.diry*ball.speed])
    if ball.rect.left < 0 or ball.rect.right > ventana.get_width():
        ball.dirx = -ball.dirx
    if ball.rect.top < 0:
        ball.diry = -ball.diry

    # Relleno el fondo de la ventana
    ventana.fill((180, 180, 207))

    # Dibujo la bola
    ventana.blit(ball.image, ball.rect)

    # Dibujo el bate
    ventana.blit(bate.image, bate.rect)

    # dibujo los ladrillos
    for ladrillo in lista_ladrillos:
        ventana.blit(ladrillo.image, ladrillo.rect)

    # dibujo las rocas
    for roca in lista_rocas:
        ventana.blit(roca.image, roca.rect)

    # Compruebo si quedan ladrillos
    if len(lista_ladrillos) == 0:
        ventana.blit(winner, winner_rect)
        theme_sound = mixer.music.stop()
        winner_sound.play()
        jugando = False

    # Compruebo si toca el fondo
    if ball.rect.bottom > ventana.get_height():
        ventana.blit(gameover, gameover_rect)
        theme_sound = mixer.music.stop()
        gameover_sound.play()
        jugando = False

    # Refresco de pantalla
    pygame.display.flip()
    # Set framerate
    pygame.time.Clock().tick(30)

time.sleep(3)
pygame.quit()