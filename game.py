import pygame
import sys

pygame.init()

# Janela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu Primeiro Jogo")

# Clock (fora do loop)
clock = pygame.time.Clock()

# Jogador
x = 100
y = 100
velocidade = 5

# Inimigo
inimigo = pygame.Rect(300, 300, 50, 50)

rodando = True
while rodando:

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Teclado
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade

    # Criar retângulo do jogador
    jogador = pygame.Rect(x, y, 50, 50)

    # Colisão
    if jogador.colliderect(inimigo):
        print("Colidiu!")
        break

    # Desenho
    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, (0, 255, 0), jogador)
    pygame.draw.rect(tela, (255, 0, 0), inimigo)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
