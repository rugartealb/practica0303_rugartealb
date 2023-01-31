import time
import pygame
from pygame import mixer
from brick import Brick, Rock


# Inicializo theme music
mixer.init()
theme_sound = mixer.music.load('wish.mp3')
theme_sound = mixer.music.set_volume(10)
theme_sound = mixer.music.play()

pygame.init()
ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Arkanoid")

# Crea el objeto ball, y obtengo su rectángulo
ball = pygame.image.load("ball.png")
ball_rect = ball.get_rect()
ball_speed = 4
ball_dir = [1, -1]
ball_rect.move_ip(240,350)

# Crea el objeto bate, y obtengo su rectángulo
bate = pygame.image.load("bate.png")
bate_rect = bate.get_rect()
bate_speed = 3
bate_prev_dir = -1
bate_rect.move_ip(240,420)

# Creo los ladrillos y los posiciono en cuadrícula
lista_ladrillos = []
for posx in range(16):
    for posy in range(4):
        lista_ladrillos.append(Brick(40*posx, 45*posy, "brick.png"))

# Creo las rocas y las posiciono
lista_rocas = []
lista_rocas.append(Rock(0, 180, "rock.png"))
lista_rocas.append(Rock(40, 180, "rock.png"))
lista_rocas.append(Rock(560, 180, "rock.png"))
lista_rocas.append(Rock(600, 180, "rock.png"))

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

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    # Compruebo si se ha pulsado alguna tecla y si se ha pulsado previamente, acelero el bate
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

    # Compruebo si hay colisión con ladrillos
    for ladrillo in lista_ladrillos:
        if ball_rect.colliderect(ladrillo.rect):
            ball_dir[1] = -ball_dir[1]
            lista_ladrillos.remove(ladrillo)

    # Compruebo si hay colisión con rocas
    for roca in lista_rocas:
        if ball_rect.colliderect(roca.rect):
            ball_dir[1] = -ball_dir[1]

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

    # dibujo los ladrillos
    for ladrillo in lista_ladrillos:
        ventana.blit(ladrillo.image, ladrillo.rect)

    # dibujo las rocas
    for roca in lista_rocas:
        ventana.blit(roca.image, roca.rect)

    # Compruebo si quedan ladrillos
    if len(lista_ladrillos) == 0:
        ventana.blit(winner, winner_rect)
        winner_sound.play()
        jugando = False

    # Compruebo si toca el fondo
    if ball_rect.bottom > ventana.get_height():
        ventana.blit(gameover, gameover_rect)
        gameover_sound.play()
        jugando = False

    # Refresco de pantalla
    pygame.display.flip()
    # Set framerate
    pygame.time.Clock().tick(60)

time.sleep(3)
pygame.quit()