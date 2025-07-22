board = []
for i in range(7):
    row = []
    for j in range(7):
        row.append("[ ]")
    board.append(row)

count = 0
turn = "[x]"
tracker = [6, 6, 6, 6, 6, 6, 6]

while count < 49 and count >= 0:
    for i in range(7):
        for j in range(7):
            print(board[i][j], end="")
        print()

    try:
        x = int(input("Choose a column [0-6]: "))
        if x < 0 or x > 6 or tracker[x] < 0:
            print("Invalid column. Try again.")
            continue
    except ValueError:
        print("Please enter a number between 0 and 6.")
        continue

    y = tracker[x]
    board[y][x] = turn
    tracker[x] -= 1
    count += 1

    for i in range(7):
        for j in range(4):
            if board[i][j] == turn and board[i][j+1] == turn and board[i][j+2] == turn and board[i][j+3] == turn:
                print(turn, "wins!")
                count = -1

    for i in range(7):
        for j in range(4):
            if board[j][i] == turn and board[j+1][i] == turn and board[j+2][i] == turn and board[j+3][i] == turn:
                print(turn, "wins!")
                count = -1

    for i in range(4):
        for j in range(4):
            if board[i][j] == turn and board[i+1][j+1] == turn and board[i+2][j+2] == turn and board[i+3][j+3] == turn:
                print(turn, "wins!")
                count = -1

    for i in range(3, 7):
        for j in range(4):
            if board[i][j] == turn and board[i-1][j+1] == turn and board[i-2][j+2] == turn and board[i-3][j+3] == turn:
                print(turn, "wins!")
                count = -1

    if turn == "[x]":
        turn = "[o]"
    else:
        turn = "[x]"
