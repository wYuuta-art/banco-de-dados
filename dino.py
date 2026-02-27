import pygame
import sys

pygame.init()

# Tela
largura = 800
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Mini Dino")

clock = pygame.time.Clock()

# Jogador
x = 100
y = 300
largura_player = 40
altura_player = 50

vel_y = 0
gravidade = 1
pulando = False

# Obstáculo
obs_x = 800
obs_y = 310
obs_largura = 30
obs_altura = 40
vel_obs = 6

rodando = True
while rodando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()

    # Pulo
    if teclas[pygame.K_SPACE] and not pulando:
        vel_y = -15
        pulando = True

    # Gravidade
    vel_y += gravidade
    y += vel_y

    # Chão
    if y >= 300:
        y = 300
        pulando = False

    # Movimento obstáculo
    obs_x -= vel_obs

    # Reset obstáculo
    if obs_x < -50:
        obs_x = 800

    # Rects
    jogador = pygame.Rect(x, y, largura_player, altura_player)
    obstaculo = pygame.Rect(obs_x, obs_y, obs_largura, obs_altura)

    # Colisão
    if jogador.colliderect(obstaculo):
        print("Game Over")

    # Desenho
    tela.fill((255,255,255))
    pygame.draw.rect(tela, (0,0,0), jogador)
    pygame.draw.rect(tela, (0,0,0), obstaculo)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
