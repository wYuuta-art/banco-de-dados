import pygame

#inicializar
pygame.init()
tamanhotela=(800,800)
tela=pygame.display.set_mode(tamanhotela)
pygame.display.set_caption('Brick Breaker') # comando pro titulo

tamanho_bola=15
bola=pygame.Rect(100,500,tamanho_bola,tamanho_bola) #cria um retangulo e a medidas dentro sao left top width heigt
tamanho_jogador=100
jogador=pygame.Rect(0,750, tamanho_jogador, 15) #esquerda, o quao longe do topo, largura altura

qt_blocos_linha=8
qt_linha_bloco=5
qt_total=qt_blocos_linha * qt_linha_bloco

def criar_blocos(qtde_blocos_linha,qt_linha_bloco):
    altura_tela = tamanhotela[1]
    largura_tela = tamanhotela[0]

    largura_bloco = largura_tela/8 - 5
    altura_bloco = 15

    blocos = []
    #criar os blocos
    for coluna in range(qt_linha_bloco):
        for linha in range(qtde_blocos_linha):  #adicionar o bloco na lista de blocos

            bloco = pygame.Rect(linha * (largura_bloco+5), coluna*(altura_bloco+10 ), largura_bloco, altura_bloco)
            blocos.append(bloco)                            #distancia das linhas dos blocos

    return blocos


#criar as cores RGB
cores={
    'branca':(255,255,255),
    'verde':(0,255,0),
    'azul':(0,0,255),
    'preto':(0,0,0),
    'amarelo':(255,255,0),
}

fim_jogo=False
pontuacao_jogador=0
movimento_bola=[1,-1] #velocidade da bola inicialmente e precisa do -1 pq ela bate e volta
movimento_bola[0] #eixo x
movimento_bola[1] #eixo y


# criar as funcoes do jogo
def movimentar_jogador(evento):
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_LEFT:
            if jogador.x>=0:
                jogador.x=jogador.x-5  #ele vai para esquerda
        if evento.key == pygame.K_RIGHT:
            if jogador.x + tamanho_jogador < tamanhotela[0]:
                jogador.x=jogador.x + 5 #ele vai  aa direita pq soma
    pass
def movimentar_bola(evento): #e onde vai acontecer as acoes, e evento e tudo q o jogador faz
    global pontuacao_jogador  #
    movimento=movimento_bola
    bola.x=bola.x + movimento[0]
    bola.y=bola.y + movimento[1]

    if bola.x <= 0:
        movimento[0]=-movimento[0]
    if bola.y <= 0:
        movimento[1]=-movimento[1]
    if bola.x + tamanho_bola >= tamanhotela[0]:
        movimento[0]=-movimento[0]
    if bola.y + tamanho_bola >= tamanhotela[1]:
        movimento=None


    if jogador.collidepoint(bola.x, bola.y):
        movimento[1]=-movimento[1]

    for bloco in blocos:
        if bloco.collidepoint(bola.x, bola.y):
            blocos.remove(bloco)
            movimento[1]=-movimento[1]
            pontuacao_jogador += 1  # soma ponto aqui


    return movimento
    pass


#apenas acontece dois eventos/ffuncoes joogador bate na bola e aa bola destroi o bloco



# desemhar ass coisas na tela
def desenhar_inicio_jogo():
    tela.fill(cores['preto']) #fill faz aparecer na tela
    pygame.draw.rect(tela,cores['azul'], jogador)
    pygame.draw.rect(tela,cores['branca'], bola)

def desenhar_blocos(blocos):
    for bloco in blocos:

        pygame.draw.rect(tela, cores['verde'], bloco)



blocos=criar_blocos(qt_blocos_linha,qt_linha_bloco)

fonte = pygame.font.SysFont(None, 40)
# criar um loop infinito
clock = pygame.time.Clock()  #seu jogo fica atualizando a tela a cada millissegundo
while not fim_jogo:

    desenhar_inicio_jogo()
    desenhar_blocos(blocos) #tem q ficar desenhando no while para a imgaem aparecer/andar
    texto = fonte.render(f'Pontos: {pontuacao_jogador}', True, cores['amarelo'])
    tela.blit(texto, (10, 10))
    for evento in pygame.event.get(): #tudo que o jogador fizer sera adicionado no .get pq e considerado evento
        if evento.type == pygame.QUIT: #se lembra do type
            fim_jogo=True
    movimentar_jogador(evento)
    movimento_bola = movimentar_bola(bola)# a bola sempre vai se mexer
    clock.tick(200)
    pygame.display.flip() #atualiza a posicao

pygame.quit()


