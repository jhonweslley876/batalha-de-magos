import os
import random
import time
import sys

def escrever_texto(texto, velocidade=0.06):
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

def magos(vida1, vida2, mana, mana_bot): # estatísticas do jogador e mago
    quadro = '+------------+-----------+'
    print(quadro)
    print( '|    VOCÊ    |    MAGO   |')
    print(quadro)
    print(f'|   {vida1} HP   |   {vida2} HP  |')
    print(quadro)
    print(f'|  {mana} Mana  | {mana_bot} Mana  |')
    print(quadro)

def regras(): # tabela de regras do jogo
    tabela = '+-----------------------------------------------+'
    print(tabela)
    print('|                   REGRAS                        |')
    print('| |')

carregamento()
escrever_texto('\nJogo carregado.')

player = 100
mago = 100
mana1 = 100
mana2 = 100

while player > 0 or mago > 0:

    magos(player, mago, mana1, mana2)

    baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
    random.shuffle(baralho)

    def formatar_carta(carta):
        if carta == 1:
            return 'A'
        if carta == 10:
            return random.choice(['K', 'Q', 'J'])
        return str(carta)

    cartas = [baralho.pop(), baralho.pop()]
    total = sum(cartas)

    tabela2 = '__________________________________________________'
    
    print(tabela2)
    print(f'Suas cartas são: {", ".join(formatar_carta(c) for c in cartas)}')
    print(f'Seu total é: {total}')

    while True:
        print(tabela2)
        compras = input('Comprar ou Finalizar?: ').strip().lower()

        if compras == 'comprar':
            if mana1 < 10:
                escrever_texto('Mana insuficiente para comprar cartas')
                break
            
            os.system('cls')
            print(tabela2)
            nova_carta = baralho.pop()
            total += nova_carta
            cartas.append(nova_carta)
            mana1 -= 10

            print(f'Carta comprada: {formatar_carta(nova_carta)}.')
            print(f'Suas cartas: {", ".join(formatar_carta(c) for c in cartas)}.')
            print(f'Seu total é: {total}.')

            if total > 21:
                break

        elif compras == 'finalizar':
            os.system('cls')
            break

        else:
            os.system('cls')
            escrever_texto('Digite apenas "comprar" ou "finalizar"!')

    print('__________________________________________________')

    if total == 21:
        print('Parabéns, você ganhou!')
        print('Dano crítico por valor 21!')
        for i in range(30):
            dano = random.randint(1, 20)
            print(f'\r{dano} ATK', end=' ', flush=True)
            time.sleep(0.1)
        print(f'\n{dano} + 10 ATK')
        mago -= dano + 10
        escrever_texto(f'\nMago sofreu {dano + 10} de dano.')

    else:
        os.system('cls')

        print('__________________________________________________')
        cartas_bot = [baralho.pop(), baralho.pop()]
        bot_total = sum(cartas_bot)

        print(f'Bot 1: {", ".join(formatar_carta(c) for c in cartas_bot)}')
        print(f'Bot 1: {bot_total}')

        while bot_total < 16:

            nova_carta = baralho.pop()
            cartas_bot.append(nova_carta)
            bot_total += nova_carta
            mana2 -= 10

            print(f'Bot 1 comprou: {formatar_carta(nova_carta)}')

            os.system('cls')
            print(f'Cartas Bot 1: {", ".join(formatar_carta(c) for c in cartas_bot)}')
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
            print('Bot 1 estourou o valor.')
            print('Você venceu o jogo!')
            print(f'Mago: {bot_total}')
            print(f'Seu total: {total}')

            for i in range(30):
                dano = random.randint(1, 20)
                print(f'\r{dano}', end=' ', flush=True)
                time.sleep(0.1)

            mago -= dano
            escrever_texto(f'\nMago sofreu {dano} de dano.')

        elif bot_total == 21:

            if total == 21:
                print('Mago ganhou com 21!')
                print('Dano crítico por valor 21!')
                for i in range(30):
                    dano = random.randint(1, 20)
                    print(f'\r{dano} ATK', end=' ', flush=True)
                    time.sleep(0.1)
                print(f'\n{dano} + 10 ATK')
                player -= dano + 10
                escrever_texto(f'\nVocê sofreu {dano + 10} de dano.')

        elif total > bot_total:
                print('Você ganhou!')
                print(f'Mago: {bot_total}')
                print(f'Seu total: {total}')

                for i in range(30):
                    dano = random.randint(1, 20)
                    print(f'\r{dano}', end=' ', flush=True)
                    time.sleep(0.1)

                mago -= dano
                escrever_texto(f'\nMago sofreu {dano} de dano.')

        elif bot_total > total:
            print('bot 1 ganhou!')
            print(f'Mago: {bot_total}')
            print(f'Seu total: {total}')

            for i in range(30):
                dano = random.randint(1, 20)
                print(f'\r{dano}', end=' ', flush=True)
                time.sleep(0.1)

            player -= dano
            escrever_texto(f'\nVocê sofreu {dano} de dano.')

    if player <= 0:
        magos(player, mago)
        print(f'Que pena, você perdeu todo o seu HP. Tente novamente.')
        break

    elif mago <= 0:
        magos(player, mago)
        escrever_texto('Parabéns, você venceu o mago!')

    cont = 1 # quantidade de vingança

    if cont == 1: #cena da vingança
        if mago <= 15:
            print(f'| {mana2} Mana  |') # tabela do mago para reviravolta
            # opção de poupar e matar
        cont -= 1 # vingança aparece apenas uma vez no jogo


    continuar = input('Deseja continuar jogando? (s/n): ').strip().lower()
    os.system('cls')
    mana1 += 5
    mana2 += 5
    if mana1 > 100:
        mana1 = 100
    if mana2 > 100:
        mana2 = 100

    if continuar != 's':

        os.system('cls')

        print('Vida final do jogo:')
        magos(player, mago, mana1, mana2)

        print('saindo...')
        carregamento()
        escrever_texto('\nSistema finalizado.')
        break