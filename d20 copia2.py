import os
import random
import time
import sys
import keyboard
from quadros import *

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
    tabela = '├─────────────────────────────────────────────────────────────────────────┤'
    print('┌─────────────────────────────┬────────────┬──────────────────────────────┐')
    print('│                             │ COMO JOGAR │                              │')
    print('├─────────────────────────────┴────────────┴──────────────────────────────┤')
    print('│               Compre cartas para ter mais chances de ganhar.            │')
    print(tabela)
    print('│                 lembre-se: se passar de 21, você perde!                 │')
    print(tabela)
    print('│ Ao lado das opções terá um número. Escreva eles para escolher a opção.  │')
    print(tabela)
    print('│               Você gasta 10 de mana para comprar cartas.                │')
    print(tabela)
    print('│     Não se preocupe, você recupera 5 de mana ao final de cada turno.    │')
    print(tabela)
    print('│ Se estourar o valor (passar de 21) ou perder por menor número, um valor │')
    print('│ de 1 a 20 será escolhido para o dano final.                             │')
    print(tabela)
    print('│    Um valor total de 21 nas cartas resultará em um bônus de +10 ATK     │')
    print('└─────────────────────────────────────────────────────────────────────────┘')

# carregamento inicial do jogo, regras e diálogos
carregamento()
escrever_texto('\nJogo carregado.')
time.sleep(2)
os.system('cls') # limpa o terminal para deixar a interface mais limpa
regras()
escrever_texto('Pressione "enter" para passar.')

keyboard.wait('enter')
input('') # espaço vazio para ajustar o wait('enter')
os.system('cls')

dialogo()

player = 100 # vida do jogador
mago = 100 # vida do mago
mana_player = 100 # mana do jogador
mana_mago = 100 # mana do mago

while player > 0 or mago > 0: 

    magos(player, mago, mana_player, mana_mago) # tabela de estatísticas dos jogadores

    baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
    random.shuffle(baralho) # embaralha aleatoriamente

    def formatar_carta(carta):
        if carta == 1:
            return 'A'
        if carta == 10:
            return random.choice(['K', 'Q', 'J'])
        return str(carta)

    cartas = [baralho.pop(), baralho.pop()] # cartas do jogador
    total = sum(cartas) # pontuação total do jogador

    tabela2 = '__________________________________________________'
    
    print(tabela2)
    print(f'Suas cartas são: {", ".join(formatar_carta(c) for c in cartas)}') # mostra as cartas
    print(f'Seu total é: {total}') # pontuação total do jogador

    while True:
        print(tabela2)
        print('┌───┬─────────┬───┬───────────┐')
        print('│ 1 │ comprar │ 2 │ finalizar │')
        print('└───┴─────────┴───┴───────────┘')
        compras = int(input('Digite a sua escolha:  ')) # sistema de compra de cartas

        if compras == 1:
            if mana_player < 10: # se o jogador não tiver mana, para de comprar
                escrever_texto('Mana insuficiente para comprar cartas')
                break
            
            os.system('cls')
            print(tabela2)
            nova_carta = baralho.pop() #pega uma nova carta da lista e exclui ela da lista (igual um baralho normal)
            total += nova_carta
            cartas.append(nova_carta) # adiciona essa carta na sua mão
            mana_player -= 10

            print(f'Carta comprada: {formatar_carta(nova_carta)}.')
            print(f'Suas cartas: {", ".join(formatar_carta(c) for c in cartas)}.')
            print(f'Seu total é: {total}.')

            if total > 21:
                break

        elif compras == 2:
            os.system('cls')
            break

        else:
            os.system('cls')
            escrever_texto('Digite apenas "comprar" ou "finalizar"!')

    print('__________________________________________________')

    if total == 21:
        print('Parabéns, você ganhou!')
        print('Dano crítico por valor 21!')

        for i in range(30): # sistema de dano
            dano = random.randint(1, 20) # escolhe aleatóriamente entre 1 e 20
            print(f'\r{dano} ATK', end=' ', flush=True) # imprime a variável na mesma linha apagando a mensagem anterior
            time.sleep(0.1)
        print(f'\nVocê: {dano} + 10 ATK')
        mago -= dano + 10

        escrever_texto(f'\nMago sofreu {dano + 10} de dano.')

    else:
        os.system('cls')

        print('__________________________________________________')
        cartas_bot = [baralho.pop(), baralho.pop()]
        bot_total = sum(cartas_bot)

        print(f'Mago: {", ".join(formatar_carta(c) for c in cartas_bot)}')
        print(f'Mago: {bot_total}')

        while bot_total < 16:

            nova_carta = baralho.pop()
            cartas_bot.append(nova_carta)
            bot_total += nova_carta
            mana_mago -= 10

            print(f'Bot 1 comprou: {formatar_carta(nova_carta)}')

            os.system('cls')
            print(f'Cartas do mago: {", ".join(formatar_carta(c) for c in cartas_bot)}')
            print(tabela2)

            escrever_texto(f'Valor total do mago: {bot_total}')
            print(tabela2)

            print(f'Seu total: {total}')
            print('__________________________________________________')
            
        if total > 21:
            os.system('cls')
            print('__________________________________________________')
            print(f'Você perdeu. Seu total de pontos é {total}, maior que 21!')

            for i in range(30):
                dano = random.randint(1, 20)
                print(f'\r{dano}', end=' ', flush=True)
                time.sleep(0.1)
            player -= dano
            escrever_texto(f'\nVocê sofreu {dano} de dano.')

        elif bot_total > 21:
            print('Mago estourou o valor.')
            print('Você venceu o jogo!')
            print('__________________________________________________')
            print(f'Mago: {bot_total}')
            print(f'Seu total: {total}')
            print('__________________________________________________')

            for i in range(30):
                dano = random.randint(1, 20)
                print(f'\r{dano}', end=' ', flush=True)
                time.sleep(0.1)

            mago -= dano
            escrever_texto(f'\nMago sofreu {dano} de dano.')

        elif bot_total == 21:
            print('Mago ganhou com 21!')
            print('Dano crítico por valor 21!')
            print('__________________________________________________')
            for i in range(30):
                dano = random.randint(1, 20)
                print(f'\r{dano} ATK', end=' ', flush=True)
                time.sleep(0.1)
            print(f'\n{dano} + 10 ATK')
            player -= dano + 10

            escrever_texto(f'\nVocê sofreu {dano + 10} de dano.')

        elif total > bot_total:
                print('Você ganhou!')
                print('__________________________________________________')
                print(f'Mago: {bot_total}')
                print(f'Seu total: {total}')
                print('__________________________________________________')

                for i in range(30):
                    dano = random.randint(1, 20)
                    print(f'\r{dano}', end=' ', flush=True)
                    time.sleep(0.1)

                mago -= dano
                escrever_texto(f'\nMago sofreu {dano} de dano.')

        elif bot_total > total:
            print('Mago ganhou!')
            print('__________________________________________________')
            print(f'Mago: {bot_total}')
            print(f'Seu total: {total}')
            print('__________________________________________________')

            for i in range(30):
                dano = random.randint(1, 20)
                print(f'\r{dano}', end=' ', flush=True)
                time.sleep(0.1)

            player -= dano
            escrever_texto(f'\nVocê sofreu {dano} de dano.')

        elif bot_total == total:
            escrever_texto('Empate, ambos perderam 10 de mana.')
            mana_mago -= 10
            mana_player -= 10

    if player <= 0:
        player = 0
        magos(player, mago, mana_player, mana_mago)
        print(f'Que pena, você perdeu todo o seu HP. Tente novamente.')
        break

    elif mago <= 0:
        mago = 0
        magos(player, mago, mana_player, mana_mago)
        escrever_texto('Parabéns, você venceu o mago!')

    cont = 1 # quantidade de vingança

    if cont == 1: #cena da vingança
        if mago <= 15:
            vingança(mago, mana_mago) # tabela do mago para reviravolta
        cont -= 1 # vingança aparece apenas uma vez no jogo


    continuar = input('Deseja continuar jogando? (s/n): ').strip().lower()
    os.system('cls')
    mana_player += 5
    mana_mago += 5
    if mana_player > 100:
        mana_player = 100
    if mana_mago > 100:
        mana_mago = 100

    if continuar == 'n':

        os.system('cls')

        print('Vida final do jogo:')
        magos(player, mago, mana_player, mana_mago)

        print('saindo...')
        carregamento()
        escrever_texto('\nSistema finalizado.')
        break
    elif continuar == 's':
        continue