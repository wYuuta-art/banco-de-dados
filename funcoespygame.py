#decora isso aqui

#1. init
#2. criar janela
#3. criar objetos
#4. loop:
    #- eventos
    #- lógica
    #- desenho
    #- atualizar tela
#5. quit



import pygame  # importa a biblioteca pygame
import sys     # usado para sair do programa corretamente

# ----------------------------
# INICIALIZAÇÃO
# ----------------------------
pygame.init()  # inicia todos os módulos do pygame

# ----------------------------
# CONFIGURAÇÕES DA JANELA
# ----------------------------
largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))  # cria janela
pygame.display.set_caption("Exemplo Completo Pygame")  # título da janela

# ----------------------------
# RELÓGIO (FPS)
# ----------------------------
clock = pygame.time.Clock()  # controla FPS

# ----------------------------
# CORES (RGB)
# ----------------------------
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)

# ----------------------------
# OBJETO (RETÂNGULO)a
# ----------------------------
x = 100
y = 100
velocidade = 5
largura_ret = 50
altura_ret = 50

# cria um retângulo (usado para colisão)
retangulo = pygame.Rect(x, y, largura_ret, altura_ret)

# ----------------------------
# FONTE (TEXTO)
# ----------------------------
fonte = pygame.font.SysFont("arial", 30)  # cria fonte do sistema
texto = fonte.render("Exemplo Pygame", True, PRETO)
# renderiza texto (True = suavização)

# ----------------------------
# SOM
# ----------------------------
pygame.mixer.init()  # inicia módulo de som
# (coloque um arquivo .wav na mesma pasta para testar)
# som = pygame.mixer.Sound("som.wav")

# ----------------------------
# LOOP PRINCIPAL
# ----------------------------
rodando = True
while rodando:

    clock.tick(60)  # limita o jogo a 60 FPS

    # ----------------------------
    # EVENTOS
    # ----------------------------
    for evento in pygame.event.get():  # captura eventos
        if evento.type == pygame.QUIT:  # botão fechar
            rodando = False

        if evento.type == pygame.KEYDOWN:  # tecla pressionada
            if evento.key == pygame.K_ESCAPE:
                rodando = False  # sai se apertar ESC

    # ----------------------------
    # TECLAS PRESSIONADAS CONTINUAMENTE
    # ----------------------------
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_w]:
        y -= velocidade
    if teclas[pygame.K_s]:
        y += velocidade
    if teclas[pygame.K_a]:
        x -= velocidade
    if teclas[pygame.K_d]:
        x += velocidade

    # atualiza posição do retângulo
    retangulo.topleft = (x, y)

    # ----------------------------
    # DESENHO NA TELA
    # ----------------------------
    tela.fill(BRANCO)  # pinta fundo

    pygame.draw.rect(tela, AZUL, retangulo)  # desenha retângulo
    pygame.draw.circle(tela, VERMELHO, (400, 300), 40)  # círculo
    pygame.draw.line(tela, VERDE, (0, 0), (800, 600), 3)  # linha

    tela.blit(texto, (250, 20))  # desenha texto na tela

    # ----------------------------
    # ATUALIZA A TELA
    # ----------------------------
    pygame.display.flip()  # atualiza tudo na tela

# ----------------------------
# FINALIZAÇÃO
# ----------------------------
pygame.quit()  # encerra pygame
sys.exit()     # fecha o programa completamente
