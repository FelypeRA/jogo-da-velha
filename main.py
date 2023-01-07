import os

def tela():
  global jogo
  print('\033[036m-*\033[m' * 20)
  print(f'\033[032m{"JOGO DA VELHA":^40}\033[m')
  print('\033[036m-*\033[m' * 20)
  print('    \033[42m 0 \033[m   \033[42m 1 \033[m   \033[42m 2 \033[m')
  for index,linha in enumerate(jogo):
    print(f'\033[042m{index}:\033[m', end=' ')
    for ix,elemento in enumerate(linha):
      print(f' {elemento:^4}', end= '')
      if ix == 0 or ix == 1:
        print('|', end = '')

    print('\n   -----------------')

def dadosjogadores():
  jogador1.append(str(input("Qual o nome do jogador 1: ")))
  jogador1.append(str(input('Deseja jogar com X ou O: ')))
  jogador2.append(str(input("Qual o nome do jogador 2: ")))
  if jogador1[1] == 'X':
    jogador2.append(str('O'))
  else: 
    jogador2.append(str('X'))
                    
  os.system("clear")
  tela()


vencedor = ''
jogo = [
['', '', ''],
['', '', ''],
['', '', ''],
]

jogador1 = []
jogador2 = []
cont = 1

tela()
dadosjogadores()

while True:
  if cont % 2 != 0:
    print("Vez do jogador 1: ")
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))
    jogo[linha][coluna] = jogador1[1]
  else:
    print("Vez do jogador 2: ")
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))
    jogo[linha][coluna] = jogador2[1]
  os.system("clear")
  tela()
  for line in jogo:
    c = 0 
    for item in line:
      if item == 'X':
        c += 1
        if c == 3:         
          if jogador1[1] == 'X':
            vencedor = 'Jogador 1'
          else: 
            vencedor = 'Jogador 2  '
          break
      elif item == 'O':
        c += 1
        if c == 3:
          if jogador2[1] == 'O':
            vencedor = 'Jogador 2 TEST'
          else: 
            vencedor = 'Jogador 1'
          break
      if vencedor != '':
        break
  if vencedor != '':
     break
  if jogo[0][0] == jogo[1][1] == jogo[2][2] and jogo[0][0] != '':
    if jogador1[1] == 'X' or jogador1[1] == 'O':
      vencedor = 'Jogador 1'
      break
    else: 
      vencedor = 'Jogador 2'
      break
  if jogo[0][2] == jogo[1][1] == jogo[2][0] and jogo[0][2] != '':
    if jogador1[1] == 'X' or jogador1[1] == 'O':
      vencedor = 'Jogador 1'
      break
    else: 
      vencedor = 'Jogador 2'
      break
  cont += 1
print(f'{vencedor} venceu a partida!')
