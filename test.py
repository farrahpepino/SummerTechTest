from random import randrange

def printBoard(board):
  print("   A  B  C  D  E  F  G  H")
  for i in range(len(board)):
    print(i, end = " ")
    for j in range(len(board[i])):
      print(board[i][j], end = "")
    print()

def makeBoard(board):
  for i in range(8):
    board.append([])
    for j in range(8):
      board[i].append("[ ]")

def validateXY(board, x, y):
  if (y < 0):
    return False
  elif (y >= len(board)):
    return False
  elif (x < 0):
    return False
  elif (x >= len(board[y])):
    return False
  else:
    return True

#Challenge: Could be further simplified, how?
def validatePlacement(board, x, y, direction, shipLength):
  if (direction == "up"):
    for i in range(shipLength):
      if (validateXY(board, x, y - i) and board[y][x] == "[ ]"):
        pass
      else:
        return False
    return True
  if (direction == "down"):
    for i in range(shipLength):
      if (validateXY(board, x, y + i) and board[y][x] == "[ ]"):
        pass
      else:
        return False
    return True
  if (direction == "right"):
    for i in range(shipLength):
      if (validateXY(board, x + i, y) and board[y][x] == "[ ]"):
        pass
      else:
        return False
    return True
  if (direction == "left"):
    for i in range(shipLength):
      if (validateXY(board, x - i, y) and board[y][x] == "[ ]"):
        pass
      else:
        return False
    return True

def placeShip(board, x, y, direction, shipLength):
  if (direction == "up"):
    for i in range(shipLength):
      board[y-i][x] = "[O]"
  elif (direction == "down"):
    for i in range(shipLength):
      board[y+i][x] = "[O]"
  elif (direction == "right"):
    for i in range(shipLength):
      board[y][x+i] = "[O]"
  elif (direction == "left"):
    for i in range(shipLength):
      board[y][x-i] = "[O]"


#Challenge: Could be simplified/extended with a dictionary.
def letterToCoordinate(letter):
  if (letter == "A"):
    return 0
  elif (letter == "B"):
    return 1
  elif (letter == "C"):
    return 2
  elif (letter == "D"):
    return 3
  elif (letter == "E"):
    return 4
  elif (letter == "F"):
    return 5
  elif (letter == "G"):
    return 6
  elif (letter == "H"):
    return 7

def checkWinner(board):
  count = 0
  for i in range(len(board)):
    for j in range(len(board[0])):
      if (board[i][j] == "[X]"):
        count += 1

  #Count the number of hits, 17 hits means all ships have been hit
  if (count == 17):
    return True
  else:
    return False

"""
makeMove may be deceptively tricky for a student. The computer make it's move
by passing playerBoard as both the master and the view. If a student conceptualizes
this as two separate functions, (or just places this code in the while-loop), it is 
completely fine.
"""
def makeMove(master, view, x, y):
  if (master[y][x] == "[O]"):
    view[y][x] = "[X]" #Hit!
  else:
    view[y][x] = "[*]" #Miss!


playerBoard = []
guessingBoard = []
computerBoard = []

shipSizes = [2, 3, 3, 4, 5]

makeBoard(playerBoard)
makeBoard(guessingBoard)
makeBoard(computerBoard)

print("Time to place your ships!")

placingShips = True
playerTurn = True
computerTurn = True
playing = True

for shipSize in shipSizes:
  
  placingShips = True
  while(placingShips == True):
    printBoard(playerBoard)
    print("This next ship is", shipSize)
    col = letterToCoordinate(input("Select a column for your ship [A-H]: "))
    row = int(input("Select a row for your ship [0-7]: "))
    direction = input("Choose a direction for your ship. [up, down, left, right]")
    if (validatePlacement(playerBoard, col, row, direction, shipSize)):
        placeShip(playerBoard, col, row, direction, shipSize)
        placingShips = False

for shipSize in shipSizes:
  
  placingShips = True
  while(placingShips == True):
    
    row = randrange(0, len(computerBoard))
    col = randrange(0, len(computerBoard[0]))
    directions = ["up", "down", "left", "right"]
    direction = directions[randrange(0, len(directions))]
                                     
    if (validatePlacement(computerBoard, col, row, direction, shipSize)):
      placeShip(computerBoard, col, row, direction, shipSize)
      placingShips = False
                                     

while (playing == True):
  
  printBoard(playerBoard)
  printBoard(guessingBoard)
  
  print("Your turn!")
  playerTurn = True
  while (playerTurn == True):
    col = letterToCoordinate(input("Pick a column [A-H]: "))
    row = int(input("Select a row for your ship [0-7]: "))
    if (validateXY(computerBoard, col, row) == True):
      makeMove(computerBoard, guessingBoard, col, row)
      playerTurn = False

  if (checkWinner(guessingBoard) == True):
    playing = False
    print("You win!")
    break

  computerTurn = True
  while (computerTurn == True):
    row = randrange(0, len(playerBoard))
    col = randrange(0, len(playerBoard[0]))
    if (validateXY(playerBoard, col, row) == True):
      makeMove(playerBoard, playerBoard, col, row)
      computerTurn = False
  
  if (checkWinner(playerBoard) == True):
    print("You lost!")
    playing = False