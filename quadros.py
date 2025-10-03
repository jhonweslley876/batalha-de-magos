import keyboard
import os
import time
import random
from funções import *

def vingança(vida, energia):

    if vida == 100:

        print('┌─────────────────────────────┐')
        print('│            mago             │')
        print('├──────────────┬──────────────┤')
        print(f'│    {vida} HP    │   {energia} MANA   │')
        print('└──────────────┴──────────────┘')

    elif vida < 10 and energia < 10:

        print('┌─────────────────────────────┐')
        print('│            mago             │')
        print('├──────────────┬──────────────┤')
        print(f'│     {vida} HP     │    {energia} MANA    │')
        print('└──────────────┴──────────────┘')

    elif vida < 10 or energia < 10:
        print('┌─────────────────────────────┐')
        print('│            mago             │')
        print('├──────────────┬──────────────┤')
        print(f'│     {vida} HP    │    {energia} MANA    │')
        print('└──────────────┴──────────────┘')


    elif vida < 100 and energia < 100:

        print('┌─────────────────────────────┐')
        print('│            mago             │')
        print('├──────────────┬──────────────┤')
        print(f'│     {vida} HP    │   {energia} MANA    │')
        print('└──────────────┴──────────────┘')

    elif vida < 100 or energia < 100:

        print('┌─────────────────────────────┐')
        print('│            mago             │')
        print('├──────────────┬──────────────┤')
        print(f'│     {vida} HP    │   {energia} MANA   │')
        print('└──────────────┴──────────────┘')

def ataque_vingança(vida, mana):
    
    c = random.randint(1, 20)

    for d in range(c):
        # 🧽 Limpa a tela ou o bloco anterior
        # os.system('cls')  # limpa a tela inteira
        sys.stdout.write("\033[F" * 5)  # 🔥 sobe 4 linhas (quantas linhas a tabela ocupa)
        sys.stdout.flush()
        # Atualiza e mostra a nova vida
        nova_vida = vida + d
        vingança(nova_vida, mana)
        time.sleep(0.1)

def dialogos(vida, vida_mago, mana, mana_mago):

    for c in range(30):

        var = random.randint(1, 20)
        print(f'\r{var} ATK', end=' ', flush=True)
        time.sleep(0.1)

    time.sleep(1)
    print('\n')

    if var < vida_mago:

        mensagem = "Você errou o ataque!"
        escrever_texto_na_caixa(mensagem, largura=60, velocidade=0.03)
        time.sleep(2)
        os.system('cls')
        ataque_vingança(vida_mago, mana_mago)
        mensagem = "Mago te ataca de volta em seguida."
        escrever_texto_na_caixa(mensagem, largura=40, velocidade = 0.08)
        for c in range(30):
            dano = random.randint(1, 20)
            print(f'\r{dano} ATK', end=' ', flush=True)
            time.sleep(0.1)
        vida -= dano
        print('\n')
        magos(vida, vida_mago, mana, mana_mago)
    elif var >= vida_mago:
        mensagem = "..."
        escrever_texto_na_caixa(mensagem, largura=3, velocidade=0.5)
        escrever_texto('Você acertou um golpe em cheio.')
        time.sleep(2)
        escrever_texto('Um golpe fatal para o mago.')
        time.sleep(0.5)
        escrever_texto('...')
        time.sleep(2)
  
def dano_player(vida, vida1, mana, mana1, poder, c):

    if poder == 21:
        c += 10

    for d in range(c):
        sys.stdout.write("\033[F" * 14)
        sys.stdout.flush()

        nova_vida = vida - d
        magos(nova_vida, vida1, mana, mana1)
        time.sleep(0.1)

def dano_mago(vida, vida1, mana, mana1, poder, c):
    time.sleep(2)
    if poder == 21:
        c += 10

    for d in range(c):
        sys.stdout.write("\033[F" * 9)
        sys.stdout.flush()

        nova_vida = vida1 - d
        magos(vida, nova_vida, mana, mana1)
        time.sleep(0.1)

def estouro_mago(vida, vida1, mana, mana1, c):
    for d in range(c + 1):
        sys.stdout.write("\033[F" * 9)
        sys.stdout.flush()

        nova_vida = vida1 - d
        nova_mana = mana1 - d
        if nova_mana < 0:
            nova_mana = 0
        time.sleep(0.1)
        magos(vida, nova_vida, mana, nova_mana)

def estouro_player(vida, vida1, mana, mana1, c):
    for d in range(c + 1):
        sys.stdout.write("\033[F" * 9)
        sys.stdout.flush()

        nova_vida = vida - d
        nova_mana = mana - d
        if nova_mana < 0:
            nova_mana = 0
        time.sleep(0.1)
        magos(nova_vida, vida1, nova_mana, mana1)

def mana_empate(vida, vida1, mana, mana1, c):
    for d in range(c + 1):
        sys.stdout.write("\033[F" * 9)
        sys.stdout.flush()

        nova_mana = mana - d
        magos(vida, vida1, nova_mana, mana1)
        time.sleep(0.1)
    
    for d in range(c + 1):
        sys.stdout.write("\033[F" * 9)
        sys.stdout.flush()

        nova_mana2 = mana1 - d
        magos(vida, vida1, nova_mana, nova_mana2)
        time.sleep(0.1)

def vingança_HP(vida, mana, c):
    for d in range(c + 1):
        sys.stdout.write("\033[F" * 5)
        sys.stdout.flush()

        nova_vida = vida + d
        time.sleep(0.1)
        vingança(nova_vida, mana)

def dialogo_mago():
    mensagem = "vc o deixa viver, dá as costas a ele e segue o seu caminho"
    escrever_texto_na_caixa(mensagem, largura=60, velocidade=0.05)
    time.sleep(1)

    mensagem = '...'
    escrever_texto_na_caixa(mensagem, largura=3, velocidade=0.5)
    time.sleep(1)

    mensagem = "você foi apunhalado pelas costas"
    escrever_texto_na_caixa(mensagem, largura=40, velocidade=0.1)
    time.sleep(1)

vidaa = 100
vida2 = 100
manaa = 100
manaa2 = 100
