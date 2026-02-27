import pygame
import sys

pygame.init()

# Tela
largura = 800
altura = 500
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Mini Mario Completo")

clock = pygame.time.Clock()

# Mundo maior que a tela
largura_mundo = 2000

# Jogador
player = pygame.Rect(100, 300, 40, 60)
vel_y = 0
gravidade = 1
velocidade = 6
pulando = False

# Plataformas
plataformas = [
    pygame.Rect(0, 450, 2000, 50),        # chão
    pygame.Rect(300, 350, 200, 20),
    pygame.Rect(700, 300, 200, 20),
    pygame.Rect(1100, 380, 200, 20),
]

# Inimigo
inimigo = pygame.Rect(600, 410, 40, 40)
vel_inimigo = 3
direcao_inimigo = 1

# Câmera
camera_x = 0

rodando = True
while rodando:

    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()

    dx = 0
    dy = 0

    # Movimento lateral
    if teclas[pygame.K_LEFT]:
        dx = -velocidade
    if teclas[pygame.K_RIGHT]:
        dx = velocidade

    # Pulo
    if teclas[pygame.K_SPACE] and not pulando:
        vel_y = -20
        pulando = True

    # Gravidade
    vel_y += gravidade
    dy += vel_y

    # ===== COLISÃO EIXO X =====
    player.x += dx
    for plat in plataformas:
        if player.colliderect(plat):
            if dx > 0:
                player.right = plat.left
            if dx < 0:
                player.left = plat.right

    # ===== COLISÃO EIXO Y =====
    player.y += dy
    for plat in plataformas:
        if player.colliderect(plat):
            if vel_y > 0:  # caindo
                player.bottom = plat.top
                vel_y = 0
                pulando = False
            if vel_y < 0:  # batendo cabeça
                player.top = plat.bottom
                vel_y = 0

    # ===== Movimento inimigo =====
    inimigo.x += vel_inimigo * direcao_inimigo

    if inimigo.left < 500 or inimigo.right > 900:
        direcao_inimigo *= -1

    # ===== Colisão jogador x inimigo =====
    if player.colliderect(inimigo):
        # Se caiu em cima do inimigo
        if vel_y > 0 and player.bottom - vel_y <= inimigo.top:
            inimigo.x = -100  # remove inimigo
            vel_y = -15
        else:
            print("Morreu!")
            player.x = 100
            player.y = 300

    # ===== Câmera =====
    camera_x = player.centerx - largura // 2

    if camera_x < 0:
        camera_x = 0
    if camera_x > largura_mundo - largura:
        camera_x = largura_mundo - largura

    # ===== Desenho =====
    tela.fill((135, 206, 235))  # céu

    for plat in plataformas:
        pygame.draw.rect(tela, (139, 69, 19),
                         (plat.x - camera_x, plat.y, plat.width, plat.height))

    pygame.draw.rect(tela, (255, 0, 0),
                     (player.x - camera_x, player.y, player.width, player.height))

    pygame.draw.rect(tela, (0, 0, 0),
                     (inimigo.x - camera_x, inimigo.y, inimigo.width, inimigo.height))

    pygame.display.flip()

pygame.quit()
sys.exit()
