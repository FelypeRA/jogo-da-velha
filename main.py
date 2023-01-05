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

jogo = [
['', '', ''],
['', '', ''],
['', '', ''],
]
tela()

jogadores = {'jogador 1': '', 'jogador 2': ''}
jogador = list()
for jog in jogadores.keys():
  jogador.append(str(input(f'Qual nome do {jog} : ')))
  if jog == 'jogador 1':
    jogador.append(str(input('Deseja jogar com X ou O: ')))
  else:
    if jogadores['jogador 1'][1] == 'x':
      jogador.append('o')
    else:
      jogador.append('x')
  jogadores[jog] = jogador[:]
  jogador.clear()
print(jogadores)

print('')
while True:
  linha = int(input('Linha: '))
  coluna = int(input('Coluna: '))
  jogo[linha][coluna] = 'X'
  os.system("cls")
  tela()
