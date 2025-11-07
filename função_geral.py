import os
import random
import time
import sys
import keyboard

#textos

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
        if keyboard.is_pressed('enter'):
            break
        sys.stdout.write(" " * (largura - len(linha)) + " │\n")  # Preenche o resto da linha
    # Move o cursor para baixo até fora da caixa
    print("\033[" + str(len(linhas)) + "B", end="")

def dialogo(): # dialogo inicial
    mensagem = "Olá, pequeno viajante!"
    escrever_texto_na_caixa(mensagem, largura=40, velocidade=0.03)

    input('')
    os.system('cls')

    mensagem = "Um mago muito poderoso está na cidade!"
    escrever_texto_na_caixa(mensagem, largura=50, velocidade=0.03)

    input('')
    os.system('cls')

    mensagem = "Ele parece desafiar alguém para uma partida de black jack."
    escrever_texto_na_caixa(mensagem, largura=60, velocidade=0.03)

    input('')
    os.system('cls')

def escrever_texto(msg, delay=0.06):
    for i, letra in enumerate(msg):
        print(letra, end='', flush=True)
        time.sleep(delay)
        if keyboard.is_pressed('enter'):
            print(msg[i+1:], end='', flush=True)
            break
    print() # quebra de linha no final

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
    input('') # espaço vazio para ajustar o wait('enter')
    os.system('cls')


# jogabilidade

def magos(vida1, vida2, mana, mana_bot): # estatísticas do jogador e mago

    quadro = '├────────────┼────────────┤'
    
    if vida1 == 100 and vida2 == 100:
        print('┌────────────┬────────────┐')
        print('│    VOCÊ    │    MAGO    │')
        print(quadro)
        print(f'│   {vida1} HP   │   {vida2} HP   │')

    elif vida1 == 100 and vida2 < 10:
        print('┌────────────┬────────────┐')
        print('│    VOCÊ    │    MAGO    │')
        print(quadro)
        print(f'│   {vida1} HP   │    {vida2} HP    │')
    
    elif vida1 == 100 and vida2 < 100:
        print('┌────────────┬────────────┐')
        print('│    VOCÊ    │    MAGO    │')
        print(quadro)
        print(f'│   {vida1} HP   │    {vida2} HP   │')

    elif vida1 < 10 and vida2 < 10:
        print('┌────────────┬────────────┐')
        print('│    VOCÊ    │    MAGO    │')
        print(quadro)
        print(f'│     {vida1} HP    │     {vida2} HP    │')
    
    elif vida1 < 10 or vida2 < 10:
        print('┌────────────┬────────────┐')
        print('│    VOCÊ    │    MAGO    │')
        print(quadro)
        print(f'│    {vida1} HP    │   {vida2} HP    │')
    
    elif vida1 < 100 and vida2 < 100:
        print('┌────────────┬────────────┐')
        print('│    VOCÊ    │    MAGO    │')
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


# banco de dados e login

import sqlite3

def conectar():
    return sqlite3.connect('jogo.db')

def criar_tabela():
    conexão = conectar()
    cursor = conexão.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS jogo(
        nome TEXT NOT NULL PRIMARY KEY,
        senha TEXT NOT NULL,
        nivel INTEGER DEFAULT 1
        )
    ''')

    conexão.commit()
    conexão.close()

def inserir(nome, senha, nivel=1):
    conexão = conectar()
    cursor = conexão.cursor()
    cursor.execute('INSERT INTO jogo(nome, senha, nivel) VALUES(?,?,?)', (nome, senha, nivel))
    conexão.commit()
    conexão.close()

def listar():
    conexão = conectar()
    cursor = conexão.cursor()
    cursor.execute('SELECT * FROM jogo')
    for linha in cursor.fetchall():
        print(linha)
    conexão.close()

def buscar_jogador(nome):
    conexão = conectar()
    cursor = conexão.cursor()
    cursor.execute('SELECT * FROM jogo WHERE nome=?', (nome,))
    jogador = cursor.fetchone()
    conexão.close()
    return jogador

def atualizar_level(nome, novo_level):
    conexão = conectar()
    cursor = conexão.cursor()
    cursor.execute('UPDATE jogo SET nivel=? WHERE nome=?', (novo_level, nome))
    conexão.commit()
    conexão.close()

def excluir(nome):
    conexão = conectar()
    cursor = conexão.cursor()
    cursor.execute('DELETE FROM jogo WHERE nome=?', (nome,))
    conexão.commit()
    conexão.close()

def login():
    apollo = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%¨&*(),.;:/?~´ãéàÀÉÃêÊçÇ[]{}º°+-=_§¹²³£¢¬""'
    contador = 0
    criar = False
    espaço = False

    print('┌───┬─────────────┬───┬─────────────────┐')
    print('│ 1 │ CRIAR CONTA │ 2 │   FAZER LOGIN   │')
    print('└───┴─────────────┴───┴─────────────────┘')

    n = int(input())

    os.system('cls')
    while True:
        if n == 1:
            print('Digite o nome do seu personagem')
            print(f'''┌───────────────────────────────────────────────────┐
                                                    │
└───────────────────────────────────────────────────┘''')

            sys.stdout.write("\033[F" * 2)
            sys.stdout.flush()

            nome = input('│ User: ')
            jogador = buscar_jogador(nome)
            time.sleep(1.5)
            os.system('cls')
            nível = 1

            for c in nome:
                if c in apollo:
                    contador = 1
                    break

            tamanho = len(nome)

            if tamanho < 2:
                print('Seu nick deve conter pelo menos 2 caracteres!')

            elif contador == 1:
                if not jogador:

                    print('Digite a senha da sua conta')
                    while True:
                        print(f'''┌─────────────────────────────────────────────────────────────────┐
                                                                  │
└─────────────────────────────────────────────────────────────────┘''')

                        sys.stdout.write("\033[F" * 2)
                        sys.stdout.flush()
                        senha = input('│ Senha: ')
                        time.sleep(1.5)
                        os.system('cls')

                        for d in senha:
                            if d == ' ':
                                espaço = True
                                break

                        if senha == '':
                            print('Digite uma senha válida!')
                            espaço = False
                        elif espaço == False:
                            print('Conta criada com sucesso.')
                            inserir(nome, senha, nível)
                            criar = True
                            break
                        else:
                            print('Digite uma senha válida!')
                            espaço = False
                        
                    time.sleep(1.5)
                    os.system('cls')

                    if criar == True:
                        break

                else:
                    print('Este nome de usuário já existe, tente outro.')
                    time.sleep(1.5)
                    os.system('cls')
            else:
                print('Você não pode deixar o seu nome em branco.')

        elif n == 2:
            print(f'''┌───────────────────────────────────────────────────┐
            │                                       │
└───────────────────────────────────────────────────┘''')

            sys.stdout.write("\033[F" * 2)
            sys.stdout.flush()

            nome = input('│ Nome de usuário: ')
            jogador = buscar_jogador(nome)
            
            time.sleep(1)
            os.system('cls')

            if jogador:
                while True:
                    print(f'''┌──────────────────────────────────────────────────────────┐
                                                           │
└──────────────────────────────────────────────────────────┘''')
                    nível = jogador[2]
                    sys.stdout.write("\033[F" * 2)
                    sys.stdout.flush()
                    senha = input('│ Digite a sua senha: ')
                    time.sleep(1)
                    os.system('cls')

                    if senha == jogador[1]:
                        escrever_texto(f'bem vindo jogador {jogador[0]}, seu nível é {jogador[2]}')
                        time.sleep(2)
                        os.system('cls')
                        criar = True
                        break
                    elif senha != jogador[1]:
                        print('Senha incorreta. (para sair do login aperte "0")')

                    elif senha == 0:
                        print('Saindo...')
                        break
                if criar == True:
                    break
            elif nome == '0':
                    print('┌───┬─────────────┬───┬─────────────────┐')
                    print('│ 1 │ CRIAR CONTA │ 2 │   FAZER LOGIN   │')
                    print('└───┴─────────────┴───┴─────────────────┘')

                    n = int(input())
            elif not jogador:
                print('Esse usuário não existe. (aperte 0 para voltar para o inicio)')
        else:
            print('Digite apenas 1 ou 2 para escolher.')

    os.system('cls')
    return nome
