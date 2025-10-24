import os
import random
import time
import sys
import keyboard

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

def dialogo(): # dialogo inicial
    mensagem = "Olá, pequeno viajante!"
    escrever_texto_na_caixa(mensagem, largura=40, velocidade=0.03)

    keyboard.wait('enter')
    input('')
    os.system('cls')

    mensagem = "Um mago muito poderoso está na cidade!"
    escrever_texto_na_caixa(mensagem, largura=50, velocidade=0.03)

    keyboard.wait('enter')
    input('')
    os.system('cls')

    mensagem = "Ele parece desafiar alguém para uma partida de black jack."
    escrever_texto_na_caixa(mensagem, largura=60, velocidade=0.03)

    keyboard.wait('enter')
    input('')
    os.system('cls')

def escrever_texto(texto, velocidade=0.06): # escreve texto como em jogos (letras aparecendo aos poucos lentamente)
    for letra in texto:
        sys.stdout.write(letra)   # escreve sem pular linha
        sys.stdout.flush()        # força a impressão imediata
        time.sleep(velocidade)    # controla a velocidade
    print()  # quebra de linha no final

def carregamento(): # barra de carregamento
    total = 30
    for i in range(1, 101):
        bloco = int(i * total / 100)
        barra = '◼' * bloco + '-' * (total-bloco)
        print(f'\r[{barra}] {i}%', end='', flush=True)
        time.sleep(0.01)

def regras():
    tabela = '├──────────────────────────────────────────────────────────────────────────┤'
    print('┌──────────────────────────────┬────────────┬──────────────────────────────┐')
    print('│                              │ COMO JOGAR │                              │')
    print('├──────────────────────────────┴────────────┴──────────────────────────────┤')
    print('│                Compre cartas para ter mais chances de ganhar.            │')
    print(tabela)
    print('│                  lembre-se: se passar de 21, você perde!                 │')
    print(tabela)
    print('│  Ao lado das opções terá um número. Escreva eles para escolher a opção.  │')
    print(tabela)
    print('│                Você gasta 10 de mana para comprar cartas.                │')
    print(tabela)
    print('│      Não se preocupe, você recupera 5 de mana ao final de cada turno.    │')
    print(tabela)
    print('│  Se estourar o valor (passar de 21) ou perder por menor número, um valor │')
    print('│  de 1 a 20 será escolhido para o dano final.                             │')
    print(tabela)
    print('│     Um valor total de 21 nas cartas resultará em um bônus de +10 ATK     │')
    print(tabela)
    print('│     A carta "A" Vale por 1, já as cartas "K", "Q" e "J" valem por 10     │')
    print('└──────────────────────────────────────────────────────────────────────────┘')
    
    escrever_texto('Pressione "enter" para passar.')
    keyboard.wait('enter')
    input('') # espaço vazio para ajustar o wait('enter')
    os.system('cls')

def magos(vida1, vida2, mana, mana_bot): # estatísticas do jogador e mago

    quadro = '├────────────┼────────────┤'
    
    if vida1 == 100 and vida2 == 100:
        print('┌────────────┬────────────┐')
        print( '│    VOCÊ    │    MAGO    │')
        print(quadro)
        print(f'│   {vida1} HP   │   {vida2} HP   │')

    elif vida1 < 10 and vida2 < 10:
        print('┌────────────┬────────────┐')
        print( '│    VOCÊ    │    MAGO    │')
        print(quadro)
        print(f'│    {vida1} HP    │    {vida2} HP    │')
    
    elif vida1 < 10 or vida2 < 10:
        print('┌────────────┬────────────┐')
        print( '│    VOCÊ    │    MAGO    │')
        print(quadro)
        print(f'│    {vida1} HP    │   {vida2} HP    │')
    
    elif vida1 < 100 and vida2 < 100:
        print('┌────────────┬────────────┐')
        print( '│    VOCÊ    │    MAGO    │')
        print(quadro)
        print(f'│    {vida1} HP   │   {vida2} HP    │')

    elif vida1 < 100:
        print('┌────────────┬────────────┐')
        print( '│    VOCÊ    │    MAGO    │')
        print(quadro)
        print(f'│   {vida1} HP    │   {vida2} HP   │')
    elif vida2 < 100:
        print('┌────────────┬────────────┐')
        print( '│    VOCÊ    │    MAGO    │')
        print(quadro)
        print(f'│   {vida1} HP   │   {vida2} HP    │')

    
    if mana == 100 and mana_bot == 100:
        print(quadro)
        print(f'│  {mana} Mana  │  {mana_bot} Mana  │')
        print('└────────────┴────────────┘')

    elif mana < 10 and mana_bot < 10:
        print(quadro)
        print(f'│   {mana} Mana   │    {mana_bot} Mana  │')
        print('└────────────┴────────────┘')
    
    elif mana < 10 and mana_bot > 10:
        print(quadro)
        print(f'│   {mana} Mana   │   {mana_bot} Mana  │')
        print('└────────────┴────────────┘')

    elif mana_bot < 10 and mana > 10:
        print(quadro)
        print(f'│   {mana} Mana  │   {mana_bot} Mana   │')
        print('└────────────┴────────────┘')

    elif mana_bot < 100 and mana < 100: 
        print(quadro)
        print(f'│   {mana} Mana  │   {mana_bot} Mana  │')
        print('└────────────┴────────────┘')

    elif mana < 100 and mana_bot == 100:
        print(quadro)
        print(f'│   {mana} Mana  │  {mana_bot} Mana  │')
        print('└────────────┴────────────┘')

    elif mana_bot < 100 and mana == 100:
        print(quadro)
        print(f'│  {mana} Mana  │   {mana_bot} Mana  │')
        print('└────────────┴────────────┘')
