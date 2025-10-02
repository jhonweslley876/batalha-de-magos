import pygame
import sys

pygame.init()

largura = 800
altura = 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Meu jogo')

verde = (34, 139, 34)
preto = (0, 0, 0)
branco = (255, 255, 255)

fonte = pygame.font.Font(None, 40)

while True:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print('Coordenadas: ', evento.pos)

    janela.fill(verde)
    texto = fonte.render('Criando uma janela de jogo', True, branco)
    janela.blit(texto, (200, 250))

    pygame.display.flip()