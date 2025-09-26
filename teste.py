# import time
# import sys

# def escrever_texto(texto, velocidade=0.06):
#     for letra in texto:
#         sys.stdout.write(letra)   # escreve sem pular linha
#         sys.stdout.flush()        # força a impressão imediata
#         time.sleep(velocidade)    # controla a velocidade
#     print()

# print(f"""+-----------------+
# | {escrever_texto("Hello, world!")} |
# +-------------------+""")

import random


c = random.randint(100)
print(c)