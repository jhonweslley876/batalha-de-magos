import sys
import time
import os

def escrever_texto_na_caixa(texto, largura=50, velocidade=0.03):
    linhas = []

    # Quebra o texto em várias linhas com base na largura
    while texto:
        linha = texto[:largura]
        if len(texto) > largura and ' ' in linha:
            # Evita cortar palavras no meio
            ultimo_espaco = linha.rfind(' ')
            linha = linha[:ultimo_espaco]
        linhas.append(linha)
        texto = texto[len(linha):].lstrip()

    # Desenhar a caixa de texto
    print("┌" + "─" * (largura + 2) + "┐")
    for _ in range(len(linhas)):
        print("│" + " " * (largura + 2) + "│")
    print("└" + "─" * (largura + 2) + "┘")

    # Subir o cursor para escrever dentro da caixa (em sistemas compatíveis com ANSI)
    for i, linha in enumerate(linhas):
        sys.stdout.write(f"\033[{len(linhas)-i+1}A")  # Move o cursor para cima
        sys.stdout.write("\r│ ")  # Início da linha dentro da caixa
        for letra in linha:
            sys.stdout.write(letra)
            sys.stdout.flush()
            time.sleep(velocidade)
        sys.stdout.write(" " * (largura - len(linha)) + " │\n")  # Preenche o resto da linha
    # Move o cursor para baixo até fora da caixa
    print("\033[" + str(len(linhas)) + "B", end="")

# Exemplo de uso:
import time
mensagem = "você deixa-o viver, da as costas a ele e segue o seu caminho"
escrever_texto_na_caixa(mensagem, largura=60, velocidade=0.03)
time.sleep(3)
mensagem2 = 'você foi apunhalado pelas costas '
escrever_texto_na_caixa(mensagem2, largura=50, velocidade=0.06)

import random

c = random.randint(1, 100)
print(f'Mago: {c} ATK')