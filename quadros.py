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

        if nova_vida == 0:
            vingança(nova_vida, mana)
            break
        vingança(nova_vida, mana)
        time.sleep(0.1)
  
def dano_player(vida, vida1, mana, mana1, poder, c):

    if poder == 21:
        c += 10

    for d in range(c):
        sys.stdout.write("\033[F" * 14)
        sys.stdout.flush()

        nova_vida = vida - d

        if nova_vida == 0:
            magos(nova_vida, vida1, mana, mana1)
            time.sleep(0.5)
            break

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
        if nova_vida == 0:
            magos(vida, nova_vida, mana, mana1)
            time.sleep(0.5)
            break

        magos(vida, nova_vida, mana, mana1)
        time.sleep(0.1)

def estouro_mago(vida, vida1, mana, mana1, c):
    for d in range(c + 1):
        sys.stdout.write("\033[F" * 9)
        sys.stdout.flush()

        nova_vida = vida1 - d
        nova_mana = mana1 - d
        if nova_mana == 0:
            magos(vida, nova_vida, mana, nova_mana)
            break

        time.sleep(0.1)
        magos(vida, nova_vida, mana, nova_mana)

def estouro_player(vida, vida1, mana, mana1, c):
    for d in range(c + 1):
        sys.stdout.write("\033[F" * 9)
        sys.stdout.flush()

        nova_vida = vida - d
        nova_mana = mana - d
        if nova_mana == 0:
            magos(nova_vida, vida1, nova_mana, mana1)
            break
        
        time.sleep(0.1)
        magos(nova_vida, vida1, nova_mana, mana1)

def mana_empate(vida, vida1, mana, mana1, c):

    for d in range(c + 1):
        sys.stdout.write("\033[F" * 9)
        sys.stdout.flush()

        nova_mana = mana - d
        if nova_mana == 0:
            magos(vida, vida1, nova_mana, mana1)
            break

        magos(vida, vida1, nova_mana, mana1)
        time.sleep(0.1)
    

    for d in range(c + 1):
        sys.stdout.write("\033[F" * 9)
        sys.stdout.flush()

        nova_mana2 = mana1 - d
        if nova_mana2 == 0:
            magos(vida, vida1, nova_mana, nova_mana2)
            break

        magos(vida, vida1, nova_mana, nova_mana2)
        time.sleep(0.1)

def vingança_HP(vida, mana, c):
    for d in range(c + 1):
        sys.stdout.write("\033[F" * 5)
        sys.stdout.flush()

        nova_vida = vida + d
        if nova_vida == 100:
            vingança(nova_vida, mana)
            break
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
