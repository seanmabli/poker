import numpy as np
import os

deck = np.array([['A', 'C'], ['2', 'C'], ['3', 'C'], ['4', 'C'], ['5', 'C'], ['6', 'C'], ['7', 'C'],['8', 'C'], ['9', 'C'], ['10', 'C'], ['J', 'C'], ['Q', 'C'], ['K', 'C'], ['A', 'D'], ['2', 'D'], ['3', 'D'], ['4', 'D'], ['5', 'D'], ['6', 'D'], ['7', 'D'],['8', 'D'], ['9', 'D'], ['10', 'D'], ['J', 'D'], ['Q', 'D'], ['K', 'D'], ['A', 'H'], ['2', 'H'], ['3', 'H'], ['4', 'H'], ['5', 'H'], ['6', 'H'], ['7', 'H'],['8', 'H'], ['9', 'H'], ['10', 'H'], ['J', 'H'], ['Q', 'H'], ['K', 'H'], ['A', 'S'], ['2', 'S'], ['3', 'S'], ['4', 'S'], ['5', 'S'], ['6', 'S'], ['7', 'S'],['8', 'S'], ['9', 'S'], ['10', 'S'], ['J', 'S'], ['Q', 'S'], ['K', 'S']])
np.random.shuffle(deck)

input('use enter to advance through the game')
os.system('clear')

playernames = np.array(['zain', 'adam']) # np.array(input("enter player names (seprated by comma's): ").strip().lower().split(','))
os.system('clear')

smallblind = 1 # int(input('small blind: '))
blind = np.array([smallblind, smallblind * 2])
os.system('clear')

cash = 200 # int(input('player starting cash: '))
playercash = np.array([cash] * len(playernames))
os.system('clear')

playercards = np.empty([len(playernames), 2, 2], str)
dealercards = np.empty([5, 2], str)

playerbets = np.zeros(playernames.shape, dtype=int)
playerbets[-2], playerbets[-1] = blind[0], blind[1]
aliveplayerbets = playerbets
minbet = blind[1]
pot = 0

playerfold = np.full(len(playernames), False, dtype=bool)

# dealing cards to players and dealer
for i in range(len(playernames)):
  for j in range(2):
    playercards[i, j] = deck[0]
    deck = deck[1:]

for i in range(5):
  dealercards[i] = deck[0]
  deck = deck[1:]

while all(element == aliveplayerbets[0] for element in aliveplayerbets) == False and any(playerfold == False) == True:
  for i in range(len(playernames)):
    if playerfold[i] == False:
      input('start ' + playernames[i] + "'s turn")
      print('cards: ' + playercards[i, 0, 0] + playercards[i, 0, 1] + ', ' + playercards[i, 1, 0] + playercards[i, 1, 1])
      print('cash: ' + str(playercash[i]))
      print('minimum bet: ' + str(minbet))
      print('current bet: ' + str(playerbets[i]))
      y = input('(b)et, (c)all, or (f)old: ').lower()
      if y == 'b' or y == 'bet':
        x = int(input('bet: '))
        playerbets[i] = minbet = x if minbet < x < playercash[i] else 0
      elif y == 'c' or y == 'call':
        playerbets[i] = minbet
      elif y == 'f' or y == 'fold':
        playerfold[i] = True
      os.system('clear')

  aliveplayerbets = playerbets
  for i in range(len(playernames)):
    if playerfold[i] == True:
      np.delete(aliveplayerbets, i)

pot = np.sum(playerbets)
playerbets = np.zeros(playernames.shape, dtype=int)

print(pot)